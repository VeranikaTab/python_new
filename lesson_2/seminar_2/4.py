# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков после запятой.
from math import pi
from decimal import Decimal, getcontext

getcontext().prec = 100  # а так будет 100

def circle(diameter):
    square = round((Decimal(diameter ** 2 / 4) * Decimal(pi)), 42)
    circumference = round((Decimal(pi) * Decimal(diameter)), 42)
    print(f'Площадь = {square}\nДлинна окр. = {circumference}')

    print(len(str(square).rpartition(".")[-1]), len(str(circumference).rpartition(".")[-1]))

print(len(str(pi)))
diameter = int(input("Введите диаметр: "))
circle(diameter)

# В отличие от аппаратного двоичного числа с плавающей запятой, 
# десятичный модуль имеет изменяемую пользователем точность 
# (по умолчанию 28 знаков), которая может быть настолько большой, 
# насколько это необходимо для данной задачи getcontext().prec = 28

# Площадь круга через диаметр S = d2 : 4 × π, где d — это диаметр. 
# Формула длины окружности через диаметр: l=π*d, 
# где π— число пи — математическая константа, d — диаметр окружности


r = int(input('Введите радиус: '))

i = 2 * r * 3.14  # Длина окружности

s = 3.14 * r ** 2  # Площадь круга

print(f"Длина окружности: {i:.42f}, площадь круга: {s:.42f}")