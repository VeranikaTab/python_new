# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔Избегайте магических чисел
# ✔Добавьте аннотацию типов, где это возможно

def convert_integer(decimal, radix):
    if radix > 36:
        return "Основание системы счисления должно быть не больше 36-ти!"

    number = ''
    while decimal > 0:
        decimal, reminder = divmod(decimal, radix)
        if reminder > 9:
            reminder = chr(ord('A') + reminder - 10)
        number = str(reminder) + number
    return number

num = int(input("Десятичное число: "))
base = int(input("Основание (2-36): "))
print(convert_integer(num, base))

# https://calcus.ru/perevod-sistem-schisleniya/iz-desyatichnoy-v-vosmerichnuyu
# перевод числа из десятичного в двоичное

num_dec = int(input("введите число: "))
res = ''
DIVIDER = 2
print(bin(num_dec))
while num_dec > 0:
    res = str(num_dec % DIVIDER) + res
    num_dec //= DIVIDER
print(res)

# ---------------------------------------------------

num_dec = int(input("введите число: "))
res = ''
DIVIDER = 8
print(oct(num_dec))
while num_dec > 0:
    res = str(num_dec % DIVIDER) + res
    num_dec //= DIVIDER
print(res)