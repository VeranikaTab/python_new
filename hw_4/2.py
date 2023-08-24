# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def function(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        new_dict[hash(value) if hash(value) == value else str(value)] = key
    return new_dict
    # for key, value in kwargs.items():
    #     new_dict[hash(value)] = key
    # return new_dict


print(function(item=8, cat="yashka", улитка="не кот", число=987))