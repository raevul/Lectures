"""list comprehension"""
# list_ = [i for i in range(50)]
# i --> что делаем с элементом
# for i  --> что берём в данном случае элемент i
# in range(50) --> откуда берём здесь из объекта функции range 

# list_ = [i for i in range(11) if i % 2 == 0]
# if --> после if идет условие           (фильтр)

# list_ = []
# for num in range(1, 21):
#     list_.append(num *2)

# этот же список с помощью list comprehension
# list_ = [num * 2 for num in range(1, 21)]
# print(list_)


# list_users = ['Alice', 'Sam', 'Sandy', 'Ben', 'John']
# invitations = ['Вы приглашены ' + name for name in list_users]   # берём name из списка list_users
# print(invitations)

# list1 = [10, 5 , -6, -8, 15, 20, 3, 14]
# list2 = [num for num in list1 if num % 2 == 0]
# print(list2)
# теперь отфилтрируем в 1 варианте числа которые делятся на 2 без остатка а во 2 добавим еще условие числа делятся без остатка но больше нуля (без отрицательных чисел)
# list1 = [10, 5 , -6, -8, 15, 20, 3, 14]
# list2 = [num for num in list1 if num % 2 == 0 and num > 0] or также можно использовать
# print(list2)
# if num % 2 == 0 and num > 0 --> это все называется фильтром

# list_ = [num ** 2 for num in range(1, 11) if num % 2 == 0]
# print(list_)

# strings = ['1998', '2001год', '2008г', '2022']
# list_ = [year for year in strings if year.isdigit()]
# print(list_)

# измеряем длину строки (имени)
# list_ = ['Raychel', 'John', 'Alice', 'Sam']
# list_ = [len(name) for name in list_]
# print(list_)

# list_ = [-5, -12, 0, 2, 8, 4, -4, 10]
# list_ = [x if x < 0 else x ** 2 for x in list_]     # if в начале это не фильтр, фильтр срабатывает только если он будет в конце
# print(list_)

# list_ = [-5, -12, 0, 2, 8, 4, -4, 10]
# list_ = [x if x < 0 else x ** 2 for x in list_ if x % 2 == 0]     # фильтр срабатывает первым
# print(list_)


# names = ['raychel', 'john', 'peter', 'jessica', 'bill',
#          'steven', 'stev213', 'sam8328', 'james']

# filtered_names = [x + ' MAKERS' if len(x) >= 5 else x + ' makers' for x in names if x.isalpha()]
# print(filtered_names)
"""теперь длинную list coprehension сделаем короче(красиво)"""
# filtered_names = [
#     x + ' MAKERS' 
#     if len(x) >= 5 
#     else x + ' makers' 
#     for x in names 
#     if x.isalpha()
#     ]

"""теперь сделаем это с циклом for"""
# filtered_names = []
# for x in names:
#     if x.isalpha():
#         if len(x) >= 5:
#             result = x + ' MAKERS'
#             filtered_names.append(result)
#         else:
#             result = x + ' makers'
#             filtered_names.append(result)
# print(filtered_names)

# john = {'name': 'John', 'age': 22}
# raychel = {'name': 'Raychel', 'age': 23}
# peter = {'name': 'Peter', 'age': 17}

# users = [john, raychel, peter]

# ages = [user.get('age', None) for user in users]

# bigger = 0
# smaller = 0
# count = 0

# for age in ages:
#     if age >= 18:
#         bigger += 1
#     else:
#         smaller += 1
#     count += 1

# bigger = bigger * (100 / count)
# smaller = smaller * (100 / count)

# print(f'Процент пользователей с возрастом больше 18: {round(bigger)} процента')
# print(f'Процент пользователей с возрастом меньше 18: {round(smaller)} процента')

# matrix = [
#     [0, 2, 5, 6]
#     [7, 3, 0, 7]
#     [5, 7, 1, 6]
# ]
# ucompress = [n for row in matrix for n in row]
# uncompress = []
# for row in matrix:
#     for n in row:
#         uncompress.append(n)
# print(uncompress)


# n = int(input("Введите число от 1 до 10:"))
# dict_ = {n: n ** 2 for n in range(1, 501) if n % n == 0}
# print(dict_)

# n = int(input("Введите число от 1 до 10:"))
# dict_ = {range(1, 501)}
# d = {n: n ** 2 for n in dict_ }
# print(dict_)


"""task14"""
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# new_dict = {k: k1 for k, v in dict_.items() for k1, v1 in v.items() if v1 == max(v.values())}
# print(new_dict)
"""task8"""
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(name) <= 4 else 'longer' for name in list_name]
# print(new_list)
"""task10"""
# n = int(input())
# dict_ = {num: num ** 2 for num in range(1, 501) if num % n == 0}
# print(dict_)
"""task11"""
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k:[v for v in range(1,v + 1)] for k,v in a.items()}
# print(dict_)
""" пример """
# dict_ = {1: 1, 2: 2, 3: 3}
# dict_ = {key: list(range(1, value + 1)) for key, value in dict_.items()}
# print(dict_)
"""task12"""
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: v for k, v in dict_.items() if v % 2 == 0}
# print(a)
"""task13"""
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [num for num in string_.split() if num.isdigit()]
# print(list_)
"""task15"""
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {k: [v[k1] for k1 in v.keys() ][0] for k, v in my_dict.items()}
# print(dict_)
"""extratask2"""
# dict_ = {1: 'one', 2: 'two', 3: 'three'}

# for key, value in dict_.items():
#     if key % 2 == 0:
#         dict_[key] = len(value)
#     elif key % 2 == 1:
#         dict_[key] = len(value) ** 3
# print(dict_)
"""comprehension extratask2"""
# dict_ = {1: 'Hello', 2: 'World', 3: 'John'}
# dict_ = {key: len(value) if key % 2 == 0 else len(value) ** 3 for key, value in dict_.items()}
# print(dict_)



    

