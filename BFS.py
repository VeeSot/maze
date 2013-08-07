# encoding:utf-8
"""Поиск в ширину.Работает медленее чем DFS,но несомненый плюс-
   кратчайщий путь в лабиринте(если путь существует)"""
from numpy import int, zeros
from processing_io import transfom_user_data, show_labirinth
import sys
# Пару кортежей в качестве хранителей констант
a = (0, 0, -1, 1)
b = (-1, 1, 0, 0)

# Хранители пути
way = [[], []]


def BFS(field, S, F, U=False):
    """Он же алгоритм Ли и волновой поиск.
       Входные данные-поле(field),начало(S),конец(F),
       U=False-User=False,по умолчанию считаем что лабиринт пришел не от юзера,
       а сгенерирован машиной"""
    # Cчетчик итераций
    iteration = 0
    # Размер в ширину-равен числу элементов в первом списке
    x = len(field[0])
    # В высоту-числу вложеных списков
    y = len(field)
    # Если лабиринт пришел от юзера-ковертнем его в более удобный вид
    if U:
        field = transfom_user_data(field, x, y)
        # У нас есть нормальный лабиринт(машина генерит с -1)
    # Точку старта обозначим как начало волны
    field[S[0]][S[1]] = 1
    # Точка финиша пусть тоже равна нулю.
    # У нас есть ее координаты и это уже неплохо.
    field[F[0]][F[1]] = 0

    # Перегрузим в массив NumPy
    xfield = zeros((y, x), dtype=int)
    c = 0
    while c < y:
        xfield[c] = field[c]
        c += 1
        # Максимально возможное число итераций.
        # Не более чем объем массива -1 ход.
    max_iteration = (x * y) - 1
    # Просматриваем массив-поле.Пока хватит иттераций
    # Количество проходок по всему лабиринту

    # Много вайло-итераций!!!!!
    while iteration < max_iteration and xfield[F[0]][F[1]] == 0:
        # На первой проходке мы найдем наш старт
        # (1 которая равна числу иттераций и начнем плясать от нее)
        iteration = iteration + 1
        i = 0
        while i < y:
            j = 0
            while j < x:
                if xfield[i][j] == iteration:
                    c = 0
                    while c < 4:
                        # Посмотрим округу
                        if xfield[i + a[c]][j + b[c]] == 0:
                            xfield[i + a[c]][j + b[c]] = iteration + 1
                        c += 1
                j += 1
            i += 1
        #Если волна дошла
    if xfield[F[0]][F[1]] != 0:
        return_way(F, S, xfield)
        return  way, xfield
    else:
        return None, field


def return_way(F, S, xfield):
# Хорошо.Начинаем отрисовку обратного пути.
# Для этого мы переместимся в точку выхода и поищем рядом с ней наименьшее
# значение которорое показывает за сколько шагов можно добраться до выхода.
    X = F[1]
    Y = F[0]
    # Пока не превратятся оба в нужные координаты-крутимся
    while not (X == S[1] and Y == S[0]):
        c = 0
        while c < 4:
            # Осмотримся.Если соседнее поле меньше на единицу-
            # прыгаем туда и плюс пишем все хранители пути
            if xfield[Y + b[c]][X + a[c]] == xfield[Y][X] - 1:
                if xfield[Y + b[c]][X + a[c]] != -1:
                    way[0].append(X + a[c])
                    way[1].append(Y + b[c])
                    # Пишем новые значения X и Y
                    X = X + a[c]
                    Y = Y + b[c]
            c = c + 1
        #Сборка списка и реверсы для гуаноидного восприятия
    way[0].reverse()
    way[1].reverse()
    way.reverse()
    way[0].insert(0, 'Y')
    way[1].insert(0, 'X')
    # Координаты старта обратного поиска и начало пути
    way[1].append(F[1])
    way[0].append(F[0])

    #Отметим тяжкий путь
    for element in xrange(len(way[0])):
        if type(way[0][element]) != str:
            xfield[way[0][element]][way[1][element]] = -2
        #Затрем все стороние числа которые не лежат на нашем пути.Нефиг вносить смуту
    y = 0
    while y<len(xfield):
        x = 0
        while x < len(xfield[0]):
            if xfield[y][x] != -2 and xfield[y][x] != -1:
                xfield[y][x] = 0
            x = x + 1
        y = y + 1


