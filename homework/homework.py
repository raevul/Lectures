""" вывести элементы из списка которые меньше 5ти """
# list_ = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in list_:
#     if i < 5:
#         print(i)

# через функцию filter
# print(list(filter(lambda i: i < 5, list_)))

# через list comprehesion
# print([i for i in a if i < 5])
""" вернуть список, который состоит из элементов, общих для этих списков """
# list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# list3 = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             list3.append(j)
# print(list3)

# через filter
# print(list(filter(lambda i: i in list2, list1)))

# list comprehesion
# print([i for i in list1 if i in list2])

# оба списка можно привести в множествам и найти их пересечение
# res = list(set(list1) & set(list2))

"""  """


# name = "Ben"
# email = "ben@gmail.com"
# user = name, email
# print(user)

# name = "John"
# email = "john@gmail.com"
# user = name, email
# print(user)

# def user(name, email):
#     return name, email

# print(user("Ben", "ben@gmail.com"))
# print(user("John", "john@gmail.com"))
# print(user("Peter", "peter@gmail.com"))
