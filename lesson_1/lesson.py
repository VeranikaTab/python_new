# константы! указываются большими строчными буквами, не может вводить пользователь
# н-р MAX_COUNT = 1000    ZERO = 0   DATA_AFTER_DELETE = 'No data'   DAY = 60 * 60 * 24
# Встроенные True - истина False - ложь None - ничего
name = 'Alex'
age = None

# функция id() возвращает адрес объекта в оперативной памяти ПК
a = 42
print(id(a))
a = "hello world"
print(id(a))
a = 42.0 * 3.141592 / 2.71828
print(id(a))
# Зарезервированные слова, keyword.kwlist
# False, None, True, and, as, assert, async, await, break, class,
# continue, def, del, elif, else, except, finally, for, from,
# global, if, import, in, is, lambda, nonlocal, not, or, pass,
# raise, return, try, while, with, yield
# не могут быть переменными

# Вывод, функция print()
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep=' ' - разделитель пробел    end='\n' - перенос на новую строку

print(name, age, a, 456, "text")

# если хотим использовать иной разделитель sep или end, то указываем
# при этом пробел до и после знака равно не ставится!
print(name, age, a, 456, "text", sep='=^.^=', end='\n(___)\n')

print(name, age, a, 456, "text", sep='___', end='(=^.^=)\n')

# Ввод, функция input()
# result = input([prompt])
name = input('Ваше имя: ')
# age = int(input('Ваш возраст: '))
# int() — целый тип или float() —
# вещественный тип, число с плавающей запятой
ADULT = 18 # КОНСТАНТА, НЕ ДОЛЖНО БЫТЬ МАГИЧЕСКИХ ЧИСЕЛ!
age = float(input('Ваш возраст: '))
how_old = age - ADULT
print(how_old, "лет назад ты стал совершеннолетним")


# Если, if

# операции Сравнения
# «==» — равно «!=» — не равно
# «>» — больше «<=» — меньше или равно
# «<» — меньше «>=» — больше или равно

pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    print('Но будьте осторожны')
print('Работа завершена')

# Иначе, else

pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны')
else:
    print('Доступ запрещён')
print('Работа завершена')

# Еще если, elif
color = input('Твой любимый цвет: ')
if color == 'красный':
    print('Любитель яркого')
elif color == 'зелёный':
    print('Ты не охотник?')
elif color == 'синий':
    print('Ха, классика!')
else:
    print('Тебя не понять')

# Выбор из вариантов, match и case
color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')

# Логические конструкции, or, and, not
# ● and — логическое умножение «И»;
# ● or — логическое сложение «ИЛИ»;
# ● not — логическое отрицание «НЕ».

# first |second |first and second | first or second | not first
# True     True         True            True            False
# False    True         False           True            True
# True     False        False           True             -
# False    False        False           False            -

# Вычислим високосный год в Григорианском календаре поэтапно:
year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

# А теперь выберем все случаи, когда год обычный и запишем их в одну строку:
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")
# Python последовательно слева направо проверяет логическое выражение,
# формируя финальный ответ — True или False.

# Ленивый if
# Ещё раз посмотрим на прошлый пример кода.

#       if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:

# В Python как и в некоторых других языках программирования if "ленивый". Если в
# логическом выражении есть оператор or и первое значение то есть левое вернуло
# истину, дальнейшая проверка не происходит, возвращается True. Если в
# логическом выражении есть оператор and и левая половина вернула ложь, то
# возвращается False без проверки правой половины выражения.

# Проверка на вхождение, in
# На одном из следующих уроках поговорим о коллекциях. Пока для простоты
# договоримся, что список целых чисел в квадратных скобках — массив данных.
# Оператор in проверяет вхождение элемента в последовательность.

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num in data:
    print('Леонардо передаёт привет!')
# А теперь тот же самый код, но с конструкцией not — отрицание:
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num not in data:
    print('Леонардо грустит :-(')
# Обратите внимание на порядок слов в строке 3. Python использует максимально
# приближенные к человеческому, а точнее к английскому языку стиль
# программирования: "Если число не входит в данные, то…"

# Тернарный оператор
# Было:
my_math = int(input('2 + 2 = '))
if 2 + 2 == my_math:
    print('Верно!')
else:
    print('Вы уверены?')
# Стало:
my_math = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')
# Слева от if записываем выражение для истины, справа от else результат для лжи.

# Логический цикл while
# Цикл while является циклом с предусловием. Проверяем логическое условие,
# аналогично "если" и в случае истинности выполняем вложенный блок кода. Далее
# возвращаемся к проверке условия.
# Попробуем перебрать всё чётные числа от нуля до введённого пользователем
# исключительно.
num = float(input('Введите число: '))
count = 0
while count < num:
    print(count)
count += 2
# Проверка условия после while и выполнение тела цикла продолжается до тех пор,
# пока условие истинно.

# Возврат в начало цикла, continue
# При необходимости работу цикла можно прервать и досрочно вернуться к проверке
# условия. Для этого используем зарезервированное слово continue.
# Выведем все чётные числа (как в прошлом примере), кроме тех, которые кратны 12.
num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue
    print(count)
# if внутри цикла проверяет кратность двенадцати. В случае истинности команда
# continue возвращает нас к началу цикла, к while.

# STEP = 2 — добавили константу для движения по чётным и ушли от
# "магических чисел". Теперь изменение условия на "вывод чисел кратных 5"
# потребует замены числа в одном месте кода.
# Ввели переменную limit. Чтобы цикл не выводил лишние числа, больше
# введенного num, на каждой проверке цикла while надо вычитать значение
# шага. Но шаг — константа. Для экономии ресурсов ПК и ускорения работы
# кода логично сделать вычитание один раз перед циклом и сравнивать
# значения быстрее, без вычитания в строке while

# Досрочное завершение цикла, break
# Она отлично подходит для создания циклов с постусловием,
# бесконечных циклов с возможностью выхода.

# Рассмотрим на примере программы, которая просит ввести число внутри заданного
# диапазона.
min_limit = 0
max_limit = 10
while True:
    print('Введи число между', min_limit, 'и', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
print('Было введено число ' + str(num))
# Конструкция while True: создаёт бесконечный цикл. Вместо True можно было бы
# подставить любое выражение, которое всегда возвращает истину. Но именно такая
# реализация обеспечивает лучшую читаемость и быстродействие.

# Действие после цикла, else

# Зарезервированное слово else может применятся не только к ветвлениям, но и к
# циклам. Для этого else должно быть расположено на том же уровне, т.е. иметь
# столько же пробельных отступов, что и начало цикла — while.
# Доработаем прошлую программу и дадим 3 попытки на попадание в диапазон.
min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input('Введи число между ' + str(min_limit) + ' и' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))
# Что изменилось в коде:
# ● Добавили счётчик count. Цикл проверяет не уменьшился ли счётчик до нуля.
# Если нет, переходим в тело цикла. Выводим значение счётчика на каждом
# витке цикла и уменьшает его на единицу.
# ● Добавили else для while. Логика следующая. Если пользователь ввёл верное
# число и сработала команда break, блок else для цикла игнорируется. А если
# числа вводились ошибочно, счётчик досчитал до нуля и произошел выход из
# цикла по "лжи" в while. В этом случае сработает блок кода после else для
# цикла.
# Если коротко, вызов break в цикле игнорирует else для цикла.
# ● quit() — ещё одна функция для завершения кода раньше, чем мы дойдём до
# конца файла. Это вторая функция. Первой, exit() мы пользовались для
# завершения работы сеанса интерпретатора. Работают они аналогично.
# ● Мы добавили пустые строки в код. Python игнорирует такие строки. Но
# разделение кода на блоки по смыслу упрощает чтение. Кроме того, на
# следующих лекциях мы поговорим о пустых строках, которые прописаны в
# PEP-8. Но не ставьте пустые строки после каждой строки кода. Если вам
# нравится большой межстрочный интервал, настройте его в своей IDE.
# ● PEP-8! Кстати, последняя строка в файле должны быть пустой. Именно одна,
# а не ноль, и не две.


# Цикл итератор for in

# Цикл for in используется Python разработчиками намного чаще. Прежде чем
# приступить к его рассмотрению уточню, что команды continue, break и else могут
# применяться к циклу for in точно так же как и до этого в цикле while.

# Рассмотрим работу цикла в качестве итератора последовательности.
# Итерироваться будем по массиву с числами из части про ветвления и проверку на
# вхождение.
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)
# Цикл последовательно перебирает все элементы массива data и поочерёдно
# помещает их в переменную item. После for указываем переменную или переменные
# для приема значений, они изменяются на каждом витке цикла. После in указываем
# объект, из которого последовательно берём данные.
# 🔥 Важно! Нельзя изменять содержимое контейнера (в нашем примере
# data) во время итерации по нему, т.е. внутри цикла. Это приведет к
# неожиданным ошибкам.

# Цикл по целым числам, он же арифметический цикл, функция range()

# Для перебора целых чисел цикл for in используется в связке с функцией range(). Она
# выступает в качестве объекта итератора. Пример печати чётных чисел от нуля до
# введённого числа может выглядеть так с циклом for:
num = int(input('Введите число: '))
for i in range(0, num, 2):
    print(i)
# 🔥 Важно! Аргументами функции range() должны быть целые числа, int()
# Рассмотрим подробнее варианты работы функции range(). Обратите внимание на
# количество переданных функции аргументов
# range(stop) — перебираем значения от нуля до stop исключительно с шагом один
# range(start, stop) — перебираем значения от start включительно до stop
# исключительно с шагом один
# range(start, stop, step) — перебираем значения от start включительно до stop
# исключительно с шагом step.
# Пара если.
# ● Если значение step отрицательное, перебор будет в сторону уменьшения.
# ● Если start больше stop при положительном step или наоборот start меньше
# stop при отрицательном step, цикл не сработает ни разу. range(10, 5, 2) -
# ничего

# Имена переменных в цикле

# Исторически сложилось, что для переменных, которые "считают арифметику" в
# цикле используются переменные i, j, k. Именно в таком порядке с учёт
# вложеннности. Этой традиции более полувека. Так что смело продолжайте её и ваш
# код поймут. Например так выглядят 3 вложенных цикла. Обратите внимание на
# отступы, которые показывают уровень вложенности
count = 10
for i in range(count):
    for j in range(count):
        for k in range(count):
            print(i, j, k)
# А так выглядят два последовательных цикла
count = 10
for i in range(count):
    print(i)
for i in range(count):
    print(i)
# Однако, когда мы перебираем какие-то данные, вместо однобуквенных переменных
# можно использовать подходящие имена. Например так может выглядеть перебор
# животных, которые хранятся в массиве данных.
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for animal in animals:
    print(animal)
# Как вы помните читаемость имеет значение.  имеем массив животных
# для каждого животного в списке животных печатаем животное

# Цикл с нумерацией элементов, функция enumerate()

# В финале рассмотрим ещё одну функцию, enumerate(). Она позволяет добавить
# порядковый номер к элементам итерируемой последовательности. Доработаем
# пример с животными. Будем выводить порядковый номер перед указанием
# животного.
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
# Что изменилось?
# ● После for указано две переменные через запятую. В i будет помещаться
# порядковый номер. В animal очередное животное из списка.
# ● Функция enumerate() получила в качестве первого аргумента список
# животных. Второй аргумент — стартовое значение счётчика, т.е. первое
# значение, которое попадёт в i.
# Если второй аргумент не передать, нумерация начнётся с нуля.
# 🔥 Важно! Функция enumerate позволяет перебирать только целые числа в
# порядке возрастания с шагом один.
