"""
false: 0, "", [], {}, set(), frozenset(), None, false
# logical operators: > < <= >= == !=
"""
# print('makers' > 'bootcamp')
"""ord() - ordinal"""
# print(ord('m'))
"""chr()" - kerecter"""
# print(chr(109))
# print(chr(60))

# print(bool(3.4))
# print(bool(-200))
# print(bool(0))
# print(bool(' '))
# print(bool(""))


# a = 10
# b = 7
# print(a + b > 15) # True
# print(a < 20 - b) # True
# print(a <= b + 3) # True
# print(a != b) # True
# print(a == b) # False

"""coplex log - and, or"""
# a = 10
# b = 15
# print(a > 10 and b < 20)
# print(a >= 10 and b < 20)
# print(a != 10 or b > 20)

"""not"""
# c = 20
# print(not c > 10) 

# a = True
# b = False
# print(not a)
# print(not b)



"""if, elif, else"""
"""
if codition is True:
    come sode 1 
elif condition is True:        # elif --> else if
    some code 3
else:
    some code 2     
"""

# a = 45
# if a > 20:
#     if a > 30:
#         print('a is greater than 30')
#     else:
#         print('a is greater than 30')
# elif a == 20:
#     print('a is equal to 20')
# else:
#     print('a is less than 20')

# a = 5
# b = 20
# if a < b:
#     print('MAKERS')
# else:
#     print('makers')

# a = 10
# b = 5
# c = 20
# if a > b or b < c:
#     print('MAKERS')
# else:
#     print('makers')

# a = 10
# b = 5
# c = 20
# if not (a > b and b > c):
#     print('MAKERS')
# else:
#     print('makers')


# list_ = [11, 42, 64, 59]
# if not 20 in list_:
#     print('YES')
# else:
#     print('NO')

# list_ = [11, 42, 64, 59]
# if not 20 in list_ and 11 in list_:
#     print('True')
# else:
#     print('False')


"""ternary operotor"""
# expression_true if condition else expression_false
""" 
a = True
print(a if True else False)
"""
# a = 'MAKERS'
# b = 10
# print(a if b > 0 else 'makers')
# print(a if b < 0 else 'makers')
# print(a if b else 'makers')       # b = 10(True)

"""alternative ternar operator"""
"""((expression_false, expression_true) [condition])"""
# a = 10
# print(('negative', 'positive')[a > 0])
# print(('negative', 'positive')[a < 0])

"""Nonetype"""  # None
# print(type(None))

# null_variable = None
# not_null_variable = 'MAKERS'

# if null_variable is None:
#     print('This is None')
# else:
#     print('This is not None')

# null_variable = None
# not_null_variable = 'MAKERS'
# if not null_variable is None:
#     print('This is None')
# else:
#     print('This is not None')





"""Operator task 1"""
# number = int(input())
# if number > 0:
#     print('True')
# else:
#     print('False')
"""task2"""
# string = input()
# if (len(string)) > 5:
#     print("True")
# else:
#     print("False")
"""task3"""
# mark = int(input())
# if mark >= 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, Ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif mark >=60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')
"""task4"""
# number = int(input())
# if number < 0:
#     print('negative')
# elif number > 0:
#     print('positive')
# else:
#     print('zero')
"""task5"""
# x = 42
# y = 24
# if x > y:
#     print(y)
# else:
#     print(x)
"""task6"""
# x = 10
# y = 5
# z = 20
# if x > y and z > y:
#     print(y)
# elif z > x and y > x:
#     print(x)
# else:
#     print(z)
"""task7"""
# x = 10
# y = 5
# z = 15
# if x == y == z:
#     print(3)
# elif x == y or y == z or x == z:
#     print(2)
# else:
#     print(0) 
"""task8"""
# x = int(input())
# y = int(input())
# if x % y == 0:
#     print("x делится на y")
#     print("Частное:", x // y)
# else:
#     print("x не делится на y")
#     print("Частное:", x // y)
#     print("Остаток:", x % y)
"""task9"""
    # year = int(input())
    # if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    #     print('YES')
    # else:
    #     print('NO')
"""task10"""
# nums = [1, 15, 36, 88]    
# target = 15
# if target in nums:
#     print('Да')
# else:
#     print('Нет')
"""task11"""
# num = int(input())
# num1 = chr(num)
# if num1.isalpha():
#     print(f'Это буква "{num1}"')
# else:
#     print(f'Это не буква, а символ "{num1}"')


# string - task12
# hashtags = "makers#bootcamp#программирование#it#курсы"
# hashtags2 = hashtags.split('#')
# print(hashtags2)

# from itertools import product

# letters = "ULAR"

# for string in product(letters, repeat=4):
#     s = "".join(string)