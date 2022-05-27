"""
r -> read - режим только для чтения
r+ -> read + write - мы можем открыть файл как и для чтения так и для записи
w -> write - этот режим позволяет открывать файл только для записи нельзя считывать данные но можно записывать
w+ -> read + write - мы можем открыть файл как и для чтения так и для записи
a -> append - его отличия от w в том что он дозаписывает данные в файл который создали, а режим w открывает файл в режиме записи если файл существует то его содержимое удаляется, а если он не существует то создается новый
a+ -> append + read - этот режим позволяет дозаписывать и считывать от туда данные
x -> wirte - этот режим тоже позволяет записывать данные в файл, но его отличия от w в том что он открыт для записи только в том случае если файла нет, если файла не существует то он появляется и сразу записывается в него данные, но если этот файл есть то генерируется исключение
b -> binary - открытие файла в двоичном режиме 
t -> text - открытие файла в текстовом режиме (txt)
rt -> открывает файл в режиме чтения в текстовом режиме (по умолчанию)
rt -> r - по умолчанию
rb -> открывает файл в режиме чтения в двоичном режиме (это не исп по умолчанию)
rb -> rb - по умолчанию
"""


""" чтобы прочитать что написано в makers2.txt (или в любом другом файле который не находиться в текущей директории) нужно указать абсолютный путь """
# file1 = open('/home/hello/bootcamp/files/makers2.txt', 'r')  
# print(file1.read())

# file1 = open('makers.txt', 'r')  
# data = file1.read(3)
# print(data)

""" read """
""" в read ->  можно ввести аргумент (число), если ввести число 3 то он возвратит первые 3 символа"""
# file1 = open('makers.txt', 'r')  
# print(file1.read(10))            # выводит первые 10 символов
# print(file1.read(10))            # выводит 10 символом после выведенных 10 символов



""" seek - возвращает курсор в начало если передать в него 0 (вместо 0 можно указать любую позицию) """
# file1 = open('makers.txt', 'r')  
# print(file1.read(10))
# file1.seek(3)         
# print(file1.read(5))     # выводит символы после поставленной позиции, если указать 3 то он выведет символы после 3 символа        

# file1 = open('makers.txt', 'r')  
# print(file1.read(10))
# file1.seek(3)         
# print(file1.read(5))
# file1.seek(10) 
# print(file1.read())     
# print(file1.read(10)) 
# print(file1.read()) 
# print(file1.read(6)) 


""" readline """
""" readline -> построчно возвращает данные из файла """
# file1 = open('makers.txt', 'r')
# print(file1.readline())           # выводит первую строку
# print(file1.readline())

# file1 = open('makers.txt', 'r')
# for line in file1:
#     print(line)

""" reaslines """
""" readlines - считывает данные(строки) файла в список """
# file1 = open('makers.txt', 'r')
# list_ = file1.readlines()
# print(list_)

# file1 = open('makers.txt', 'r')
# list_ = file1.readlines()
# for line in list_:
#     print(line)

# file1 = open('makers.txt', 'r')
# list_ = file1.readlines()
# list_ = [line.replace('\n', '') for line in list_]
# print(list_)




""" w - write"""
file2 = open('bootcamp.txt', 'w')           
print(file2.write("It's such a beautiful day today a"))                        # write - принимает строку




