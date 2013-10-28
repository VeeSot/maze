#encoding:utf-8
"""Главная часть программы-поисковика пути."""
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
    x, y = hello_amigo(height, width)    # Поприветствуем пользователя и попросим его задать размерность нашего будущего лабиринта
    # Мы запрашиваем у пользователя данные для одного лабиринта,
    M = x + 2   # строим чуток другой на 2 клеточки больше в ширину и в высоту,
    N = y + 2   # потом мы эти излишки сыграют роль стен лабиринта
    field = zeros((N, M), dtype=int)   # Игровое поле
    # Cтенки
    wall_horizontal(field, 0)   # Верхняя+Нижняя
    wall_horizontal(field, N - 1)
    wall_vertical(field, 0, N)   # Левая+Правая
    wall_vertical(field, M - 1, N)
    block_set(field, N, M)  # Разбрасываем блоки в рандоме
    show_labirinth(N, M, field)  # Показываем пользователю лабиринт
    while True:
        S = promt_point_way(field, N, M, 'начала')  # Попросим ввести координаты начала пути в лабиринте
        F = promt_point_way(field, N, M, 'окончания')   # Координаты конца
        if S != F:
            field[F[0]][F[1]] = 3
            print 'Спасибо.Данные приняты.'
            break
        else:
            print 'Точка начала и окончания в лабиринте-совпадают.Введите корректные данные'
    x = promt('search')  # Вариант из двух алгоритмов поиска
    if x == 2:
        B_way, B_field = BFS(field, S, F)  # на поиск в ширину
        check = final_check(B_field, F)
        if check:
            show_way(B_way)
            show_labirinth(N, M, B_field)
    elif x == 1:
        from sys import setrecursionlimit
        setrecursionlimit(height * width)
        DFS(S[0], S[1], field, S, F, way)  # на рекурсивный алгоритм поиска в глубину,
        check = final_check(field, F)
        if check:
            show_way(way)
            show_labirinth(N, M, field)
elif value == 2:
    read_out_file(height, width)
raw_input('Для выхода  нажмите клавшу "Enter"')