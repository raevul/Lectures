""" Для создания функции введется ключевое слово def посло него идет имя(название) функции, в круглых скобках идет параметр """
""" return - возвращает элемент, похож на print """
# pass - ничего не выведет в терминал
# def test_func(word):                # Внутрь скобок введется параметр(переменная). Этот параметр работает только внутри функции.     
#     print(word, end="")      # Внутри функции можно прописовать что угодно циклы(while, for), условные операторы(if, else) и т.д 
#     print("!")

# test_func("Hello")                # Вызваем функцию (по ее названию) test_func == print
# test_func(5)                     # Функцию можно вызывать несколько раз
# test_func(5.3)

# def summa(a, b):
#     res = a + b
#     print("result: ", res)

# summa(5, 6)
# summa('H', 'i')

# def summa(a, b):
#     # res = a + b           # переменную можно не указывать 
#     return a + b

# res = summa(5.4, 5.6)
# print(res)
# print(summa('H', 'i'))



""" Находим минимальное число из списка """
nums1 = [5.3, 7.2, 9, 4, 2.1]

min = nums1[0]
for el in nums1:
    if el < min:
        min = el
print(min)

nums2 = [5.4, 7.2, 9.1, 4.7, 2]

min2 = nums2[0]
for el in nums2:
    if el < min2:
        min2 = el
print(min2)
""" Эти программы в виде функции """
# def minimal(list_):
#     min_number = list_[0]
#     for el in list_:
#         if el < min_number:
#             min_number = el

#     return min_number               # Минимальные элементы из этих списков

# nums1 = [5.3, 7.2, 9, 4, 2.1]
# min1 = minimal(nums1)

# nums2 = [5.4, 7.2, 9.1, 4.7, 2]
# min2 = minimal(nums2)

# if min1 < min2:                 # Минимальный элемент из двух списков
#     print(min1)
# else:
#     print(min2)


""" lambda функция """
# func = lambda x, y: x * y
# res = func(5, 4)     # or print(func(5, 4))
# print(res)

""" lambda функция записывается в одну строчку чем функция def """

# def summa(x, y):
#     return x * y

# print(summa(5, 4))


# func = lambda x, y: x * y
# print(func(5, 4))


# определение функции
# def sayHello():
#     print('hello')
#     print('world')
#     print('and everybody')

# sayHello()                  # вызываем функцию если не вызвать функцию то принты ничего не выведят


# def square(x):
#     print('Квадрат числа', x, '=', x ** 2)


""" главная программа(в ней будем вызывать функции) """
# for i in range(1, 11):
#     square(i) 
# square(5)
# square(10)


# def multiply(a, b):
#     print(a * b)

""" главная программа(в ней будем вызывать функции) """
# multiply(3, 5)
# multiply(3, 100)

# def even(a):
#     if a % 2 == 0:
#         print(a, 'четное')
#     else:
#         print(a, 'нечетное')


""" главная программа(в ней будем вызывать функции) """
# for i in range(20, 30):
#     even(i)


# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr = pr * i
#         print(pr)

# factorial(5)


# if 5 > 7:
#     def primer():
#         print('hello')
# else:
#     def primer():
#         print('HELLO')

# primer()
"""task1"""
# def add(a, b):
#     return a + b

# add(5, 5)
"""task2"""
# def get_string_length(a):
#     return (len(a))

# print(get_string_length('hello'))
"""task3"""
# def get_type(a, b):
#     return (type(a), type(b))

# print(get_type(5, "s"))

# def get_type(arg1, arg2):
#     a = type(arg1)
#     b = type(arg2)
#     return a, b

# print(get_type(5, 's'))
"""task4"""
# def divide(num1, num2):
#     return num1 / num2

# print(divide(20, 2))
"""task5"""
# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# def dictionary(dict_):
#     for key in dict_:
#         print(key)
# dictionary(dict_)
"""task6"""
# num = 6
# if not num % 2 == 0:
#     def check():
#         print('It is odd number')
# elif num % 2 == 0:
#     def check():
#         print('It is even number')

# check()
# num = 6
# def check(num):
#     if num % 2 == 0:
#         return "It is even number"
#     else:
#         return "It is odd number"

# print(check(num))
"""task7"""

"""task8"""
# def max_num(num1, num2):
#     num1 < num2
#     return max(num1, num2)
# print(max_num(10, 12))
"""task9"""
# def multiple_list(lst):
#     mult = 1
#     for i in list(lst):
#         mult *= int(i)
#     return mult

# print((multiple_list([1, 2, 3, 4, 5, 6])))  
"""task10"""
# def sum_digits(num):
#     sum = 0
#     for i in str(num):
#         sum += int(i)
#     return sum

# print(sum_digits(105))


"""синтаксис функции"""

"""
def name_of_function():      # сначала идет ключевое слово def затем имя функции в скобках идет параметр
    some_code                # тело функции
    return variable          # возвращает переменную 

name_of_function()           # вызываем функцию
"""

# def function():
#     print("The function is called")
#     return 'Makers'
# print(function())


# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)          # print встроенная функция которая показыввает результат в терминалеб не возвращает результат
#     return num1 - num2          # return не показывает результат в терминале чтобы посмоьреть результат нужно рапринтить функцию
                                
# substract()          # если не вызвать функцию то она не будет работать
# variable = substract()     # можно обернуть функцию в переменную и запринтить
# print(variable)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, substract()]
# print(list_)

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)  
#     return num1 - num2 

# def function():
#     print("I'm calling substract function")
#     # print(substract())
#     variable = substract()
#     return variable
# print(function())


# def multiply(a, b):
#     return a * b

# num1 = 70
# num2 = 10
# print(multiply(num1, num2))


# def welcome(name, last_name):
#     return f'Welcome, {name} {last_name}!'

# name = input()
# last_name = input()
# print(welcome(name, last_name))

""" функция которая фильтрует и выводит из введеного слова все гласные """
# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'e', 'i','u']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     print(list_vowels)
#     result = ''.join(list_vowels)
#     return result

# my_word = input('Enter the word: ')
# print(get_vowels(get_word(my_word)))


# def info(name = 'Sam', age = 20):
#     return f'{name} is {age} years old.'

# print(info('John', age = 22))

# def test(n1, n2 = 9):
#     return n1 + n2

# print(test(n1 = 10, n2 = 9))

# def test(n1, n2 = 9):
#     return n1 + n2

# print(test(n1 = 10))

# def create_profile(name, age, image = 'default.jpg'):
#     return name, age, image

# print(create_profile(name = 'Alice', age = 20, image = 'flower.png'))


""" *args and **kwargs """
# *args - позиционный аргумент - создает множества позиционных аргументов
# **kwargs - именованный аргумент - создает словарь с именованными аргументами
# после * можно задать любое слово необязательно args и kwargs но желательно использовать их

# def func(required, *test, **some):
#     print(required)

#     if test:
#         print(test)
#     if some:
#         print(some)

# func('Makers', 'bootcamp', 'python', name = 'Raychel', age = 23)

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)

# many(1, 2, 3, name = 'John', job = 'IT-specialist')


# def even(x):
#     return x % 2 == 0           # if x % 2 == 0           if x % 2 == 0    
#                                 #     return True               return True
#                                 # else:                   return False
#                                 #     return False
# for i in range(1, 11):
#     print(i, even(i))


"""task2"""
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print(x)
#     x = 'Я могу изменяться'
#     print(x)
    
# my_func()
# print(globals())
"""task3"""
# num = 3
# def mul():
#     global num
#     num = num ** 2
#     return num
# mul()
# mul()
# mul()
# print(num)
"""task4"""
# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
"""task5"""
"""task6"""
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# for k, v in a.items():
#     if v >= 17:
#         print(f'{k}, Вы можете войти в клуб')
#     else:
#         print(f'{k}, извините, Вы не проходите по age-control')
"""task7"""




