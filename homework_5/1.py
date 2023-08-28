# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def split_path(file_path):
    path_parts = file_path.rsplit('/', 1)
    path = path_parts[0] if len(path_parts) > 1 else ''

    filename = path_parts[-1].rsplit('.', 1)
    file = filename[0]
    extension = '.' + filename[1] if len(file) > 1 else ''

    my_tuple = (path, file, extension)
    return my_tuple


path = "C:/Users/Anika/Desktop/file_python.txt"
result = split_path(path)
print(result)
