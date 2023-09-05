# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8
# - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint

# бьют
position_1 = [[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]

# не бьют
position_0 = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]


def check_positions(pos):
    for i in range(0, 7):
        for j in range(i + 1, 7):
            if (pos[i][0] - pos[j][0] == pos[i][1] - pos[j][1] or
                    pos[i][0] == pos[j][0] or pos[i][1] == pos[j][1]):
                return False
    return True


print(check_positions(position_0))
print(check_positions(position_1))

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


def find_position():
    list_right_pos = []
    quantity_position = 4
    while quantity_position > 0:
        pos = [[randint(0, 8), randint(0, 8)] for _ in range(0, 8)]
        if check_positions(pos):
            list_right_pos.append(pos)
            quantity_position -= 1
    return list_right_pos


print(find_position())
