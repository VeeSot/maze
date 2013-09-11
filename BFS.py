# encoding:utf-8
"""Поиск в ширину.Работает медленее чем DFS,но несомненый плюс-
   кратчайщий путь в лабиринте(если путь существует)"""
from numpy import int, zeros
from config import tuple_x, tuple_y, way


def BFS(field, F, S):
    """Он же алгоритм Ли и волновой поиск.
       Входные данные-поле(field),начало(S),конец(F).
       В алгоритме мы подменим старт и финиш.Будем искать путь из конца в начало
       это даст некий выигрыш во времени впоследствии"""
    # Cчетчик итераций
    iteration = 0
    # Размер в ширину-равен числу элементов в первом списке
    x = len(field[0])
    # В высоту-числу вложеных списков
    y = len(field)
    # Если лабиринт пришел от юзера-ковертнем его в более удобный вид
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
    while iteration < max_iteration and xfield[F[0]][F[1]] == 0:
        iteration = iteration + 1
        i = 0
        while i < y:
            j = 0
            while j < x:
                if xfield[i][j] == iteration:
                    c = 0
                    while c < 4:
                        # Посмотрим округу
                        if xfield[i + tuple_x[c]][j + tuple_y[c]] == 0:
                            xfield[i + tuple_x[c]][j + tuple_y[c]] = iteration + 1
                        c += 1
                j += 1
            i += 1
            #Если волна дошла
    if xfield[F[0]][F[1]] != 0:
        return_way(F, S, xfield)
        return way, xfield
    else:
        return None, field


def return_way(F, S, xfield):
# Начинаем отрисовку обратного пути.
# Для этого мы переместимся в точку выхода и поищем рядом с ней наименьшее
# значение которорое показывает за сколько шагов можно добраться до выхода.
# Координаты старта  пути + шапка вывода
    way[1].append('Y')
    way[0].append('X')
    way[1].append(F[0])
    way[0].append(F[1])
    X = F[1]
    Y = F[0]
    # Пока не превратятся оба в нужные координаты(конец пути)-крутимся
    while not (X == S[1] and Y == S[0]):
        c = 0
        while c < 4:
            # Осмотримся.Если соседнее поле меньше на единицу-
            # прыгаем туда и плюс пишем путь в хранители
            if xfield[Y + tuple_y[c]][X + tuple_x[c]] == xfield[Y][X] - 1:
                if xfield[Y + tuple_y[c]][X + tuple_x[c]] != -1:
                    way[0].append(X + tuple_x[c])
                    way[1].append(Y + tuple_y[c])
                    # Пишем новые значения X и Y
                    X = X + tuple_x[c]
                    Y = Y + tuple_y[c]
            c = c + 1
        # реверс для смены  столбиков значений х и у местами
    way.reverse()
    # Отрисовка пути
    for element in xrange(len(way[0])):
        if type(way[0][element]) != str:
            xfield[way[0][element]][way[1][element]] = -2
    # Сотрем с карты все отметки кроме равных -2(Т.к "-2"-это наш путь)
    y = 0
    #Пока координата по высоте-меньше числа строчек в поле-матрице
    while y < len(xfield):
        x = 0
        # И координата по ширине-меньше количества столбиков
        while x < len(xfield[0]):
            if xfield[y][x] != -2 and xfield[y][x] != -1:
                #Перереписываем все несоответствующие значения нулями
                xfield[y][x] = 0
            x = x + 1
        y = y + 1