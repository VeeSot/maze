# encoding:utf-8
"""Алгоритм поиска в глубину.
Рекурсия,стек вызовов,и не всегда самый оптимальный путь"""
from config import tuple_x, tuple_y

def DFS(x, y, field, S, F, way):
    field[x][y] = -2  # Пришли в новую точку.Отметим как посещеную
    c = 0  # Счетчик итераций
    while c < 4 and field[F[0]][F[1]] != -2:  # Смотрим по сторонам четыре раза
        if field[x + tuple_x[c]][y + tuple_y[c]] == 0:   # и если точка не имеет знак что мы в ней побывали
            way[0].append(x + tuple_x[c])
            way[1].append(y + tuple_y[c])
            DFS(x + tuple_x[c], y + tuple_y[c], field, S, F, way)  # Рекурсивно вызываем себя же и порождаем новые потоки
        elif field[x + tuple_x[c]][y + tuple_y[c]] == 3:  # Значит мы таки пришли к точке выхода.
            field[x + tuple_x[c]][y + tuple_y[c]] = -2  # Отметим ее как посещеную
            way[0].insert(0, 'Y')  # Прикрутим заголовок
            way[1].insert(0, 'X')
            way[0].insert(1, S[0])  # и начало пути
            way[1].insert(1, S[1])
            way[0].append(F[0])  # Добавим координаты завершения
            way[1].append(F[1])
        c += 1