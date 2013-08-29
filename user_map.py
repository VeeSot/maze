# encoding:utf-8
"""Обработка пользовательской карты"""
from processing_io import show_labirinth, promt, show_way,final_check
from re import findall, sub
from numpy import int, zeros, argwhere
from DFS import *
from time import sleep
from  BFS import *
way = [['Y'], ['X']]

class ManyIO(Exception):
    """Много точек вход-выхода"""
    pass


class NotCorrectValue(Exception):
    """Случай когда пользователь вбивает в лабиринт-постороние цифры"""
    pass

class NotEqalLen(Exception):
    """Строки разной длины"""
    pass


def read_out_file():
    # Попытка получить файл на диске
    try:
        raw_input('''Уважаемый пользователь.ниже написана небольшая инструкция
После ее прочтения и выполнения - нажмите клавишу "Enter"
1.Карта должна лежать в одной папке с исполняемой программой(скриптом)
2.Карта должна иметь имя "field".Без кавычек
3.Карта должна представлять из себя матрицу чисел,в которой могут и долны встречаться числа O, 1, 2, 3
4.Начало пути отмечается цифрой "2". Окончание - цифрой "3".Проходимые участки - цифрой "0". Непроходимые - цифрой "1"
5.Пример карты лежит в папке с программой и назван "example_field"
6.Если вы все поняли и выполнили - нажмите 'Enter' и добро пожаловать в лабиринт''')
        # Читам что нам там подарил юзер
        all_file = str(open('field').readlines())
        file_check(all_file)
        # Получим первую строку и потом из нее узнаем сколько в ней чисел
        input_value = open('field')
        first_string = input_value.readline().rstrip()
        total_elements_in_string = len(findall('(\d+)', first_string))
        M = total_elements_in_string + 2
        # Количество строк в файле
        N = len(open('field').readlines()) + 2
        # Переоткроем файл и начнем читать с первой строки
        input_value = open('field')
        field = buildin_field(total_elements_in_string, input_value)
        # Но это полдела.Надо конвертнуть
        xfield = convert_type_maze(field, N, M)
        # Покажем юзеру наше творение
        show_labirinth(N, M, xfield)

        print "Наш лабиринт!"
        sleep(2)
        # Получим координаты старта и финиша.
        S = argwhere(xfield == 2)[0]
        F = argwhere(xfield == 3)[0]
        # Затрем отметку старта(для лучшей визуализации) и...
        xfield[S[0]][S[1]] = 0
        # Запустим поиск!
        x = promt('search')
        if x == 2:
            Bway,Bfield = BFS(field, S, F)
            check = final_check(Bfield, F)
            if check:
                show_way(Bway)
                show_labirinth(N, M, Bfield)
        elif x == 1:
            DFS(S[0], S[1], field, S, F, way)
            check = final_check(field, F)
            if check:
                show_way(way)
                show_labirinth(N, M, field)
    except IOError:
        print "Проблемы с доступом к файлу." \
              "Проверьте наличие файла согласно инструкции " \
              "или создайте его если такового не имеется" +   '\n'
    except NotCorrectValue:
        print "В карте лабиринта обнаружены неверные входные данные" \
              "(числа отличные от требований программы)" +   '\n'
    except ManyIO:
        print "В вашей карте более одного входа или выхода." \
              "Исправьте входные данные" +   '\n'
    except NotEqalLen():
        print "В вашей карте имеются строки разной длины." \
              "Исправьте входные данные" +   '\n'
    except IndexError:
        print "Упс!!Что то пошло не так," \
              "возможно вы не указали точку начала или окончания пути"
    except:
        print "Что то пошло не так...Проверьте входные данные и повторите" \
              " Если проблема повторяется-обратитесь к разработчику" +   '\n'






def buildin_field(total_elements_in_string, input_value):
    """Займемся сборкой игрового поля из того что нам подарил юзер"""
    # Новый список туда будем складывать все строки
    field = []
    string_field = []
    # И сразу же построим верхнюю стенку
    for x in xrange(total_elements_in_string + 2):
        string_field.append(-1)
    field.append(string_field)
    i = 1
    while i <= len(open('field').readlines()):
        string_content = input_value.readline().rstrip()
        # Немного движений ушами дабы преобразовать непустую строку в список
        if string_content != '':
            # Заморочка на юзабельность  и внешний вид
            # чтобы модифицировать единички в (-1)стенки
            string_content = sub('1', '-1', string_content)
            string_content = findall('(-*\d+)', string_content)
            # Число цифр в строке.
            # Контролируем дабы не было лабиринта со строками разного уровня
            if len(string_content) != total_elements_in_string:
                raise NotEqalLen
                # А потом все добавить в список который будет строкой-частью поля
            # И плюсом два элемента стенки по бокам
            del string_field[:]
            string_field.append(-1)
            for x in string_content:
                string_field.append(int(x))
            string_field.append(-1)
            field.append(string_field[:])
            i += 1
            # Как только выйдем из вайла-добавим нижнюю стенку.
    del string_field[:]
    for x in xrange(total_elements_in_string + 2):
        string_field.append(-1)
    field.append(string_field)
    return  field


def file_check(all_file):
# Если файл прочитался-не значит что он корректный.
# Отлавливаем всякие гадости и бросаем исключения
    # Наличие постороних цифр
    all_numbers_in_files = findall('(-*\d+)', all_file)
    for x in all_numbers_in_files:
        if x != '0':
            if x != '1':
                if x != '2':
                    if x != '3':
                        raise NotCorrectValue
        # Слишком много входных или выходных координат
    two = []
    three = []
    for x in all_numbers_in_files:
        if x == '2':
            two.append(x)
        elif x == '3':
            three.append(x)
    if len(two)>1 or len(three)>1:
        raise ManyIO



def convert_type_maze(field, N, M):
    """Получим лабиринт из вложеных списков.
       Превратим его в лабиринт-массив из NumPy"""
    xfield = zeros((N, M), dtype=int)
    y = 0
    while y < N:
        xfield[y] = field[y]
        y += 1
    return xfield