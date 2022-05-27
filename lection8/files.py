"""r - открытие для чтения файла"""
""" w - открывать и записывать данные в файл, перезаписывает данные """
""" x - открывает и записывает данные, если вдруг не находит файл, то он вытаскивает исключение """
""" a - открывает и записывает данные, если в файле существует уже данные, то он добавляет в конец файла """
""" b - открывает в двоичном режиме """
""" t - открывает только в текстовом режиме """
""" + ->  открывает и чтение и запись """

# file_ = open('text.txt', 'r')
# print(file_)
# print(file_.read())
# print(file_.readable())
# NAME_OF_FILE = "info.txt"
# name = input("Введите имя: ")
# address = input("Введите адрес: ")
# email = input("Введите почту: ")
# phone_number = input("Введите номер телефона: ")
# description = input("Введите текст: ")
# file_ = open(NAME_OF_FILE, 'rb')

# file_.write(
#     f'\n{name}\n{address}\n{email}\n{phone_number}\n{description}\n'
#     )
# file_.write("-"*100)

# from pprint import pprint
# dict_ = dict.fromkeys(['x for x in range(1, 20)'])
# pprint(dict_)

# from pprint import pprint
# import json

# dict_ = {
#     'str': "hello world", 
#     'int': 123,
#     'bool': True,
#     'float': 23.42, 
#     "list": [1, 2, 3], 
#     'tuple': (1, 2, 3),
#     "dict": {"a": 1, "b": 2},   
# }
# json_file = open('test.json', 'a')

# методы - load, dump, loads, dumps
# сериализация - перевод с python в json (dump, dumps)
# десериализация - перевод с json в python (load, loads)

# json_str = json.dumps(dict_)
# json_file.write(json_str)
# json_file.close()

# file_.close()


# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write("""\nИ снова седая ночь,
# И только ей доверяю я.
# Знаешь седая ночь,
# Ты все мои тайны.
# Но даже и ты помочь
# Не можешь, и темнота твоя
# Мне одному совсем,
# совсем ни к чему.""")


"""check youself"""
# with open("test.txt", "r") as file:
#     line_count = 0
#     for stroka in file:
#         line_count +=1
#         print(f"символов в {line_count} строке: {len(stroka)-1}")
#         splitted = stroka.split()
#         print(f"слов в {line_count} строке: {len(splitted)}")
# print("Всего строк в файле:",line_count)


"""task4"""
# with open('task4.txt') as file:
#     count = 0
#     for f in file:
#         count += 1
# print(count)

with open('task5.txt', 'r') as file:
    file1 = min(file)
    file2 = max(file)
    
with open('task6.txt', 'a') as f:
    f.write(file1, file2)






