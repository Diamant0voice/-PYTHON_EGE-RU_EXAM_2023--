# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # yxwz
def columns(x, y, z, w):
    return ((x <= y) <= z) or (w <= (y and z))


for holes in product([0, 1], repeat=7):
    table = [(0, holes[0], holes[1], 0), (1, 0, holes[2], holes[3]), (holes[4], 1, holes[5], holes[6])]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xyzw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 876
for N in range(100, 1000): 
    dig1 = N // 100; dig2 = N // 10 % 10; dig3 = N % 10
    new = str(max(dig1 * dig2 * dig3, dig1 + dig2 + dig3)) + str(min(dig1 + dig2 + dig3, dig1 * dig2 * dig3))
    print(N) if new == "33621" else None

print("№6:")  # 2476
screensize(10000, 10000)
ht()
speed(10)
color("violet", "red")
tracer(0)
scale = 70
counter6 = 0
pensize(0.1)

begin_fill()
lt(90)
for rep in range(7):  # Заметим, что сторона и угол шибко мелкие для Δ, дальше база
    fd(31 * scale)
    rt(60)
end_fill()
up()
canvas = getcanvas()
for X in range(-260 * scale, 260 * scale, scale):
    for Y in range(-260 * scale, 260 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 3030260
@lru_cache(None)
def F(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 != 0:
        return 3 + F(n - 1) * F(n - 2) - F(n - 1) - F(n - 2)
    elif n > 1 and n % 2 == 0:
        return 2 * F(n - 1)
print(F(12))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("23:")  # 5411
func23 = lambda start, end: func23(start + 2, end) + func23(start + 10, end) if start < end else start == end
print(func23(5, 71))

print("№24:")  # 532

print("№25:")  # Ответ верный
def divs(number):
    s = set()
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            s.add(divider); s.add(number // divider)
    return sorted(s)

for number in range(799_999, 790_000, -1):
    d = divs(number)
    if len(d) > 0:
        M = max(d) - min(d)
        print(number, M) if M % 17 == 0 else None

print("№26:")  # 

print("№27:")  # 
