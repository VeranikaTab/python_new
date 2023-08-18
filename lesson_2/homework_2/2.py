#  Напишите программу, которая принимает две строки 
# вида “a/b” — дробь с числителем и знаменателем. 
# Программа должна возвращать сумму 
# и *произведение дробей. Для проверки своего 
# кода используйте модуль fractions.
from fractions import Fraction
def process_fractions(frac1_str, frac2_str):
    # Преобразуем дроби из строк в числа
    numerator1, denominator1 = map(int, frac1_str.split("/"))
    numerator2, denominator2 = map(int, frac2_str.split("/"))

    # Вычисляем сумму дробей
    sum_frac_num = numerator1 * denominator2 + numerator2 * denominator1
    sum_frac_denom = denominator1 * denominator2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # Вычисляем произведение дробей
    prod_frac_num = numerator1 * numerator2
    prod_frac_denom = denominator1 * denominator2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

frac1_str = input("Введите дробь 1 -> ")
frac2_str = input("Введите дробь 2 -> ")

sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

print(f"Сумма дробей - {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей - {prod_frac[0]}/{prod_frac[1]}")

# решение с помощью модуля fractions


numerator1, denominator1 = map(int, frac1_str.split("/"))
numerator2, denominator2 = map(int, frac2_str.split("/"))
frac1_str = Fraction(input("Введите дробь 1 -> "))
frac2_str = Fraction(input("Введите дробь 2 -> "))

print(f"Сумма дробей = \
      {numerator1 * denominator2 + numerator2 * denominator1}/{denominator1 * denominator2 }")
print(f"Произведение дробей = {numerator1 * numerator2}/{denominator1 * denominator2}")