# инициализация это создать
# DRY - Don't repeat youself - не повторайся

# def name_of_func(param1, param2):
#     print(param1 + param2)
#     return "Returned"

# print(name_of_func(4, 5))


# def name_of_func(param1, param2):
#     print(param1 + param2)
#     return "Returned"

# res = print(5)
# print(res)


# def name_of_func(param1, param2):
#     print(param1 + param2)
#     return param1 + param2

# name_of_func(4, 5)

# def name_of_func(param1, param2):
#     print(param1 + param2)
#     return param1 - param2

# res = name_of_func(5, 4)
# print(res)

# def add(num1, num2):
#     return num1 + num2

# print(add(5, 4))


# def divide(num1, num2):
#     if num2 == 0:
#         print('Error')
#     return num1 / num2

# print(divide(5, 3))

# def divide(num1, num2):
#     if num2 == 0:
#         print('Error')
#     return num1 / num2

# print(divide(num2 = 5,num1 = 10))


""" *args and **kwargs """

# def func(*numbers, **users):
#     print(f"args: {numbers}")
#     print(f"kwargs: {users}")

# func(2, 43, 5, 6, 4, key1 = "value1", key2 = "value2")


# def say_hello(age, name = 'Anonim'):
#     print(f"Hello, {name}! You are {age} y.o")

# say_hello(20)

# def say_hello(*users):
#     for user in users:
#         print(user)
#         print(f"Hello, {user[0]}! You are {user[1]} y.o")

# say_hello(["Nastya", 14], ["Atai", 25], ["Nuraiym", 10])

# database = {
#     "Nastya": "12344567",
#     "Atai": "qwerty",
#     "Nuraiym": "98776655",
#     "Hasan": "hello"
# }

# def login(**data):
#     user = data.get("username")                               # .get - вызываем по ключу
#     passw = data["password"]
#     if user in database:
#         if passw == database[user]:
#             print("You logged in")
#         else:
#             print("Incorrect password")
#     else:
#         print('Incorrect username')

# login(username = "Hasan", password = "grfd")


# string = input("Enter: ").lower()

# def translate(string):
#     eng = "qwertyuiopasdfghjklzxcvbnm"
#     ru = "йцукенгшщзхъфывапролджэячсмитьбю"
#     if string[0] in eng:
#         transtab = (str.maketrans(eng, ru))
#     else: 
#         transtab = str.maketrans(ru, eng)
#     return string.translate(transtab)

# print(translate(string))


# string = input("Enter: ").lower()

# def translate(string):
#     eng = "qwertyuiopasdfghjklzxcvbnm"
#     ru = "йцукенгшщзхъфывапролджэячсмитьбю"
#     if string[0] in eng:
#         transtab = (str.maketrans(eng, ru))
#     else: 
#         transtab = str.maketrans(ru, eng)
#     return string.translate(transtab)

# print(translate(string))



# def nums(num1, num2):
#     print(num1 * num2)
#     print(num1 + num2)
#     if num1 < num2:
#         print('Делимое число не может мыть больше делителя числа')
#     else:
#         print(num1 / num2)

# nums(15, 20)








