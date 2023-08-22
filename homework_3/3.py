# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things = {"фонарь": 1, "палатка": 5, "спальник": 2}
max_value = 5

sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))

for key, value in sorted_things.items():
    if value <= max_value:
        print(key)
    max_value -= value

# ---------------------------

things = {'фонарь': 1, 'палатка': 5, 'спальник': 2}
max_value = 5
new_things = []

for key, value in sorted(things.items()):

    if value <= max_value:
        new_things.append(key)
        max_value -= value


print(*new_things)
