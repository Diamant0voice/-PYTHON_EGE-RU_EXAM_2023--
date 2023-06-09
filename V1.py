# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

# Привет. Ниже представлены ВСЕ использованные за 20 вариантов библиотеки\модули, вам понадобится поменьше)
# Всё нестандартное прокоментировано. Удачной подготовки!
  
import string # Вставка модуля целиком - плохая идея, грузим память + писать больше, а это критично
import math
from turtle import *  # Пулл имеющихся только в коде функций, а не всей библиотеки, уже лучше
from itertools import product, permutations, groupby
from functools import lru_cache as lru # Оптимальный вариант, хватаем что надо и укорачиваем под себя
from sys import getrecursionlimit, setrecursionlimit

print('№2:')  # Ответ: xzyw
def columns(x, y, z, w):  # Букавы из условия (регистр одинаков на всю задачу!)
    return x and (y <= z) and ((not y) <= ((not z) == w))  # Само логическое выражение


for holes in product([0, 1], repeat=5):  # Перебор для имеющегося в таблице кол-ва дырок, вместо лесенок из for'ов
    table = [(holes[0], holes[1], 0, 0), (holes[2], 0, 0, holes[3]), (1, holes[4], 1, 1)]; F = [1, 1, 0]  # Всё по спискам, но строки в кортежи
    if len(table) == len(set(table)):  # Брокер дубликатов из-за специфики решения
        for answer2 in permutations('xyzw'):  # Перебор расстановок для проверки соответсвия имён столбцов и значений их итогам,
            if [columns(**dict(zip(answer2, variation))) for variation in table] == F:  # Принимая распаковку словаря из различных вариантов пар
                print(*answer2, sep='')  # Готовый для копипаста ответ (распакованным в строку списком без пробелов)
# Рекомендую изучить все возможности астериска (*) отдельно, станет комфортнее

print('№5:')  # Ответ: 9
for N in range(1, 50):  # Рассматриваем разные нат. числа, обычно их немного
    R = bin(N)[2:]  # Строим их двоичную запись, срезав указатель сс
    R += '0' if N % 2 == 0 else '1'  # Шаг 2 через тернарку (do ... if True else don't ...)
    R = R.replace(R[:2], '11', 1) if R.count('1') % 3 == 0 else R.replace(R[:2], '10', 1)  # По аналогии
    if int(R, 2) >= 26:  # Ограничение из условия
        print(N, ', а новое такое:', int(R, 2))  # Ради интереса выводим и N, и R
        break  # Для остановки проги, ведь нужно наименьшее

print('№6:')  # Ответ: 625
# БЛОК ПАРАМЕТРОВ (для ускорения программы):
screensize(10000, 10000)  # Размер выпадающего окна
speed(10)  # Ускоряем отрисовку в целом
tracer(0)  # Ускоряем блок путём остановки анимаций
shape("turtle") # Делаем черепаху "черепахой", чтобы видеть её конечное положение
color("orange", "red")  # Цвет контура и цвет заливки. colorID красного - 5, важно для блока счёта
scale = 55  # Ваша константа масштаба для увеличения микрокартинки
counter6 = 0  # Счётчик точек для ответа

# БЛОК РИСОВАНИЯ (дословно переносим алгоритм из усл., но с нюансами):
up() # Поднимаем изначально готовый хвост
left(90)  # ВАЖНО, ибо черепаха Python смотрит вправо (OX+), а Кумир'овская, стандарт, в небо (OY+)
forward(100 * scale) # Вперёд в масштабе
right(90) # Угол поворота в градусах
forward(100 * scale)
right(30)
down()
begin_fill()  # Как только хвост опущен, включаем заливку
for repeat in range(4):  # !!!СНАЧАЛА АНАЛИЗ ФИГУРЫ!!! ПОТОМ ПОВТОРЫ СТАВИМ ОСОЗНАННО, ИНАЧЕ ТОЧЕК БОЛЬШЕ!
    forward(25 * scale)  
    right(90)
end_fill()
up() # Поднимаем хвост, чтобы не считать точку выхода. Фигура готова!

# БЛОК СЧЁТА (находим целочисленные точки):
canvas = getcanvas()  # Делаем картинку (холст) итерируемым объектом
for X in range(-550 * scale, 550 * scale, scale):  # Бо́льшим фигуры диапазоном проходим сетку Декартовой СК, в масштабе
    for Y in range(-550 *  scale, 550 * scale, scale):
        scanner = canvas.find_overlapping(X, Y, X, Y)  # Дискретизируем фигуру из условия пиксельными квадратами
        if len(scanner) == 1 and scanner[0] == 5: # Если наши квадраты размером с сами точки и имеют цвет заливки, а не конутра - "ура"!
            counter6 += 1  # len == 1 как флажок, ВСЕГДА НАДО; [0] == 5 - факт "ненахождения" на границах, доп. усл.

# БЛОК ВЫХОДА:
print(counter6)
update()  # Обновление кадра, чтобы увидеть итог
exitonclick()  # Выход по нажатию, чтобы окно не сворачивалось. В среднем 5-6 минут на перепечатывание и уходит, не прикопаешься, тьфу

print('№7:')  # Ответ: 4
file_size = 512 * 750; file_compr_kbyte = 80; file_compr_ratio = 100
file_orig_ratio = 100 + 65; file_orig_kbyte = (file_orig_ratio * file_compr_kbyte) / file_compr_ratio
file_orig_bit = file_orig_kbyte * 1 * 8 * 1024  # * 2**13 
i = math.floor(file_orig_bit / file_size)  # Округление в меньшую сторону, чтобы после уменьшения величины объёма хватило
print(2**i)  # i - лишь глубина кодирования, степень двойки

print('№8:')  # Ответ: 612
counter = 0
for digits in product('01234567', repeat=5):  # Перебираем цифры 5 раз и сохраняем их в строку
    number = ''.join(digits)  # All(...) возвращает bool, и нам нужна правда; {} - безповторное множество вариантов (защита от приколов)
    if number.count('4') == 2 and number[0] != '0' and all(number.count(fail) == 0 for fail in {'14', '34', '54', '74', '41', '43', '45', '47'}):
        counter += 1  # Считаем кол-во подошедших по условию
print(counter)

print('№9:')  # Ответ: 1
# Открываем файл. Если условие - кукож, то нажимаем F12, сохраняем в .txt с табуляцией (.csv тоже подойдёт)
counter = 0  # Счётчик кол-ва строк, удовлетворяющих требованию
with open('z9_v1-4.txt', "r") as file9:  # Так файл САМ закроется и после выполнения и освободит память
    for string_excel in file9.readlines():  # Или sorted(int(number9) for number9 in string_excel.split())
        list9 = sorted(map(int, string_excel.split()))  # Генерируем упорядоченный по возрастанию числовой список
        if (list9[3]*2 < (list9[2] + list9[1] + list9[0])) and ((list9[3] + list9[2] == list9[1] + list9[0])
           or ((list9[3] + list9[1] == list9[2] + list9[0]) or (list9[3] + list9[0] == list9[2] + list9[1]))):
            counter += 1
            print(counter, ', а сама строка такая:', *list9)

print('ТИП №11:')  # Ответ: 2800
alp, length, users = 500 + 10, 711, 3584  # Краткая форма инициализации переменных, быстро, но стрёмно
pass_byte_size = math.ceil((math.ceil(math.log2(alp)) * length) / 8)  # По формуле Хартли берём i, и округляем наверх, раз повышаем разряд
all_pass = (pass_byte_size * users) / 1024
print(int(all_pass))

print('ТИП №12:')  # Ответ: 121222
string = '22' + '1' * 2023 + '22'
while '211' in string or '112' in string: # ОЧЕНЬ важно именно приравнивать строку новому результату, и делать по одной замене зараз
    string = string.replace('11', '1', 1); string = string.replace('21', '12', 1) if '21' in string else string.replace('12', '1', 1)
print(string)

print('ТИП №14:')  # Ответ: 3028
cringe, counter = 4 * 25**2022 - 2 * 5**2000 + 125**1011 - 3 * 5**100 - 660, 0  # Решение "безфункционнное", easy, но не универсально
while cringe > 0:
    if cringe % 5 == 4:
       counter += 1  # Или counter = counter + 1
    cringe //= 5  # Дополненные операторы присваивания, по секрету, не одной арифметикой хороши
print(counter)

print('ТИП №15:')  # Ответ: 227
for A in range(1, 1000):  # Классическое решение (через флажковый метод):
    flag = True  # или 1
    for x in range(1, 2000):  # Иксов всегда перебираем побольше параметра
        logic = ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500)
        if logic == 0:
            flag = False  # или 0
            break  # Если что-то не сходится, то обнуляем и тормозим
    if flag == True:  # Ну а если всё без изменений, то победа
        print(A)
        break  # Стоп, т. к. ищем наименьшее

print('ТИП №16:')  # Ответ: 530
@lru(None)  # Это - декоратор, влияет на функцию, не меняя её. Данный - ускоряет работу, запоминая результаты
def F(n):
    if n < 3:
        return n
    elif n > 2 and n % 2 == 0:  # Обязательно elif'ами, иначе минус балл
        return 2 * (n - 1) + F(n - 1) + 2
    elif n > 2 and n % 2 != 0:
        return 2 * (n + 1) + F(n - 2) - 5
print(F(32))

print('ТИП №17:')  # Ответ: 2 9997800125
counter = squares_sum = 0
with open('17var01.txt', "r") as file17:
    f = [int(num) for num in file17]  # Генератор списков. Этот все числа в файле перегоняет в список
    maximum = max(f)  # Ищем наибольшее число
    for number, number_next in zip(f, f[1:]):  # Инициализируем по паре чисел из списка (для троек - f[2:])
        if number + number_next == maximum:
            counter += 1
            squares_sum = max(squares_sum, number ** 2 + number_next ** 2)  # Перезапишем значение, если поступившее больше последнего
print(counter, squares_sum)

print('№19:')  # Ответ: 114
def heap19(rocks1, positions):
    if rocks1 >= 229 or positions > 3:  # Условия завершения игры
        return positions == 3
    if positions % 2 == 0:  # Мы на 1-ой позиции, дальше будет 2-ая, чётная, на них и смотрим
        return heap19(rocks1 + 1, positions + 1) or heap19(rocks1 * 2, positions + 1)
    else:  # Если есть "ПРИ ЛЮБОМ ХОДЕ ПЕРВОГО ВТОРОЙ МОЖЕТ ВЫИГРАТЬ ЗА 1 ХОД", то учитываем И чужие ходы
        return heap19(rocks1 + 1, positions + 1) and heap19(rocks1 * 2, positions + 1)


for answer19 in range(1, 228 + 1):  # Перебираем возможное кол-во камней в куче
    print(answer19) if heap19(answer19, 1) else None  # Начиная с первой позиции, начальной

print('№20:')  # Ответ: 57 113
def heap20(rocks1, positions):
    if rocks1 >= 229 or positions > 4:
        return positions == 4
    if positions % 2 != 0:  # Здесь нужна нечётная, 3-я позиция
        return heap20(rocks1 + 1, positions + 1) or heap20(rocks1 * 2, positions + 1)
    else:
        return heap20(rocks1 + 1, positions + 1) and heap20(rocks1 * 2, positions + 1)


for answer20 in range(1, 228 + 1):
    print(answer20) if heap20(answer20, 1) else None

print('№21:')  # Ответ: 112
def heap21(rocks1, positions):
    if rocks1 >= 229 or positions > 5:
        return positions == 3 or positions == 5  # Костыль, ибо без позиции 3 позиция 5 не существует
    if positions % 2 == 0:
        return heap21(rocks1 + 1, positions + 1) or heap21(rocks1 * 2, positions + 1)
    else:
        return heap21(rocks1 + 1, positions + 1) and heap21(rocks1 * 2, positions + 1)


for answer21 in range(1, 228 + 1):  # Выбираем ТО число, которого прежде НЕ видели
    print(answer21) if heap21(answer21, 1) else None

print('№23:')  # Ответ: 2340
func23 = lambda start, end: func23(start - 1, end) + func23(start // 2, end) if start > end else start == end
print(func23(50, 20) * func23(20, 1))  # Для удобства - анонимная (она же лямбда) функция в тернарке, но принцип из №19-21

print('№24:')  # Ответ: 501
with open('24var01.txt', "r") as file24:
    f = file24.read().strip() # Читаем весь файл, скрыв возможные пробелы в начале и в конце
    symb1, symb2, symb3 = 1, 2, 3  # Нам нужно 3 символа подряд
    max_len = cur_len = 3  # ЗАРАНЕЕ открыв файл, видим, что уже первые 3 удовл. усл., cразу их учтём
    for index in range(3, len(f)):  # Нумеруем все символы (минуя учтённые)
        if f[index] == 'A':
            cur_len = index - symb1  # Отбрасываем самую старую "А", соблюдая усл. 'cur_len <= 3'
            max_len = max(max_len, cur_len)  # Будем фиксировать новую длину, если она больше последней
            symb1, symb2, symb3 = symb2, symb3, index  # Сдвигаем наш поисковик
        else:
            cur_len += 1  # Захватываем следующий символ для рассмотрения
            max_len = max(cur_len, max_len)  # Подстраховка
print(max_len)

print('№25:')  # Ответ верный
for length in range(4):  # если вставок цифр будет больше 4, то число превысит 9 символов (10**0 = 1 символ, 10**1 = 2, 10**2 = 3...)
    for asterisk in product('0123456789', repeat=length):  # Экспериментируем с подстановкой
        mask = int(f"11{''.join(asterisk)}223")  # Маска через f-строку, форматируем как senior'ы
        print(mask, mask // 149) if mask % 149 == 0 else None
