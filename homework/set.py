""" Множества (Sets) """
""" Множества - это неупорядоченная коллекция уникальных элементов. Литералы --> {} """
""" Элементы множества неизменяемы т.е являются уникальными, одноко само по себе множество является изменяемым """
""" Так как элементы не индексируются, множества не поддерживают никаких операций среза и индексирования """
# Способы создания множеств
# set_ = set()
# set_ = {'a', 1, 'b', 2}
# set_ = set([1, 3, 2, 0, 2])

""" Элементами множества могут быть неизменяемые типы данных (числа, строки, кортежи, булевые значения) """
# set_ = {"hello", 3, 4, 43.23, 2.5, ('1', '2', '3')}

""" способы создания """
# set_ = set([1, 3, 2, 0, 2, 3])
# print(set_)

# cities = ["New-York", "Chikago", "Washington", "Barcelona", "New-York", "Washington"]
# print(set(cities))
"""преобразуем множество в список"""
# print(list(set(cities)))

""" Методы множеств """


""" .add()  --> добавляет новый элемент во множество (add - добавляет только один элемент) """
# set_ = set()
# set_.add(7)
# print(set_)


""" .update  --> добавляет сразу несколько элементов """
# set_ = set()
# set_.update([7, 'a', (1, 2)])
# print(set_)


""" .discard()  --> удаляет элемент """
# set_ = set([7, 2, 3, 'a', (1, 2)])
# set_.discard(7)                       # если ввести не существующий объект то discard не выведет ошибки а remove выведет ошибку
# print(set_)


""" .remove() --> удаляет элемент """
# set_ = set([7, 2, 3, 'a', (1, 2)])
# set_.remove(7)
# print(set_)



""".pop()  --> удаляет и возвращает элемент """
# set_ = set([7, 2, 3, 'a', (1, 2)])
# set2 = set_.pop()         
# print(set2)


""" .clear()  --> очищает множество """
# set_ = set([7, 2, 3, 'a', (1, 2)])
# set_.clear()
# print(set_)



""" Операции над множествами """

""" .intersection() или ( & ) --> Пересечение двух множеств """
# возвращает одинаковые значения 
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.intersection(set2)
# set1.intersection_update(set2)            # сохраняет элементы в set1 
# set3 = set1 & set2                        # создает новое множество
# print(set3)


""" .union() или ( | ) --> Объединение двух множеств при этом исходные множества не изменяются """
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.union(set2)
# set3 = set1 | set2       # создает новое множество
# print(set3)


""" .difference() или ( - )  --> Вычитание множеств (разность) """
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.difference(set2)
# set3 = set1 - set2
# set4 = set2 - set1
# print(set3)
# print(set4)


""" .symmetric_difference() или ( ^ ) -->  симметрическая разность """
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.symmetric_difference(set2)
# set3 = set1 ^ set2
# print(set3)



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


""" сравнение множеств """
# set1 = {7, 6, 5, 4, 3}
# set2 = {3, 4, 5, 6, 7}
# set3 = set1 == set2
# print(set3)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = set1 > set2
# print(set3)

# set1 = {7, 6, 5, 4, 3}
# set2 = {3, 4, 5}
# set3 = set1 > set2
# print(set3)

# set1 = {7, 6, 5, 4, 3}
# set2 = {3, 4, 5}
# set3 = set1 < set2
# print(set3)









