"""
strings  (строки)
strings methods  (методы строк)
""" 
# .upper() --> преобразует все символы в верхний регистр
"""
name = "Jonh"
name.upper
print (name)
# first_name = input("type your name: ")
# new = first_name.upper()
# print (new)
"""
# .lower() --> преобразует все символы в нижний регистр
"""
name = "Jonh"
name.lower
print (name)
# first_name = input("type your name: ")
# new = first_name.lower()
# print (new)
"""
# .swapcase() --> меняет регистры в протиположный регистр (верхний регистр в нижний, а нижний в верхний)
# .capitalize() --> преобразует первый символ строки в верхий регистр а остальные в нижний
# .title() --> первую букву каждого слова переводит в верхний регистр, а остальные в нижний
# .find(str, [start, end]) --> поиск подстороки в строке, возвращает номер первого вхождения или -1
# .rfind(str, [start],[end]) - поиск подстроки в строке, возвращает номер последнего вхождения или -1
# .startswith(str) --> начинается ли строка с шаблона str
# .endswith(str) --> заканчивается ли строка шаблоном str
# .replace(шаблон, замена) --> заменяет шаблон
# .index(str, [start, end]) --> поиск подстроки в строке по индексу, возвращает номер первого вхождения или вызывет ValueError
# .rindex(str, [start, end]) --> поиск подстроки в строке по индексу, возвращает номер последнего вхождения или вызывет ValueError
# .strip([chars]) --> возвращает копию строки, в которой все сиволы удалены с начала и с конца (по умол этот символ "пробел")
# .rstrip() --> удаляет все символы справа
# .lstrip() --> удаляет все символы слева
# .split(символ) --> разбиение строки по разделителю
# .join("") --> разделяет строки через указанный символ 
# .isascii() --> проверяет символов строки на вхождение в таблицу ASCII, метод вернет True если все символы строки входят в ASCII
# .
# .

# .isdigit() --> проверяет состоит ли строка только из цифр (пробел или др сиволы не считаются)
# .isalpha() --> проверяет состоит ли строка только из букв (пробел или др сиволы не считаются)
# .isalnum() --> проверяет состоит ли строка только из цифр и букв (пробел или др сиволы не считаются)
# .islower() --> проверяет состоит ли строка из символов в нижнем регистре
# .isupper() --> проверяет состоит ли строка из символов в верхнем регистре
# .isspace() --> проверяет состоит ли строка из неотображаемых символов (пробелов, табуляции)
# .istitle() --> проверяет начинается ли строка с заглавной буквы

# dir --> methods   

# salam = "SALAM 312"
# print(type(salam))

# hello = 'Hello world !'
# print(type(hello))

# var = 'I don\'t know'
# print(var)
# var1 = """
# Janna d'Ark "hello world"
# """
# print(var1)
# var2 = "Janna d'Ark \"hello world\""
# print(var2)


# srting interpolation    # форматирование строк
"""metods (есть 3 метода форматирования)
1. %s
2. {}
3. f{}
""" 


# player_1 = 150
# message = 'Player1: %s points'
# result = message % player_1
# print(result) 


# in_the_botton = "Who lives at the bottom of ocean?"
# yellow = "Yellow sponge, child without flaw"
# always_wins = "Who wins always and every where?"
# as_fish = "Who is as agile as a fish in water?"

# stronge_bob = "%s --> Stronge Bob Squere Pains"
# print(stronge_bob % in_the_botton)
# print(stronge_bob % yellow)
# print(stronge_bob % always_wins)
# print(stronge_bob % as_fish)

# result = "I'm programmer. I know %s, i learn now %s"
# print(result % ('python', 'javascript'))

# result = "I'm programmer. I know %s, i learn now %s"
# langs = ('python', 'javascript')
# print(result % langs)


# result = "I'm programmer {0}. I know {2}, i learn now {1}"
# message = result.format('Senior', 'Python', 'Java')
# print(message)


# result = "I'm programmer {level}. I know {f_lang}, i learn now {s_lang}"
# message = result.format(f_lang= "Python", s_lang= "Java", level= "Senior")
# print(message)

# name = "Jonh"
# last_name = "Snow"
# hello = f"{name} {last_name} -- the best actor"
# print(hello)

# title = "Hello"
# last_title = "World"
# res = title + " " + last_title
# print(res)

# country = "Kyrgystan \n"
# print (country * 5)

# my_country = "Kyrgystan"
# print(len(my_country))
