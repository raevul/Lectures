# or, and, is, in, not , in, not

# names = ['John', 'Peter', 'Raychel']
# # names[0]
# # DRY - Don't repeat youself
# name1 = names[0].capitalize()
# name2 = names[1].capitalize()
# name3 = names[2].capitalize()
# new_names = []
# new_names.append(name1)
# new_names.append(name2)
# new_names.append(name3)
# print(new_names)
# names = ["john", "peter", "raychel"]
# i = None
# range(start, end, step)
# for i in range(0, 100):       
#     print(i)
# for i in range(100, 0, -1):
#     print(i)
# for n in range(1, 100):
#     print(f"{n} + 1 = {n + 1}")

# names = ["john", "peter", "raychel"]
# new_names = []

# for name in names:
#     new_names.append(name.capitalize())

# print(new_names)

# pizza = [
#     "first_item", "second_item", "third_item",
#     "fourth_item", "fifth_item", "sixth_item"
# ]

# for item in pizza:
#     print(f"Before eating piece: {pizza}")      # or print("Before eating piece: ", pizza)
#     print(f"Eating {item} piece")              
#     pizza.pop()
#     print(f"After eating piece: {pizza}")       # or print("After eating piece: ", pizza)

#  for item in pizza:
#     print(f"Before eating piece: {pizza}")      # or print("Before eating piece: ", pizza)
#     print(f"Eating {item} piece")              
#     print(f"After eating piece: {pizza}")       # or print("After eating piece: ", pizza)
# pizza.clear()
# print(pizza)


"""
fizz - 1 - нечетное
buzz - 2 - четное
fizzbuzz
"""
# 3 / 3 == fizz
# 5 / 5 == buzz
# 15 / 3 and 15 / 5 == fizzbuzz


# for x in range(1, 100):
#     if x % 3 == 0 and x % 5 == 0:
#         print(f"{x} --> fizz buzz")
#     elif x % 3 == 0:
#         print(f"{x} --> fizz")
#     elif x % 5 == 0:
#         print(f"{x} --> buzz") 


"""for x in []:
for x in "hello":
for x in range():
"""
# phone_numbers = [777, 999, 666, 888, 111, 222, 777, 888, 999]
# unique_numbers = []
# for x in phone_numbers:
#     if x not in unique_numbers:
#         unique_numbers.append(x)
#     else:
#         continue
# print(unique_numbers)

# phone_numbers = [777, 999, 666, 888, 111, 222, 777, 888, 999]
# unique_numbers = list(set(phone_numbers))
# print(unique_numbers)

"""
mutable(изменяемые) - list, dict, set
immutable(неизменяемые) - int, str, tuple, bool, float, frozenset,
"""
# str_ = "hello world"
# new = str_ + "hello"
# print(new)
# print(str_)

# tuple_ = ("john", "peter", [])
# tuple_[2].append("hello")
# print(tuple_)


# tuple_ = ("john", "raychel", "john")
# # print(dir(tuple_))
# print(tuple_.count("john"))
# print(tuple_.index("raychel"))

"""
numbers(int, float) - immutable
str - immutable
tuple () - immtable
list [] - mutable
bool - immutable
NoneType - immutable
set {} - mutable 
"""


"""creating set"""
# numbers = set()
# names = {"john", "raychel", "peter", "jason"}
# # print(dir(names))
# for x in names:
#     print(x)
"""method - add"""
# month = {
# "Jan", "Feb", "March",
# "Apr", "May", "July",
# "Aug", "Sep", "Oct", 
# "Nov", "Dec"
# }
# month.add("June")
# print(month)
"""method discard, remove"""
# laptops = {"Acer", "Mac", "Asus", "Hp"}
# laptops.discard("Acer")
# print(laptops)
# laptops.discard("Acer")
# print(laptops)
# laptops.remove("Acer")
# print(laptops)
"""pop"""
# laptops = {"Acer", "Mac", "Asus", "Hp"}
# removed = laptops.pop()
# print(removed)

"""method union() or ( | )"""
# language_a = {"Python", "JavaScript"}
# language_b = {"PHP", "Java", "C#"}
# all_languages = language_a.union(language_b)
# print(all_languages)

# framework_a = {"Django", "Fkask", "FastApi"}
# framework_b = {"aioHttp", "Pyside", "PyQT"}
# all_frameworks = framework_a | framework_b
# print(all_frameworks)

# x = {1, 3, 3}
# y = {4, 5, 6}
# z = {10, 11, 12}
# data = x.union(y, z)
# print(data)

# x = {1, 3, 3}
# y = {4, 5, 6}
# z = {10, 11, 12}
# data = x | y | z
# print(data)

"""intersection() or ( & )"""
# libraries_a = {"requests", "bs4", "python-decouple"}
# libraries_b = {"jinja", "json", "celery"}
# intersections_ = libraries_a.intersection(libraries_b)
# print(intersections_)

# libraries_a = {"requests", "bs4", "python-decouple", "unitest"}
# libraries_b = {"jinja", "bs4", "celery", "unitest"}
# intersections_ = libraries_a.intersection(libraries_b)
# print(intersections_)

# a = {1, 2, 3, 4}
# b = {2, 5, 4, 6}
# c = {10, 11, 12, 2}
# z = a & b & c
# print(z)

# a = {1, 2, 3, 4}
# b = {2, 5, 4, 6}
# c = {10, 11, 12, 2}
# z = a.intersection(b, c)
# print(z)

"""difference() or ( - )"""
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# difference_of_set = set_a.difference(set_b)
# print(difference_of_set)

# tehnologies_a = {"chrome", "mozilla", "pycharm"}
# tehnologies_b = {"vscode", "facebook", "nano", "pycharm"}
# diff = tehnologies_a - tehnologies_b
# print(diff)

"""symmetric_difference() or ( ^ )"""
# laptop_a = {"Dell", "Hp", "Acer"}
# laptop_b = {"Mac", "Lenovo", "Asus", "Acer"}
# sym_diff = laptop_a.symmetric_difference(laptop_b)
# print(sym_diff)

# laptop_a = {"Dell", "Hp", "Acer"}
# laptop_b = {"Mac", "Lenovo", "Asus", "Acer"}
# sym_diff = laptop_a ^ laptop_b
# print(sym_diff)

"""issubset() or ( <= ), issuperset() or ( >= )"""
# set_1 = {"a", "b", "c"}
# set_2 = {"a", "b", "c", "d", "e"}
# subset_check = set_1 <= set_2
# superset_check = set_2 >= set_1
# print(subset_check)
# print(superset_check)

# sentence_student = {"I", "am", "Python"}
# sentence_original = {"I", "am", "Python", "Developer"}
# res = sentence_original.issuperset(sentence_student)
# print('Подмножество!')
# a = {1, 2, 3, 4 ,5}
# b = {4, 5, 6, 7, 8}
# res = b.issuperset(a)
# print('Подмножество!')
"""frozenset()"""
# frozen_ = frozenset({1, 2, 3, 4})
# print(frozen_)

"""task13(set)"""
# robert = {101, 73, 11, 51, 282}
# kail = {8, 11, 14, 52, 22} 
# merri = {192, 32, 101, 11, 20}
# if kail.intersection(robert):
#     print("kail merri")
# elif merri.intersection(robert):
#     print("merri")
# else:
#     print('no one')
#################################
# robert = {101, 73, 11, 51, 282}
# kail = {8, 11, 14, 52, 22} 
# merri = {192, 32, 101, 11, 20}
# if robert & kail and robert & merri:
#     print("kail merri")
# elif robert & kail:
#     print("kail")
# elif robert & merri:
#     print("merri")
# else:
#     print("no one")
"""task14"""
# tilek = {"Dodo", "ImperiaPizza", "FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", "KFC"}
# elina = {"Dodo", "ImperiaPizza", "FreshBox", "OchakKebab", "KFC"}
# print(tilek.intersection(timur,alexander,elina))
##############################################
# tilek = {"Dodo", "ImperiaPizza", "FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", "KFC"}
# elina = {}
# for res in set(tilek & timur & alexander):
#     print(res)
"""task15"""
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.add("помидор")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.discard("сыр чеддар")
# ingredients.add("сыр моцарелла")
# print(ingredients)
"""extra task1"""
# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# for ind, set_ in enumerate(a):
#     if inp2 - 1 == ind:
#         set_.add(inp1)
#     else:
#         set_.add("default value")
# print(a)

