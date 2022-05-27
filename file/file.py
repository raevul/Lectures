
# labels = ['Mercedes-Benz', 'Honda', 'Audi']
# for i in labels:
#     print("I like brand", i)

# list_ = ['world', 'hello']
# new_list = list_.reverse()
# print(new_list)

# suitcase = []
# suitcase.append('футболка')   
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)
"""task6"""
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for i in nums:
#     if i < 5:
#         res.append(i)
# print(res)


# num = input().split(",") 
# list_ = num
# tuple_ = tuple(num)
# print(list_)
# print(tuple_)

# list_ = [1, 2, 3, 4, 5]
# new_list = str(list_)
# print(new_list)

"""task11"""
# list_ = list(range(0, 101, 2))
# print(list_)

"""task3"""
# name_of_list = ['Helloworld!'] 
# if len(name_of_list[0]) % 2 == 0:
#     name = len(name_of_list[0])/2
#     print(list(name_of_list[0][int(name):]+name_of_list[0][:int(name)]))
# else:
#     name = len(name_of_list[0])//2+1
#     print(list(name_of_list[0][name:]+name_of_list[0][:name]))
"""task3"""
# name_of_list = ['Helloworld!'] 
# middle = int(len(name_of_list[0])/2)
# if len(name_of_list[0]) % 2 != 0:
#     middle += 1 

# print(list(name_of_list[0][middle:] + name_of_list[0][:middle]))
"""task4"""
# list_ = ['world', 'hello']
# new_list = list_.copy()
# new_list.reverse()
# print(new_list)
"""task8"""
# list_ = [1, 2, 3, 4, 5]
# new_list = [str(x) for x in list_]
# print(new_list)   

# list_ = [1,2,3,4,5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)
"""task12"""
# list1 = [1, 2, 3, 3, 5]
# list2 = [2, 4, 5, 6, 8] 
# sum_ = list1 + list2
# print(sum(list1 + list2))

# list1 = [1, 2, 3, 3, 5]
# list2 = [2, 4, 5, 6, 8] 
# print(sum(list1 + list2))

# list1 = [1, 2, 3, 3, 5]
# list2 = [2, 4, 5, 6, 8] 
# list3 = list1 + list2
# sum_ = 0
# for i in list3:
#     sum_ = sum_ + i
# print(sum_)
"""task7"""
# user = input()
# a = user.split(',')
# list_ = a
# tuple_ = tuple(a)
# print(list_)
# print(tuple_)
"""task9"""
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for num in list_:
#     if not num // num == 0 and num % 2 == 0:
#         new_list.append(str('четное'))
#     else:
#         new_list.append(str('нечетное'))
# print(new_list)

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)
"""task10"""
# list_ = list(range(20))
# print(list_)

"""task13"""
# nums = input().split(',')
# list_ = []
# for x in nums:
#     list_.append(x)
# list_.sort()
# print(list_)
"""task14"""
# list_ = [1, 2, 3]

# for i in list_:
#     if i in list_:
#         print('yes')
#     else:
#         print("ERROR")

"""task15"""
# list_ = list(range(54, 9184))
# new_list = []
# for i in list_:
#     if i % 5 == 0:
#         new_list.append(i)
# print(new_list)

# for i in range(1, 10):
#     i -= 5
# print(i)



# import math
# r = int(input('Введите радиус круга: '))
# s = int(input('Введите длина круга: '))
# pi = math.pi
# res = round((pi * r ** 2),2)
# res2 = round((2 * pi * r),2)
# print('Площадь круга составляет: ', res)
# print('Длина круга составляет ', res2)

# num6 = int(input("Введите радиус круга: "))
# num7 = 3.14159
# result1 = round(num7 * (num6 * num6),2)
# result2 = round((2 * (num6 * num7)),2)
# print ("Площадь круга составляет: ", result1, "Длина круга составляет: ", result2)
