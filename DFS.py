# encoding:utf-8
"""Алгоритм поиска в глубину.
Рекурсия,стек вызовов,и не всегда самый оптимальный путь"""
from config import tuple_x, tuple_y


def DFS(x, y, field, S, F, way):
    # Пришли в новую точку.Отметим как посещеную
    field[x][y] = -2
    #Счетчик итераций
    c = 0
    # Смотрим по сторонам четыре раза
    # и если точка не имеет знак что мы в ней побывали-идем туда
    while c < 4 and field[F[0]][F[1]] != -2:
        if field[x + tuple_x[c]][y + tuple_y[c]] == 0:
            field[x + tuple_x[c]][y + tuple_y[c]] = -2
            way[0].append(x + tuple_x[c])
            way[1].append(y + tuple_y[c])
            # Рекурсивно вызываем себя же и порождаем новые потоки
            DFS(x + tuple_x[c], y + tuple_y[c], field, S, F, way)
        elif field[x + tuple_x[c]][y + tuple_y[c]] == 3:
            #Значит мы таки пришли к точке выхода.Отметим ее как посещеную
            field[x + tuple_x[c]][y + tuple_y[c]] = -2
            #Прикрутим заголовок и начало пути
            way[0].insert(0, 'Y')
            way[1].insert(0, 'X')
            way[0].insert(1, S[0])
            way[1].insert(1, S[1])
            #Добавим координаты завершения
            way[0].append(F[0])
            way[1].append(F[1])
        c += 1
