# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # wxzy
def columns(x, y, z, w):
    return not(x  <= y) or (x == z) or w


for holes in product([0, 1], repeat=6):
    table = [(holes[0], holes[1], 1, 1), (0, 1, holes[2], 1), (holes[3], holes[4], 1, holes[5])]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xyzw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  #
for N in range(1, 100):
    N = bin(N)[2:]
    N = N.replace('0', 'a').replace('1', 'b')
    N = N.replace('a', '01').replace('b', '10')
    if int(N, 2) > 63:
        print(int(N, 2))
        break

print("№6:")  # 153
screensize(4000, 4000)
speed(10)
shape("turtle")
tracer(0)
color("blue", "red")
pensize(0.1)
scale = 50
counter6 = 0

begin_fill()
lt(180)
circle(-4 * scale, 180)
lt(90)
circle(-4 * scale, 180)
lt(90)
circle(-4 * scale, 180)
lt(90)
circle(-4 * scale, 180)
end_fill()
up()

canvas = getcanvas()
for X in range(-300 * scale, 300 * scale, scale):
    for Y in range(-300 * scale, 300 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№12:")  # 
for n in range(1, 10):
    string = '>' + '0' * 15 + '1' * n + '2' * 15
    while '>0' in string or '>1' in string or '>2' in string:
        string = string.replace('>0', '22>', 1) if '>0' in string else string
        string = string.replace('>1', '2>', 1) if '>1' in string else string
        string = string.replace('>2', '1>', 1) if '>2' in string else string
    if (string.count('2') + string.count('1')) % 2 != 0 and (string.count('2') + string.count('1')) % 3 != 0:
        print(n)  # перебор НЕ корректен, есть другие делители, но писать их перебор кукож, лучше поскладывать
        break

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 16345854
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n ** 2 + F(n - 1)

for n in range(2, 1_000_000):  # Числа можно записывать с разделителем разрядов, если они велики
    F(n)  # Уходить за 1024 Мб рекурсии нельзя, хитро ограничиваем её
print(F(2023) - F(2019))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 40
func23 = lambda start, end: func23(start + 1, end) + func23(start + 3, end) + func23(start * 2, end) if start < end else start == end
print(func23(2, 6) * func23(6, 9) * func23(9, 14))

print("№24:")  # 

print("№25:")  #
