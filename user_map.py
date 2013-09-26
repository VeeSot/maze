# encoding:utf-8
"""Обработка пользовательской карты"""
from processing_io import show_labirinth
from re import findall
from config import way, height, width

#Блок исключений
class UserExceptions(Exception):
    """Класс для обработки человеческих ошибок"""

    def __init__(self):
        self.data = None

    def set_value(self, value):  # Получение входных параметров
        self.data = value

    def many_io(self):  # Блок избыточных точек входа или выход
        point = 'выход'
        if self.data[0] == '2':
            point = 'вход'
        print "В вашей карте более одного " + point + "а.Исправьте входные данные" + '\n'
        raise Exception

    def incorrect_size(self):  # Блок неверных размеров лабиринта
        size = str(width)
        if self.data == 'высоту':
            size = str(height)
        print "Размеры лабиринта" + " в " + self.data + "больше допустимых " + size + " клеточек" + '\n'
        raise Exception

    def not_correct_value(self):   # Случай когда пользователь использует в лабиринте постороние цифры
        print "В карте лабиринта обнаружено число " + self.data + "которое не удволетворяет требованиям программы" + '\n'
        raise Exception

    def not_equal_len(self):  # Строки разной длины
        print "В вашей карте имеются строки разной длины.(строка # " + str(self.data) + ")" + '\n'
        raise Exception

def create_exception(data):
    exception = UserExceptions()
    exception.set_value(data)
    print  # Вставка для того чтобы отделить визуально причину внештатной ситуации
    return exception

# Чтение и сборка
def read_out_file(height, width):
    # Попытка получить файл на диске
    try:
        raw_input('''Уважаемый пользователь.ниже написана небольшая инструкция
После ее прочтения и выполнения - нажмите клавишу "Enter"
1.Карта должна лежать в одной папке с исполняемой программой(скриптом)
2.Файл с картой должен иметь имя "field".Без кавычек
3.Файл с картой должен представлять из себя матрицу чисел,в которой могут и долны встречаться числа 0, 1, 2, 3
4.Начало пути отмечается цифрой "2". Окончание - цифрой "3".Проходимые участки - цифрой "0". Непроходимые - цифрой "1"
5.Пример карты лежит в папке с программой и назван "example_field"
6.Если вы все поняли и выполнили - нажмите 'Enter' и добро пожаловать в лабиринт''')
        all_file = str(open('field').readlines())  # Читам что нам там подарил пользователь
        first_string = all_file[:all_file.find('\\n')]  # Первая строка до переноса каретки
        total_elements_in_string = len(findall('(\d+)', first_string))  # Получим первую строку и потом из нее узнаем сколько в ней чисел
        number_string_in_file = len(open('field').readlines())  # Количество строк в файле
        file_check(all_file)
        size_maze(total_elements_in_string, number_string_in_file)  # Проверка размеров лабиринта
        M = total_elements_in_string + 2
        N = number_string_in_file + 2
        field = building_field(total_elements_in_string, open('field'))  # Постройка лабиринта из файла с картой
        xfield = convert_type_maze(field, N, M)  # Но это полдела.Надо конвертнуть
        show_labirinth(N, M, xfield)  # Покажем лабиринт
        print "Наш лабиринт!"
        from time import sleep
        sleep(2)  # Пауза чтоб рассмотреть
        from numpy import argwhere
        S = argwhere(xfield == 2)[0]  # Получим координаты старта
        F = argwhere(xfield == 3)[0]  # и финиша.
        xfield[S[0]][S[1]] = 0  # Затрем отметку старта(для лучшей визуализации)
        from processing_io import promt, final_check,show_way
        x = promt('search')
        if x == 2:  # Вилка на выбор варианта алгоритмы
            from BFS import BFS
            Bway,Bfield = BFS(field, S, F)
            check = final_check(Bfield, F)
            if check:
                show_way(Bway)
                show_labirinth(N, M, Bfield)
        elif x == 1:
            from DFS import DFS # Подгружаем алгоритм
            from sys import setrecursionlimit  # Установка рекурсии именно на этом шаге,
            setrecursionlimit(height*width)  # т.к не факт что пользователь выберет этот путь
            DFS(S[0], S[1], field, S, F, way)
            check = final_check(field, F)
            if check:
                show_way(way)
                show_labirinth(N, M, field)
    except IOError:
        print "Проблемы с доступом к файлу.Проверьте наличие файла согласно инструкции или создайте его если такового не имеется" +   '\n'
    except IndexError:
        print "возможно вы не указали точку начала или окончания пути"


def convert_type_maze(field, N, M):
    """Получим лабиринт из вложеных списков.
       Превратим его в лабиринт-массив из NumPy"""
    from numpy import zeros
    second_field = zeros((N, M), dtype=int)
    y = 0
    while y < N:
        second_field[y] = field[y]
        y += 1
    return second_field

def building_field(total_elements_in_string, input_value):
    """Займемся сборкой игрового поля из того что нам подарил пользователь"""
    from re import sub
    field = []# Новый список туда будем складывать все строки
    string_field = []
    # И сразу же построим верхнюю стенку
    for x in xrange(total_elements_in_string + 2):
        string_field.append(-1)
    field.append(string_field)
    i = 1
    while i <= len(open('field').readlines()):
        string_content = input_value.readline().strip()
        if string_content != '':# Немного движений  дабы преобразовать непустую строку в список
            string_content = sub('1', '-1', string_content)# чтобы модифицировать единички в (-1)стенки
            string_content = findall('(-*\d+)', string_content)# Число цифр в строке.
            if len(string_content) != total_elements_in_string:# Контролируем дабы не было лабиринта со строками разного уровня
                exception = create_exception(i)
                exception.not_equal_len()
                # А потом все добавить в список который будет строкой-частью поля
            # И плюсом два элемента стенки по бокам
            del string_field[:]
            string_field.append(-1)
            for x in string_content:
                string_field.append(int(x))
            string_field.append(-1)
            field.append(string_field[:])
            i += 1
            # Как только выйдем из цикла-добавим нижнюю стенку.
    del string_field[:]
    for x in xrange(total_elements_in_string + 2):
        string_field.append(-1)
    field.append(string_field)
    return field

# Проверки
def file_check(all_file):
    # проверка наличия постороних цифр
    all_numbers_in_files = findall('(-*\d+)', all_file)
    for x in all_numbers_in_files:
        if x != '0' and x != '1' and x != '2' and x != '3':
            exception = create_exception(x)
            exception.not_correct_value()
    two = []
    three = []
    for x in all_numbers_in_files:
        if x == '2':
            two.append(x)
        elif x == '3':
            three.append(x)
    if len(two) > 1:
        exception = create_exception(two)
        exception.many_io()
    elif len(three) > 1:
        exception = create_exception(three)
        exception.many_io()

def size_maze(total_elements_in_string, number_string_in_file):
    if total_elements_in_string > width:
            exception = create_exception('ширину')
            exception.incorrect_size()
    elif number_string_in_file > height:
            exception = create_exception('высоту')
            exception.incorrect_size()