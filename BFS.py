#encoding:utf-8
"""Поиск в ширину.Работает медленее чем DFS,но несомненый плюс-кратчайщий путь в лабиринте(если путь существует)"""
from numpy import int, zeros
from processing_io import transfom_user_data, show_labirinth
import sys
#Пару кортежей в качестве хранителей констант
a = (0, 0, -1, 1)
b = (-1, 1, 0, 0)
#Хранители пути
wayX = []
wayY = []


def BFS(field, S, F, U=False):
    """Он же алгоритм Ли и волновой поиск.Входные данные-поле(field),начало(S),конец(F)"""
    #Cчетчик итераций
    iteration = 0
    #Размер в ширину-равен числу элементов в первом списке
    x = len(field[0])
    #В высоту-числу вложеных списков
    y = len(field)
    #Если лабиринт пришел от юзера-ковертнем его в более удобный вид
    if U:
        field = transfom_user_data(field, x, y)
    #У нас есть нормальный лабиринт(машина генерит с -1)
    #Точку старта обозначим как начало волны
    field[S[0]][S[1]] = 1
    #Точка финиша пусть тоже равна нулю.У нас есть ее координаты и это уже неплохо.
    field[F[0]][F[1]] = 0

    #Перегрузим в массив NumPy
    xfield = zeros((y, x), dtype=int)
    c = 0
    while c < y:
        xfield[c] = field[c]
        c += 1
    #Максимально возможное число итераций.Не более чем объем массива -1 ход.
    max_iteration = (x * y) - 1
    #Просматриваем массив-поле.Пока хватит иттераций
    #Количество проходок по всему лабиринту

    #Много вайло-итераций!!!!!
    while iteration < max_iteration:
        #На первой проходке мы найдем наш старт(1 которая равна числу иттераций и начнем плясать от нее)
        iteration = iteration + 1
        i = 0
        while i < y:
            j = 0
            while j < x:
                if xfield[i][j] == iteration:
                    #Каунтер
                    c = 0
                    while c < 4:
                        #Посмотрим округу
                        if xfield[i + a[c]][j + b[c]] == 0:
                            xfield[i + a[c]][j + b[c]] = iteration + 1
                        c += 1
                j += 1
            i += 1
    if xfield[F[0]][F[1]] == 0:
        #Все печально.Пути в лабиринте нет
        print "К сожалению не существует пути между указаными вами точками"
    else:
        return_way(F, S, xfield, field, x, y)


def return_way(F, S, xfield, field, x, y):
#Хорошо.Начинаем отрисовку обратного пути для этого мы переместимся в точку выхода и поищем рядом
#  с ней наименьшее значение которорое показывает за сколько шагов можно добрать до выхода.
#Координаты старта обратного поиска и начало пути
    Y = F[0]
    X = F[1]
    wayX.append(X)
    wayY.append(Y)
    #Пока не превратятся оба в нужные координаты-крутимся
    while not (X == S[1] and Y == S[0]):
        c = 0
        while c < 4:
            #Осмотримся.Если соседнее поле меньше на единицу-прыгаем туда и плюс пишем все  хранители пути
            if xfield[Y + b[c]][X + a[c]] == xfield[Y][X] - 1 and xfield[Y + b[c]][X + a[c]] != -1:
                wayX.append(X + a[c])
                wayY.append(Y + b[c])
                #Пишем новые значения X и Y
                X = X + a[c]
                Y = Y + b[c]
            c = c + 1
            #Перевернем наши списки
    wayY.reverse()
    wayX.reverse()

    #Возьмем исходный массив field b и отрисуем на нем путь
    xfield = zeros((y, x), dtype=int)
    c = 0
    while c < y:
        xfield[c] = field[c]
        c += 1
    print "Мы сделали " + str(len(wayX)) + " шагов к нашей цели.Ниже они перечислены подробнее"

    sys.stdout.write("%3s" % 'X' + ' | ' + 'Y')
    print ' '
    for element in xrange(len(wayX)):
        xfield[wayY[element]][wayX[element]] = -2
        sys.stdout.write("%3s" % str(wayX[element]) + ' | ' + str(wayY[element]))
        print ' '

    show_labirinth(y, x, xfield)




