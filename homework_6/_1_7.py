# Задание №7 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

"""Функция возвращает истину, если дата может существовать или ложь, 
если такая дата невозможна. Формат DD.MM.YYYY (год может быть в диапазоне [1, 9999])"""


def check(date: str):
    day, month, year = map(int, date.split("."))
    if (year < 0 or
            year > 9999 or
            month < 0 or
            month > 12 or
            day < 0):
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    leap = leap_year(year)
    if leap and month == 2 and day > 29:
        return False

    if not leap and month == 2 and day > 28:
        return False

    return True


# Високосный или нет
def leap_year(year):
    return not year % 400 != 0 or year % 4 == 0 and year % 100 != 0
