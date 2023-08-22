# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint

my_list = [randint(1, 20) for i in range(10)]
print(f"Исходный список: {my_list}")

new_list = []

for i in set(my_list):
    if not (my_list.count(i) == 1):
        new_list.append(i)

print(f"Список с дублирующимися элементами без дубликатов: {new_list}")

# --------------------------- вариант 2

new_list = [i for i in set(my_list) if not my_list.count(i) == 1]
print(f"Список с дублирующимися элементами без дубликатов: {new_list}")
