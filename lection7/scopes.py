""" области видимости """
# LEGB - Local Enclosed Global  Built_in
#  Локальные Замкнутые Глобальные Встроенные
#  встроенные переменные str, list, dict, int 
# global() --> dict
# local()  -> dict\

# name = "Hello"

# def func(name2):
#     global name
#     print("GLOBALS", globals().get("name"))
#     print("LOCAL", locals().get("name"))

# func("Nastya")
# name = "Hello"


# count = 0

# def incr():
#     global count
#     count += 1
#     # print(count)

# incr()

# for i in range(4):
#     incr()
#     print(count)


# def atai():
#     nastya("маркер черный", "маркер красный", "маркер синий")
#     print("настя унесла маркер")


# def nastya(*markers):
#     print("унесла МАРКЕР")
#     return f"{markers} вернулся на доску"

# atai()



# def len(obj):
#     count = 0
#     for elem in obj:
#         count += 1
#     print(count)

# if len("abc") == 3:
#     print(True)
# else:
#     print(False)

# x = "глобальная переменная"
# def some_func():
#     x = "локальная переменная"
#     print(x)

# some_func()

# x = "глобальная переменная"
# def some_func():
#     x = "замкнутая переменная"
#     def some_func_2():
#         x = "локальная переменная"
#         print(x)                     # принтить последний х

#     some_func_2()
#     print(x)
# some_func()


# def add(x, y):
#     return x + y

# print(add(5, 6))
# print(add(7, 4))
# print(add(2, 9))


# def mylen(obj):
#     count = 0
#     for elem in obj:
#         count += 1
#     return(count)

# objects = [
#     [1, 2, 3, 4],
#     "abc",
#     "khfew"
# ]
# for obj in objects:
#     print(mylen(obj))

# print(len([1, 2, 3, 4]))
# print(len("abc"))
# print(len("khfew"))


""""
built-ins --> встроенная пространство имен - это встроенная пространство имен где находиться встроенные объкты
global --> глобальная пространство имен - это к чему у нас есть доступ к данной программе
enclosed --> замкнутая пространство имен которая находиться между глобальным и локальным простраства имен
local --> локальная пространство имен - это самая вложенная(внутреняя) функция
"""
# this_var_is_visible = "You can see me inside and outside the function"                    # это переменная на глобальном уровне но в границах этой программы

# def var_visibility():
#     this_var_is_not_visible = "You can see me only inside the function"
#     print(this_var_is_not_visible)

# print(this_var_is_visible)


# import builtins
# print(dir(builtins))         # показывает встроенные функции python


# word = "I'm global"            # глобальная переменная

# def func_a():
#     word = "I'm local"         # локальная переменная
#     print(word)         # интерпритатор ищет имя word сначала внутри функции т.е в локальном прострастве имен, есди не находит то переходит на глобальную простраству имен

# func_a()                # если вызвать функцию то мы получим I'm local потому что программа ищет переменную word внутри функции
# print(word)             # здесь print принтует глобальную переменную потому что он не находиться внутри функции


# word = "I'm global"

# def outer():                       # функция outer замкнутая простраство (находится межну локальным и глобальными пространствами )
#     word = "I'm enclosed"
#     print(word)

#     def inner():                   # а inner локальная 
#         word = "I'm local"
#         print(word)

#     inner()

# outer()
# print(word)


# name = 'makers'
# globals()['name'] = 'bootcamp' --> DICTIONARY перезаписали значение

""" 
globals() --> возвращает текущий словарь глобального пространсва имен
locals() --> возвращает словарь локального пространства имен
"""
# globals()
# name = 'Makers'
# name = "Bootcamp"
# print(globals())
""" это одно и тоже """
# dict_  ={'name': 'Makers', 'name': 'Bootcamp'}

# locals()
# def func():
#     name = 'Bootcamp'
#     print(locals())
# func()
# def func(company):
#     name = 'Bootcamp'
#     print(locals())
# func(company='Makers')

# def info(name, age, height):
#     name = 'Alice'
#     age = 23
#     print(locals())

# info(name = 'Carly', age = '24', height = 166)

""" изменение переменной вне области видимости """
# namespace --> простраство имен



""" lection scope """
# * - это распаковка

# def func(arg1, arg2=[]):
#     arg2.append(arg1)
#     print(arg2)

# func("hello")
# func("world")


# def func(arg1, arg2):
#     arg2 = []
#     arg2.append(arg1)
#     print(arg2)

# func("hello")
# func("world")

# this_var_is_visible = 'Can be seen inside and outside function'

# def var_visibility():
#     this_var_is_not_visible = 'cannot be seen outside function'
#     return

# print(this_var_is_visible)
# print(this_var_is_not_visible)

# def func(a, b):          # внутри скобок параметры
#     return a + b
# res = func(12, 14)       # внутри скобок аргументы
# print(res)


# def some_func(name):
#     print(locals())

# some_func("Asus")

# name = "Asus"
# def get_name():
#     name = "Acer"
# get_name()
# print(name)

# name = "Lenovo"
# def func_one():
#     name = 'Asus'

#     def func_two():
#         name = 'Acer'
#         print(name)
#     func_two()
# func_one()

# map = "Lenovo"
# def func_one():
#     map = 'Asus'

#     def func_two():
#         map = 'Acer'
#         print(map)
#     func_two()
# func_one()

"""
local
enclosed
global
duilt-ins
LEGB
"""

# for x in range(1, 100):
#     if isinstance(x, str):
#         break
#     else:
#         continue

# print(x)

# str_ = "hello"
# if str_ == "John":
#     name = "John"
# else:
#     name = "defald"
# print(name)


""" 
global
nonlhello"
# if str_ == "John":
#     name = "John"
# else:
#     name = "defald"
# print(name)
glocal
"""

# names = {}

# def func():
#     # names = {}
#     names["key"] = 'John'

# func()
# print(names)


"""global scope"""
# def f():
#     global s
#     s += "GFG"
#     print(s)
#     s = 'Look for Geeksforgeeks Python Sevtion'
#     print(s)

# s = "Python is great"
# f()
# print(s)

# def func_one():
#     x = "John"
#     def func_two():
#         nonlocal x
#         x = "Raychel"
#         print("First: ", x)
#     func_two()
#     print("Second: ", x)

# func_one()














