#encoding:utf-8
"""Модуль отвечающий за processing_IO-обработку входных или выходных данных"""
from time import sleep
import sys
import random

def hello_amigo():
    """Мы же вежливые =] Салют пользователь-амиго"""
    while True:
        try:
            x,y= input("Введи через запятую размеры для нашего будущего лабиринта ."+'\n'
                                                                                     "Невыбирай очень большие числа,т.к восприятие лабиринта на экране будет искажено  " +'\n')
            if x<0 or y<0:
                print "Размеры не могут быть отрицательным числом '\n "
            elif type(x) == float  or type(y) ==float:
                print "Размеры не могут быть указаны нецелым числом '\n "
            elif x>100  or y>100 :
                print "Мы нерекомендуем использовать такие большие размеры из за внутрених ограничений программы '\n "
            elif type(x) == str  or type(y) == str:
                print "Размеры не могут быть указаны текстом \n "
            elif x > 0  and y > 0 and type(x) == int  and type(y) ==int:
                return x,y
        except TypeError:
            print "Упс.Кажется Вы ввели некоректные данные(например нецелое число)" +   '\n'
        except NameError:
            print "Упс.Кажется Вы ввели некоректные данные(например какую нибудь строку или набор букв)" +  '\n'
        except :
            print "Упс.Кажется Вы ввели некоректные данные." +  '\n'

def promt(x):
    """Обработка либо методов работы алгоритмов,либо решения о типе лабиринта"""
    while True:
        if x == 'method_input':
            argument = "Привет Амиго!!!Я предлагаю тебе выбор.Ты хочешь сгенерировать лабиринт автоматически?Если так то введи цифру 1.Иначе если ты хочешь загрузить лабиринт из файла-введи цифру 2" +'\n'
        elif x == 'search':
            argument = "Теперь выберем механизм поиска пути.1-Поиск в глубину(DFS) более быстрый но делает слишком много лишних шагов.2-Поиск в ширину(BFS)-Делает меньше шагов,всегда находит короткий путь,но более ресурсоемкий.1 или 2?" +'\n'
        try:
            value= input(argument)
            # Условности-эксепшены фильтрующие непотребство которое придет от нерадивого пользователя
            if value<0:
                print "Либо 1,либо 2.Никаких отрицательных чисел '\n "
            elif value>2:
                print "Введеные данные-неверны.Они не могут превышать 2 '\n "
            elif type(value) == float:
                print "Надо вводить целочисленые значения а не дробные(2.0 и 1.0-не принимаются) '\n "
            elif type(value) == str:
                print "Нужно ввести цифры а не текст \n "
            elif (value == 1 or value == 2) and len(str(value)) == 1:
                return value
        except TypeError:
            print "Упс.Кажется Вы ввели некоректные данные(например нецелое число)" +   '\n'
        except NameError:
            print "Упс.Кажется Вы ввели некоректные данные(например какую нибудь строку или набор букв)" +  '\n'
        except :
            print "Упс.Кажется Вы ввели некоректные данные." +  '\n'

def promt_point_way(field, N, M, point):
    """Запрос точек начала и конца пути для лабиринта при режиме автоматической генерации вышеупомянутого"""
    retry = 'Пожалуйста,будьте внимательнее и попробуйте снова.'  +  '\n' \
            'Введеные данные должны быть разделены запятой и являться положительными целыми числами'+'\n' \
            "Абцисса(горизонтальная координата) точки должна быть не более чем " + str(M-2) + " и не менее 0"+'\n' \
            "Ордината(вертикальная координата) точки должна быть не более чем " + str(N-2) + " и не менее 0" +'\n'
    while True:
        try:
            y,x = input("Введите через запятую координаты "+point+" пути   " +'\n')
            if x<0 or y<0:
                print"Координаты не могут быть отрицательным числом \n "  + retry
            elif x == 0 or y == 0 or x == M or y == N:
                print "Упс.Введены координаты указывающие на стену \n "  + retry
            elif x >= 1 and y >= 1  and field[x, y] != -1:
                P=[x, y]
                return P
            elif field[x, y] == -1:
                print "Упс.На указанных вами координатах находится непроходимый участок(блок) '\n'"  + retry
            elif type(x) == float  or type(y) ==float:
                print "Координаты не могут быть указаны нецелым числом '\n "
            elif type(x) ==str  or type(y) == str:
                print "Координаты  не могут быть указаны текстом \n "

        # Обработка эксепшенами от всякой ереси
        except TypeError:
            print "Упс.Кажется Вы ввели некоректные данные(например нецелое число)" +   '\n'  + retry
        except NameError:
            print "Упс.Кажется Вы ввели некоректные данные(например какую нибудь строку или набор букв)" +  '\n' + retry
        except IndexError:
            print "Ууу...слишком далеко за пределы карты действий" +  '\n' + retry
        except :
            print "Упс.Кажется Вы ввели некоректные данные." +  '\n' + retry

def show_way(way, field, N, M):
    """Покажем пользователю каким тяжким путем мы добрались"""
    print "Нам потребовалось "+str(len(way[0])-1)+" ходов,чтобы добраться до выхода"+'\n'+ \
          'Ниже перчислены наши шаги от точки входа до выхода'+'\n'
    for element in xrange(len(way[0])):
        sys.stdout.write("%4s" % str(way[1][element]) +' | '+ str(way[0][element]))
        print ' '
    print "А теперь посмотрим наш путь"+'\n'
    sleep(5)
    show_labirinth(N,M,field)

def final_message(field,F):
    """Если путь наш пуст-значит не дошли мы до точки"""
    if field[F[0]][F[1]] != -2:
        print "Между двумя указаными точками-нет пути"
    else:
        print "Поздравляю Амиго!Мы нашли путь =]"

def block_set(field, N, M):
    """Примитивнийший механизм генерации даже не лабиринта...блоков что создадут подобие лабиринта
       Возможно когда нибудь и перепишу"""
    i = 0
    # Число блоков не слишком большое иначе непроходимость возрастает.
    # А так..четверть всего доступного рабочего пространства
    b = N * M / 4
    while i <= b:
        x = random.randint(1, N - 2)
        y = random.randint(1, M - 2)
        i += 1
        field[x, y] = -1

def show_labirinth(N, M, field):
    """Отрисуем лабиринт и покажем его пользователю смешано с индексами для лучшей визуализации"""
    # Выведем строку для координат
    i = 0
    for element in xrange(M):
        sys.stdout.write("%2s" % number_for_wall(element) )
    print ' '
    y = 0
    while y < N:
        x = 0

        while x < M:
            sys.stdout.write("%2s" % str(transform_out(x,y,field)))
            x = x + 1
        sys.stdout.write(number_for_wall(i))
        i = i + 1
        print ' '
        y = y + 1
    for element in xrange(M):
        sys.stdout.write("%2s" % number_for_wall(element) )
    print ' '

def number_for_wall(number):
    """Если число которым мы хотим отрисовать номера стенок-
       не делится на десятку(не содержит в себе  только десятки)-вернем только хвост числа
       Таким образом боремся со смещением лабринта"""
    if number % 10 != 0:
        return str(number)[-1]
    else: return str(number)

def transform_out(y, x, field):
    """Трансформация в удобоваримый для пользвателя вид.Иначе с ума сойдет и запаникует от нулей,единичек и прочего"""
    if field[x,y] == - 1:
        return '#'
    elif field[x,y] == 0:
        return ' '
    elif field[x,y] == -2:
        return '+'
    else:
        return str(field[x,y])

def wall_horizont(field, row):
    """Добавим горизонатльные стенки для лабиринта"""
    i = 0
    for element in field[row]:
        field[row, i] = -1
        i += 1

def wall_verical(field, column, N):
    """Вертикальные стенки"""
    i = 0
    while i < N:
        field[i, column] = -1
        i += 1

def transfom_user_data(field, x, y):
    """Трансформируем юзверский лабиринт.Нам он отдаст лабиринт с 1.
       Мы же,обработаем и превратим в -1.Небольшая хитрость чтобы отрисовать
       понятный и читабельный путь впоследствии.А вообще эта функция-
       опциональная и нужна возможно только в DFS чтоб цифрами корректно показать путь.
       Ну и чтоб потом при выводе первый шаг не показало как непроходимый блок"""
    i = 0
    while i < y:
        j = 0
        while j < x:
            if field[i][j] == 1:
                field[i][j] = -1
            j = j + 1
        i = i + 1
    return field
