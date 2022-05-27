""" Списки (Lists) """
""" Списки упорядоченные, изменяемые коллекции объектов произвольных типов.  Литералы списков --> [] """ 

# способы создания список
# list_1 = []         # Первый вариант
# list_2 = list()     # Второй вариант


""" В списки можно добавлять все типы данных (числа, дробные числа, строки, кортежи, другие списки, словари) """
# list3 = ["hello", 3, 4, 43.23, 2.5, ('1', '2', '3'), {'user': 'Victor'}, [], "", [1, 3, 'world']]


""" К спискам можно обращатся по индексу """
# list4 = ['Hello', 'World']
# print(list4[0])                   # В квадратные скобки пишем индекс

""" Срезы """
# list5 = [1, 2, 3, 4, 'hello']
# print(list5[0:2])                  # Синтаксис среза --> [start:end:step] [начало:конец:шаг]

""" Мытоды список """

""" .append()  --> добавляет объект в конец списка """
# list_ = ['john', 'peter', 'raychel']
# list_.append('david') 
# print(list_)


""" .insert()  --> добавляет объект по указанному индексу синтаксис --> (индекс, объект) (1, 'hello') """
# list_ = ['john', 'peter', 'raychel']
# list_.insert(1, 'david') 
# print(list_)


""" .pop()  --> удаляет и возвращает из списка с указанным элементом """
# list_ = ['john', 'peter', 'raychel']
# list_.pop(-2)              # если не указать индекс то по умолчанию удалится последний из списка
# print(list_)


""" .extend()  --> объеденяет две списки (или складывает(конкатенация)) """
# list1 = ['john', 'peter', 'raychel']
# list2 = ['tom', 'david', 'stark']
# list1.extend(list2)  
# print(list1)

# lis = ['hello'] + ['friend'] + [23]
# print(lis)


""" .remove()  -->  удаляет элемент с переданным значением """
# list_ = ['john', 'peter', 'raychel', 'john']
# list_.remove('john')        # если в списке есть дубликаты то удаляет первый элемент
# print(list_)


""" .copy()  --> копирует список """
# list1 = ['john', 'peter', 'raychel']
# list2 = list1.copy()
# print(list2)


""" .count()  --> возвращает количество элементов с переданным в нем значением """
# list1 = ['john', 'peter', 'raychel', 'john']
# list2 = list1.count('john')
# print(list2)


""" .index()  --> возвращает индекс элемента """
# list1 = ['john', 'peter', 'raychel', 'john']
# list2 = list1.index('john')               # если в списке есть дубликаты то возвращает индекс первого элемента
# print(list2)


""".sort()  --> сортирует список на основе функции """
# list1 = ['john', 'peter', 'raychel', 'john']
# print(list1.sort())                        # если не передать функцию то отсортирует список


""".reverse()  --> возвращает список в обратном порядке т.е переварачивает """
# list1 = ['john', 'peter', 'john', 'raychel']
# list1.reverse()
# print(list1)


""".join()  --> объединяет списки с помощью определенного указателя  " ".join , ",".join """
# list1 = ['Hello', 'world', 'hi', 'bye']
# list2 = ",".join(list1)
# print(list2)


""".clear()  --> полностью очищает список """
# list1 = ['Hello', 'world', 'hi', 'bye']
# list1.clear()
# print(list1)


""" Функции min и max которые возвращают минимальные и максимальные значения в списке """
# list_ = [1, 43, -34, 4, -3, 87]
# print(min(list_))
# print(max(list_))


















