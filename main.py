#encoding:utf-8
"""Главная часть программы-поисковика пути.
   Пусть комментарии не смущают и не настораживают читающего сей текст"""
from numpy import int, zeros
from processing_io import *
from DFS import *
from BFS import *
from user_map import read_out_file
# Поднимем рекурсию дабы разершить уровень 100 на 100 клеточек
sys.setrecursionlimit(5000)
# Хранитель пути
way = [['Y'], ['X']]
# Простая вилка направленая на то  чтобы пользователь выбрал удобный ему путь.
# Автоматически генерируемый лабиринт или считаем лабиринт из файла
value = promt('method_input')
if value == 1:
    # Блок входных данных их обработки
    # Поприветствуем юзера
    # и попросим его задать размерность нашего будущего лабиринта.
    x, y = hello_amigo()
    # Тут небольшой финт ушами,
    # мы запрашиваем у пользователя данные для одного лабиринта,
    # а строим чуток другой на 2 клеточки больше в ширину и в высоту,
    # потом мы эти излишки пустим на стены лабиринта
    M = x + 2
    N = y + 2
    # Игровое поле
    field = zeros((N, M), dtype=int)
    # Блок подготовки карты и показывание ее
    # Cтенки
    # Верхняя+Нижняя
    wall_horizont(field, 0)
    wall_horizont(field, N - 1)
    # Левая+Правая
    wall_verical(field, 0, N)
    wall_verical(field, M - 1, N)
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
    # Тут будет кейс из двух случаев.
    # Один направит на рекурсивный алгоритм поиска в глубину,
    # другой на поиск в ширину
    x = promt('search')
    if x == 2:
        Bway, Bfield = BFS(field, S, F)
        check = final_check(Bfield, F)
        if check:
            show_way(Bway)
            show_labirinth(N, M, Bfield)
    elif x == 1:
        DFS(S[0], S[1], field, S, F, way)
        check = final_check(field, F)
        if check:
            show_way(way)
            show_labirinth(N, M, field)
elif value == 2:
    read_out_file()
raw_input('Для выхода из программы нажмите клавшу "Enter"')