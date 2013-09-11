#encoding:utf-8
"""Главная часть программы-поисковика пути.
   Пусть комментарии не смущают и не настораживают читающего сей текст"""
from numpy import int, zeros
from processing_io import wall_vertical, wall_horizontal, block_set, final_check,\
    hello_amigo, promt, promt_point_way, show_labirinth, show_way
from DFS import DFS
from BFS import BFS
from user_map import read_out_file
from config import width, height, way
# Простая вилка направленая на то  чтобы пользователь выбрал удобный ему путь.
# Автоматически генерируемый лабиринт или считаем лабиринт из файла
value = promt('method_input')
if value == 1:
    # Блок входных данных их обработки
    # Поприветствуем юзера
    # и попросим его задать размерность нашего будущего лабиринта.
    x, y = hello_amigo(height, width)
    # Мы запрашиваем у пользователя данные для одного лабиринта,
    # а строим чуток другой на 2 клеточки больше в ширину и в высоту,
    # потом мы эти излишки сыграют роль стен лабиринта
    M = x + 2
    N = y + 2
    # Игровое поле
    field = zeros((N, M), dtype=int)
    # Cтенки
    # Верхняя+Нижняя
    wall_horizontal(field, 0)
    wall_horizontal(field, N - 1)
    # Левая+Правая
    wall_vertical(field, 0, N)
    wall_vertical(field, M - 1, N)
    # Разбрасываем блоки в рандоме
    block_set(field, N, M)
    # Показываем пользователю лабиринт
    show_labirinth(N, M, field)
    while True:
        # Попросим ввести координаты начала пути в лабиринте
        # и подвергнем ряду проверок
        S = promt_point_way(field, N, M, 'начала')
        # Координаты конца
        F = promt_point_way(field, N, M, 'окончания')
        if S != F:
            field[F[0]][F[1]] = 3
            print 'Спасибо.Данные приняты.'
            break
        else:
            print 'Точка начала и окончания в лабиринте-совпадают.' \
                  'Введите корректные данные'
    # Вариант из двух случаев.
    # Один ответ направит на рекурсивный алгоритм поиска в глубину,
    # другой на поиск в ширину
    x = promt('search')
    if x == 2:
        Bway, Bfield = BFS(field, S, F)
        check = final_check(Bfield, F)
        if check:
            show_way(Bway)
            show_labirinth(N, M, Bfield)
    elif x == 1:
        from sys import setrecursionlimit
        setrecursionlimit(height*width)
        DFS(S[0], S[1], field, S, F, way)
        check = final_check(field, F)
        if check:
            show_way(way)
            show_labirinth(N, M, field)
elif value == 2:
    read_out_file(height, width)
raw_input('Для выхода  нажмите клавшу "Enter"')