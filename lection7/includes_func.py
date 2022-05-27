""" Встроенные  функции """
"""
len() - вытаскивает длину объкта
print() - выводит в консоль значение
input() - запрашивает данные
dir() - выводит методы объекта
divmod() - остаток от деления
globals() - выводит словарь с глобал данными
local() - выводит словарь с локальными данными
round() - округляет число
enumerate() - нумирует итерируемые объекты, можно указать старт нумерации
pow() - степень выводит, остаток от деления
min() - минимальное значение выводит
max() - максимальное значение выводит
type() - выводит тип данных объекта
range - создает диапазон
sorted - временно сортирует объект
"""

# negative = -125
# absolute = abs(negative)
# print(absolute)

"""all()"""
# list_of_zeros_num = [0, 1, 2]
# is_true = all(list_of_zeros_num)
# print(is_true)

# tuple_of_trues_obj = (True, 1, 2, 3)
# is_true = all(tuple_of_trues_obj)
# print(is_true)


# def all_(iterable):
#     for element in iterable:
#         if not element:
#             return False
#         return True

# is_true = all_((True, 1, 2, 3, [1, 2, 3, 0]))
# print(is_true)

# visa_cards = {
#     "visa1": "100$",
#     "visa2": "50$",
#     "visa3": "2000 сом",
#     "visa4": 0
# }
# is_true = all(visa_cards.values())
# print(is_true)

"""any()"""
# tuple_of_trues_and_falses = (False, False, True, False)
# print(any(tuple_of_trues_and_falses))

# def any_(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# print(any_([0, 0, 1]))

"""ascii()"""
# example_one = ascii([0, 1, 'item'])
# print(example_one)


# one = bin(1)
# print(one)

# key = 0b1
# encrypt = key ^ 2
# print(encrypt)


# def add(a, b):
#     return a + b

# is_callable = callable(add)
# print(is_callable)

# @property
# def name(name):
#     print(name)
# name()

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# res = list(enumerate(seasons))
# print(res)


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# res = dict(enumerate(seasons))
# print(res)

# name1 = ['John', 'Raychel']
# name2 = ['Peter', 'Jessica']
# for index, value in enumerate(name1):
#     print(value)
#     print(name2[index])



"""task1"""
# from functools import reduce
# list_ = [1, 2, 3, 4]  
# result = reduce(lambda x, y: x + y, list_)
# print(result)
"""task10"""
# from functools import reduce
# list_ = ['Paul', 'Ringo', 'George', 'John'] 
# result = reduce(lambda a, b: a if (len(a) > len(b)) else b, list_)
# print(result)
