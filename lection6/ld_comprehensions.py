"""
List comprehension  (генератор списков)
Dict comprehension  (генератор словарей)
"""
# even = []
# for x in range(1, 101):
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         continue
# print(even)

# even = [x for x in range(1, 101) if x % 2 == 0]       # первый х это ответ(результат) а второй это переменная которую мы создали
# print(even)

# num = [2, 4, 6, 8, 10]
# list_ = [x ** 2 for x in num]
# print(list_)
"""это же с циклом"""
# num = [2, 4, 6, 8, 10]
# ls = []
# for x in num:
#     ls.append(x ** 2)
# print(ls)

# list_1 = [10, 5, 8, -4, -8, 20, 3, 4]
# list_2 = [x for x in list_1 if x % 2 == 0 and x > 0]
# print(list_2)

# years = ['1997', '1997 год', '1997г']
# list_ = [year for year in years if year.isdigit()]
# print(list_)

# names = ['john', 'raychel', 'peter', 'jessica']
# count_of_names = [{name: len(name)} for name in names]
# print(count_of_names)

# numbers = [-5, -12, 0, 1, 2, 8, 4, 5, 7, 9]
# new_numbers = [number if number < 0 else number ** 2 for number in numbers]
# print(new_numbers)

""" синтаксис --> условия ветвления: for: фильтрация """

# ls = [x if x < 0 else x ** 2 if x <= 0 else x ** 2 for x in range(1, 100)]
# print(ls)

# numbers = [-5, -12, 0, 1, 2, 8, 4, 5, 7, 9]
# new_numbers = [number if number < 0 else number ** 2 for number in numbers if number % 2 == 0 or number < 0]
# print(new_numbers)
"""в виде цикла"""
# numbers = [-5, -12, 0, 1, 2, 8, 4, 5, 7, 9]
# new_numbers = []
# for number in numbers:
#     if number % 2 == 0 or number < 0:
#         if number < 0:
#             new_numbers.append(number)
#         else:
#             new_numbers.append(number ** 2)
# print(new_numbers)

# matrix = [
#     [1, 2, 3],
#     [10, 11, 12],
#     [20, 21, 22],
#     [30, 31, 32]
# ]
# uncompress = [x for row in matrix for x in row]
# print(uncompress)

# matrix = [
#     [1, 2, 3],
#     [10, 11, 12],
#     [20, 21, 22],
#     [30, 31, 32]
# ]
# uncompress = []
# for row in matrix:                   # добавляем в переменую row значение из переменной matrix
#     for x in row:                    # добавляем в переменую x значение из переменной row
#         uncompress.append(x)         # добавляем в пустой list(uncompress) значения из переменной х
# print(uncompress)

# dict_ = {'a': ord('a'), 'b': ord('b'), 'c': ord('c')}
# dict_ord = {value: key for key, value in dict_.items()}   # поменять местами ключ и значение 
# print(dict_ord)

# dict_ = {'a': {'a': ord('a')}, 'b': {'b': ord('b')}, 'c': {'c': ord('c')}}
# new_dict = {}
# for key, value in dict_.items():
#     new_dict[key] = value[key]
# print(new_dict)
# for key, value in dict_.items():
#     dict_[key] = value[key]
# print(dict_)

# dict_ = {'a': {'a': ord('a')}, 'b': {'b': ord('b')}, 'c': {'c': ord('c')}}
# new_dict = {key: value[key] for key, value in dict_.items()}
# print(dict_)

# dict_ = {1: 1, 2: 2, 3: 3}
# dict_ = {key: list(range(1, value + 1)) for key, value in dict_.items()}
# print(dict_)

# dict_ = {1: 1, 2: 2, 3: 3}
# dict_ = {key: str(list(range(1, value + 1))).replace('[', '').replace(']', '') for key, value in dict_.items()}
# print(dict_)










