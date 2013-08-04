# encoding:utf-8
"""Алгоритм поиска в глубину.
Рекурсия,стек вызовов,и не всегда самый оптимальный путь"""
# Пару кортежей в качестве хранителей констант
i = (0, 0, -1, 1)
j = (-1, 1, 0, 0)


def DFS(x, y, field, S, F, way):
    c = 0
    # Начало пути же.Посему отметим его
    field[x][y] = -2
    while c < 4 and not field[F[0]][F[1]] == -2:
        if  field[x + i[c]][y + j[c]] == 3:
            field[x + i[c]][y + j[c]] = -2
            #Прикрутим заголовок и начало пути
            way[0].insert(1, S[0])
            way[1].insert(1, S[1])
            #Добавим координаты завершения
            way[0].append(F[0])
            way[1].append(F[1])
        else:
            if field[x + i[c]][y + j[c]] == 0:
                field[x + i[c]][y + j[c]] = -2
                way[0].append(x + i[c])
                way[1].append(y + j[c])
                # Рекурсивно вызываем себя же и порождаем новые потоки
                DFS(x + i[c], y + j[c], field, S, F, way)
        c += 1