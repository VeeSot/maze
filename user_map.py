#encoding:utf-8
"""Обработка пользовательской карты"""
from processing_io import show_labirinth, promt
from re import findall, sub
from numpy import int, zeros, argwhere
from DFS import *
from time import sleep
from  BFS import *


class InputError(Exception):
    pass


class ErrorFromUser(Exception):
    def not_way(self):
        print "В вашем лабиринте нет проходимых участков"


def read_out_file():
    #Попытка получить файл на диске
    try:
        raw_input("Уважаемый пользователь.ниже написана небольшая инструкция"+'\n'
                  ".После ее прочтения и выполнения - нажмите клавишу 'Enter' " +'\n'
                  "1.Карта должна лежать в одной папке с исполняемой программой(скриптом)" +'\n'
                  "2.Карта должна иметь имя 'field'.Без кавычек" +'\n'
                  "3.Карта должна представлять из себя матрицу чисел "
                  "в которой могут и долны встречаться числа O, 1, 2, 3"+'\n'
                  "4.Начало пути отмечается цифрой 2. Окончание-цифрой 3. "
                  "Проходимые участки-цифрой 0. Непроходимые -цифрой 1" +'\n'
                  "5.Пример карты лежит в папке с программой и назван 'example_field'" +'\n'
                  "6.Если вы все выполнили и поняли-нажмите 'Enter' и добро пожаловать в лабиринт =]")
        #Читам что нам там подарил юзер
        all_file = str(open('field').readlines())
        file_check(all_file)
        #Получим первую строку и потом из нее узнаем сколько в ней чисел
        input_value = open('field')
        first_string = input_value.readline().rstrip()
        total_elements_in_string = len(findall('(\d+)', first_string))
        M = total_elements_in_string + 2
        #Количество строк в файле
        N = len(open('field').readlines()) + 2
        #Переоткроем файл и начнем читать с первой строки
        input_value = open('field')
        field = buildin_field(total_elements_in_string, input_value)
        #Но это полдела.Надо конвертнуть
        xfield = convert_type_maze(field, N, M)
        #Покажем юзеру наше творение
        show_labirinth(N, M, xfield)

        print "Наш лабиринт!"
        sleep(2)
        #Получим координаты старта и финиша.
        S = argwhere(xfield == 2)[0]
        F = argwhere(xfield == 3)[0]
        #Затрем отметку старта(для лучшей визуализации и...
        xfield[S[0]][S[1]] = 0
        #Запустим поиск!
        x = promt('search')
        if x == 2:
            BFS(field, S, F, True)
        elif x == 1:
            DFS(S[0], S[1], xfield, S, F, N, M, False)

    except IOError:
        print "Проблемы с доступом к файлу." \
              "Проверьте наличие файла согласно инструкции или создайте его если такового не имеется" +   '\n'
    except IndexError:
        print "Упс.Кажется Вы ввели некоректные данные или забыли верно указать точку входа и выхода"




def buildin_field(total_elements_in_string, input_value):
    """Займемся сборкой игрового поля из того что нам подарил юзер"""
    #Новый список туда будем складывать все строки
    field = []
    string_field = []
    #И сразу же построим верхнюю стенку
    for x in xrange(total_elements_in_string + 2):
        string_field.append(-1)
    field.append(string_field)
    i = 1
    while i <= len(open('field').readlines()):
        string_content = input_value.readline().rstrip()
        #Немного движений ушами дабы преобразовать непустую строку в список
        if string_content != '':
            #Заморочка на юзабельность  и внешний вид
            # чтобы модифицировать единички в (-1)стенки
            string_content = sub('1', '-1', string_content)
            string_content = findall('(-*\d+)', string_content)
            #А потом все добавить в список который будет строкой-частью поля
            #И плюсом два элемента стенки по бокам
            #Тут интересная ситуевина с которой я немного поплясал.Если удалить все элементы из списка методом
            # del string_field[:] или подобным-почему то сразу же удаляется значение взятое из этого списка которое
            # мы когда то внесли в сборное игровое поле.Скорее всего просто мы удаляем значения а сборщик муссора
            # удаляет все из игрового поля.Так что вот только через новое присваивание.Жаль.Ниже пример в картинках
            #>>> a = [1]
            #>>> b = [a]
            #>>> b
            #[[1]]
            #>>> del a[:]
            #>>> b
            #[[]]
            #Позже заменено на взятии копии и инклюд ее в игровое поле))
            del string_field[:]
            string_field.append(-1)
            for x in string_content:
                  string_field.append(int(x))
            string_field.append(-1)
            field.append(string_field[:])
            i += 1
            #Как только выйдем из вайла-добавим нижнюю стенку.И вуаля-готов наш лабиринт))
    del string_field[:]
    for x in xrange(total_elements_in_string + 2):
        string_field.append(-1)
    field.append(string_field)
    return  field


def file_check(all_file):
#Если файл прочитался-не значит что он корректный.Отлавливаем всякие гадости и бросаем исключения
    all_numbers_in_files = findall('(-*\d+)', all_file)
    for x in all_numbers_in_files:
        if x != '0':
            if x != '1':
                if x != '2':
                    if x != '3':
                        raise ErrorFromUser.not_way(x)


def convert_type_maze(field, N, M):
    """Получим лабиринт из вложеных списков.Превратим его в лабиринт-массив из NumPy"""
    xfield = zeros((N, M), dtype=int)
    y = 0
    while y < N:
        xfield[y] = field[y]
        y += 1
    return xfield