# Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8


def fibonacci(amount: int):
    a, b = 0, 1
    for __ in range(amount):
        yield a
        a, b = b, a + b


if __name__ == "__main__":

    num = int(input("Введите количество элементов для генерации чисел Фибоначчи: "))
    if num > 0:
        for item in fibonacci(num):
            print(item, end=" ")
    else:
        print("Введено отрицательное значение. Выход из программы")
