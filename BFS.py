# encoding:utf-8
"""Поиск в ширину.Работает медленее чем DFS,но несомненый плюс-
   кратчайший путь в лабиринте(если путь существует)"""
from config import tuple_x, tuple_y, way

def BFS(field, F, S):
    """Он же алгоритм Ли и волновой поиск.
       Входные данные-поле(field),начало(S),конец(F).
       В алгоритме мы подменим старт и финиш.Будем искать путь из конца в начало
       это даст некий выигрыш во времени впоследствии"""
    x = len(field[0])  # Размер в ширину-равен числу элементов в первом списке
    y = len(field)  # В высоту-числу вложеных списков
    field[S[0]][S[1]] = 1  # Точку старта обозначим как начало волны
    field[F[0]][F[1]] = 0  # Точка финиша пусть  равна нулю.
    from numpy import zeros
    xfield = zeros((y, x), dtype=int)  # заведем массив NumPy для последующей перегрузки в него
    c = 0
    while c < y:
        xfield[c] = field[c]
        c += 1
    iteration = 0   # Cчетчик итераций
    max_iteration = (x * y) - 1  # Максимально возможное число итераций.
    while iteration < max_iteration and xfield[F[0]][F[1]] == 0:  # Просматриваем массив-поле.Пока хватит иттераций
        iteration += 1
        i = 0
        while i < y:
            j = 0
            while j < x:
                if xfield[i][j] == iteration:
                    c = 0
                    while c < 4:
                        if xfield[i + tuple_x[c]][j + tuple_y[c]] == 0:  # Посмотрим округу
                            xfield[i + tuple_x[c]][j + tuple_y[c]] = iteration + 1
                        c += 1
                j += 1
            i += 1
    if xfield[F[0]][F[1]] != 0:  # Если волна дошла
        return_way(F, S, xfield)
        return way, xfield
    else:
        return None, field

def return_way(F, S, double_field):
    """ Начинаем отрисовку обратного пути.
     Для этого мы переместимся в точку выхода и поищем рядом с ней наименьшее
     значение которорое показывает за сколько шагов можно добраться до выхода"""
    way[1].extend(['Y', F[0]])  # шапка вывода & Координаты старта  пути
    way[0].extend(['X', F[1]])
    X = F[1]
    Y = F[0]
    while not (X == S[1] and Y == S[0]):  # Пока не превратятся оба в нужные координаты(конец пути)-крутимся
        c = 0
        while c < 4:
            if double_field[Y + tuple_y[c]][X + tuple_x[c]] == double_field[Y][X] - 1:  # Осмотримся.Если соседнее поле меньше на единицу-
                if double_field[Y + tuple_y[c]][X + tuple_x[c]] != -1:
                    way[0].append(X + tuple_x[c])  # прыгаем туда и плюс пишем путь в хранители
                    way[1].append(Y + tuple_y[c])
                    X = X + tuple_x[c]  # Пишем новые значения X и Y
                    Y = Y + tuple_y[c]
            c += 1
    way.reverse()  # реверс для смены  столбиков значений х и у местами
    for element in xrange(len(way[0])):  # Отметка пути на карте
        if type(way[0][element]) != str:
            double_field[way[0][element]][way[1][element]] = -2
    # Сотрем с карты все отметки кроме равных -2(Т.к "-2"-это наш путь)
    y = 0
    while y < len(double_field):  # Пока координата по высоте-меньше числа строчек в поле-матрице
        x = 0
        while x < len(double_field[0]):  # И координата по ширине-меньше количества столбиков
            if double_field[y][x] != -2 and double_field[y][x] != -1:
                double_field[y][x] = 0  # Перереписываем все несоответствующие значения нулями
            x += 1
        y += 1