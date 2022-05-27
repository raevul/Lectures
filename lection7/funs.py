""" Functions Функции """
# def = define

""" Синтаксис функции """
# ключевое слово def после имя функции (по желаннию имя должно быть глаголом):

# def add():
#     num1 = 15
#     num2 = 20
#     res = num1 + num2
#     return res
# print(add())

# db = []
# def save(data):
#     db.append(data)
# save({'key': 15})
# save({'key1': 20})
# save({'key2': 35})
# print(db)

# def swapcase_str(string):
#     if string.islower():
#         return string.upper()
#     else:
#         return string.lower()

# res = swapcase_str('HELLO')
# print(res)

# def check_add_email(email):
#     full_email = ""
#     if '@' not in email:
#         full_email = email + '@gmail.com'
#         return full_email
#     return email

# res1 = check_add_email('test1')
# res2 = check_add_email('test1@gmail.com')
# print('First: ', res1)
# print('Second: ', res2)


# def get_even_nums(num):
#     even_nums = []
#     for x in range(1, num):
#         if x % 2 == 0:
#             even_nums.append(x)
#         else:
#             continue
#     return even_nums

# res1 = get_even_nums(10)
# res2 = get_even_nums(5)
# res3 = get_even_nums(15)

# print('First: ', res1)
# print('Second: ', res2)
# print('Third: ', res3)

# db_users = ['John', 'Jessica', 'Peter', 'Raychel']

# def login_required(username):
#     if username not in db_users:
#         print('Вы не вошли в аккаунт!')
#         username = input('Логин: ')
#         return login_required(username)
# db_users = ['John', 'Jessica', 'Peter', 'Raychel']

# def login_required(username):
#     if username not in db_users:
#         print('Вы не вошли в аккаунт!')
#         username = input('Логин: ')
#         return login_required(username)
#     else:
#         return "Вы успешно вошли в аккаунт"

# res = login_required('Aibek')
# print(res)
#     else:
#         return "Вы успешно вошли в аккаунт"

# res = login_required('Aibek')
# print(res)


""" Калькулятор """

# def add(num1, num2):
#     return num1 + num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("You can't divide to zero number!")

# def multiple(num1, num2):
#     return num1 * num2

# def main():
#     try:
#         num1 = int(input('Enter the first number: '))
#         num2 = int(input('Enter the second number: '))
#     except ValueError as Error:
#         print('Error')
#         return main()
#     operator = input('Choose the operator: + - / *: ')
#     res = None
#     if operator == '+':
#         res = add(num1, num2)
#     elif operator == '-':
#         res = substract(num1, num2)
#     elif operator == '/':
#         res = divide(num1, num2)
#     elif operator == '*':
#         res = multiple(num1, num2)
#     else:
#         print("I don't understand your operator symbol!")
#     print(res)
#     question = input("Do you want to continue operator? \nYes or No: ")
#     if question.lower() == "yes":
#         return main()
#     else:
#         return
# main()

"""
Параметры - мы указываем их в начале создании функции внутри скобок 
Аргументы - когда мы  запускаем передаем аргументы вместо параметров

Именованные аргументы - {}
Позиционные аргументы - ()

Мы можем передать в функции неограниченное количество аргументов(ОЗУ) или ограничение мы можем сами сделать
"""
# def generate_name(name):     # параметры
#     #...
#     pass

# generate_name('John')   # аргументы
# def some_func(a, b, c, d):
    
# def some_func(a, b, c, d):
#     print(a, b, c, d)

# some_func(1, 2, 3, 4)

# def some_func(a, b, c, d):
#     print(a, b, c, d)

# some_func(b = 2, d = 4, a = 1, c = 3)

# def add(num1, num2 = 12):           # по умолчанию можно задать в переменную num2 значение
#     print(num1 + num2)

# add(15)


# def some_func(*args, **kwargs):
#     print(args, kwargs)

# some_func(12, 14, 16, a = "hello", b = "world")




# def sum_range(start, end):
#     if start > end:
#         end, start = start, end
#     return sum(range(start, end + 1))

# print(sum_range(2, 2))


# def func(args1, args2 = '1'):
#     print(args1, args2)
# func(args2='1', args1='2')

