"""Dictionary"""

# some_dict = {}
# some_dict = dict()

# names = {"name1": "John", "name2": "Raychel"}
# print(names["name1"])
# print(names["name2"])

# names = {"name1": "John", "name2": "Raychel"}
# names["name3"] = "Peter"
# names["name1"] = "July"
# print(names)

# test_dict = {"key": 1, (1, 2): 2, True: False, 12.5: 3, 12: {1: 2}}
# print(test_dict)

# d = dict(lat = '42.121342', long = "72.4532543")
# print(d)

# d = {}. fromkeys(["a", "b"])
# print(d)

# full_information = {
#     "first_name": "John", "last_name": "Snow"
#     }
# full_information["first_name2"] = "John"
# print(full_information)

# dict_ = {"name": "John", "name": "Raychel"}
# print(dict_["name"])

"""method values()"""
# users = {
#     "username": "coderkg",
#     "email": "bestcodekg@gmail.com",
#     "password": "2001ul",
#     "address": "12 mkr 15",
#     "phone_number": "00708839"
# }
# values_of_dict = list(users.values())
# print(values_of_dict)

"""method keys()"""
# users = {
#     "username": "coderkg",
#     "email": "bestcodekg@gmail.com",
#     "password": "2001ul",
#     "address": "12 mkr 15",
#     "phone_number": "00708839"
# }
# values_of_dict = list(users.keys())
# print(values_of_dict)

# from datetime import datetime
# posts = []
# title = input("Enter title name: ")

# if len(title) >= 225:
#     raise ValueError("Invalid number of characters!")
# elif not title[0].isupper:
#     raise ValueError("Name must start with a capital letter!")

# description = input("Enter description: ")
# hasthags = input("Enter hastag: ")

# for hashtag in hasthags:
#     if not hashtag.startswith("#"):
#         raise ValueError("Wrong hashtag!")

# preview = input("Select photo: ")
# created_at = datetime.now()
# update_at = None
# if len(title) >= 225:
#     raise ValueError("Invalid number of characters!")
# elif not title[0].isupper:
#     raise ValueError("Name must start with a capital letter!")

# post = {
#     "title": title,
#     "description": description,
#     "hasthags": hasthags,
#     "preview": preview,
#     "created_at": created_at,
#     "update_at": update_at
# }
# posts.append(post)
# print(post)

"""method.get()"""
# methods = {
# "method1": "append",
# "mathod2": "insert",
# "mathod3": "pop",
# "mathod4": "reverse",
# "mathod5": "remove"
# }

#                            #return meaning with keys, если токого ключа нет то по умолчанию возвращает None
# res = methods.get("method1")
#    print(methods["method6"])
# print(res)

# """method.item()"""
# methods = {
# "method1": "append",
# "mathod2": "insert",
# "mathod3": "pop",
# "mathod4": "reverse",
# "mathod5": "remove"
# }
# res = list(methods.items())
# print(res)
# print(dict(res))
# for x, y in methods.items():
#     print(x, y)

# a = 15
# b = 20
# a, b = b, a
# print(a, b)
# a = 15
# b = 20
# a = b     # or b = a
# print(a, b)

# methods = {
# "method1": "append",
# "mathod2": "insert",
# "mathod3": "pop",
# "mathod4": "reverse",
# "mathod5": "remove"
# }

# for key, value in methods.items():
#     print(key, value)

"""method.pop()"""
# cars = {
#     "car_1": "Toyota Camry",
#     "car_2": "BMW 525",
#     "car_3": "Merecedes 124",
#     "car_4": "Matiz Daewoo 2010"
# }  
# remove_value = cars.pop("car_5", None)
# print(remove_value)
# print(cars)

username = input("Введите имя: ")
password = input("Введите пароль: ")
password_confirmation = input("Потвердите пароль: ")

db = []

data = {
    "username": username,
    "password": password,
    "password_confirmation": password_confirmation
}

password = data.get("password")
password_confirmation = data.pop("password_confirmation")

if password != password_confirmation:
    raise ValueError(
        "Password and Password confirmation is not match"
        )
db.append(data)
print(db)

"""popitem()"""
# information = {"name": "Raychel", "age": 25}
# removed = information.popitem()
# print(information)
# print(removed)


# profile = {
#     "name": "Raychel",
#     "age": 25,
#     "address": "California",
#     "country": "USA",
#     "money": 2500
# }
# print(profile["address"])
# print(profile.get("address"))
# print(profile.setdefault("address"))                    Get or Create
# profile.setdefault("address1234", "Bishkek")
# print(profile)

"""update()"""
# data = {"key": 1, "key2": 2}
# data.update({"key": 4, "key2": 8})
# print(data)

"""
pop
popitem
keys
setdefault - get or create
valiues
items
copy 
get
clear
update
fromkeys
"""

"""while"""

# count = 1
# while count <= 20:
#     print("hello", count)
#     count += 1

# count = 20
# while count >= 1:
#     print("hello", count)
#     count -= 1

# psw = "Hello world"
# count = 1
# while True:
#     o_psw = input("Введите пароль: ")
#     if o_psw == psw:
#         print("Вы вошли в систему")
#         break
#     print(f"У вас осталось {6 - count} попыток")
#     count += 1

# for x in range(1, 100):
#     if x % 2 == 0:
#         continue
#     print(x)
# for x in range(1, 100):
#     if x % 2 == 0:
#         break
#     print(x)
# for x in range(1, 100):
#     if x % 2 == 0:
#         print(x)


"""
Dict comprehension
List comprehension
Set comprehension
"""

"""task10"""
# a = {'a': 1, 'b': 2, 'c': None}
# for i, x in list(a.items()):
#     if x == None:
#         del a[i]
#     else:
#         continue
# print(a)
"""task11"""
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for i, x in a.items():
#     a[i] = x / 5
# print(a)
"""task12"""
# a = {'a': 5, 'b': 3, 'c': 2}
# for i, x in list(a.items()):
#     if x % 2 == 0:
#         del a[i]
#     else:
#         continue
# print(a)
"""OR"""
# a = {'a': 5, 'b': 3, 'c': 2}
# for i, x in list(a.items()):
#     if x % 2 == 0:
#         del a[i]
# print(a)

"""task13"""
# a = {'apple': 0.4, 'orange': 0.35, 'banana': 0.25}
# inverse_dict = {}
# for key, value in a.items():
#     inverse_dict[value] = key
# print(inverse_dict)

