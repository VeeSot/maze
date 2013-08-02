#encoding:utf-8
"""Алгоритм поиска в глубину.Рекурсия,стек вызовов,и не всегда самый оптимальный путь"""
from  processing_io import show_way
#Пару кортежей в качестве хранителей констант
i = (0, 0, -1, 1)
j = (-1, 1, 0, 0)
#Хранители пути
wayX = []
wayY = []
way = []
#Состояние найденности пути


def DFS(x, y, field, S, F, N, M, Find):
    c = 0
    #Начало пути же.Посему отметим его
    field[x, y] = -2
    while c < 4 and not Find:
        if  field[x + i[c], y + j[c]] == 3:
            field[x + i[c], y + j[c]] = -2
            #Соберем все данные в два списка(X,Y) добавив координаты старта и финиша,а потом-схлопнем в один список
            X = ['Y']
            Y = ['X']
            X.append(S[0])
            X = X + wayX
            X.append(F[0])
            Y.append(S[1])
            Y = Y + wayY
            Y.append(F[1])
            #Превращаем в один который пробросим его на печать дабы показать наш путь
            way.append(X)
            way.append(Y)
            #Мы нашли путь!!!
            Find = True
            show_way(way, field, N, M)
            return Find
        else:
            if field[x + i[c], y + j[c]] == 0:
                field[x + i[c], y + j[c]] = -2
                wayX.append(x + i[c])
                wayY.append(y + j[c])
                #Рекурсивно вызываем себя же и порождаем новые потоки
                DFS(x + i[c], y + j[c], field, S, F, N, M, False)

        c += 1