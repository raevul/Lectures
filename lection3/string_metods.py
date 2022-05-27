# language = "Python3"
# print(language[0])
# print(language[-1])

"""slice"""

# new_flavor = "New Birth Cake"
# result = new_flavor [0:3]
# result = new_flavor [10:]
# result = new_flavor [-5:]
# print(result)
# new_flavor = "birthday"
# result = new_flavor [0:3]
# result = new_flavor [-3:]
# print(result)
"""start:end:step"""
# car = "lamborgini"
# print (car[0::2])  #[0:(-1) or (10) :2]
# print (car[::])
# print (car[0:-1:2])
# print (car[0:10:2])
# print (car[0::3])


# polindrom_word = input ("Enter word: ").lower()
# if polindrom_word == polindrom_word[::-1]:
#     print(f"Yes! {polindrom_word} is an polindrom")
# else:
#     print(f"No! {polindrom_word} is not polindrom")


"""find"""
text = "url of the site: https://boometang.kg "
# fragment_start_index = text.find("http")
# print(fragment_start_index)
# fragment_end = text.find(" ", fragment_start_index)
# print(fragment_end)
# full_url = text[fragment_start_index:fragment_end]
# print(full_url)

# text = "hello wait world"
# res = text.find('w', 7, 15)
# print(text.find("w"))
# print(res)

"""rfind --> reverce find"""
# city = "Bishkek"
# index_of_last_k = city.rfind("k")
# print(index_of_last_k)

"""index"""
# city = "New York"
# print(city.index("k"))
# print(city.index("B"))

"""rindex"""
# city = "Bishkek"
# print(city.rindex("k"))
# print(city.rindex("a"))

"""replace"""
# city = "Bishkek"
# print(city.replace("k", "K"))        #  "k" --> "K"

"""split"""
# string = "totoro"
# res = string.split("o")      #  "o" --> ""
# print (res)

# list = [x for x in res if x]
# print(list)

# _env = "127.0.0.1,localhost,boomerang.kg"
# allowed_hosts = _env.split(",")
# print(allowed_hosts)


"""isdigit"""
# var = "hello 312"
# print (var.isdigit())

"""isaplha"""
# name = "John 1"
# print (name.isalpha())

"""isalnum"""
# num_str = "John23"
# print(num_str.isalnum())

"""islower"""
# str = "python"
# print(str.islower())

"""isupper"""
# str = "PYTHON"
# print(str.isupper())

"""istitle"""
# str = "Python"
# print(str.istitle())

"""
upper - "no" --> "NO"
lower - "YES" --> "yes"
title - "hello python" --> "Hello Python"
capitalize - "hello makers" --> "Hello makers"
swapcase - "Hello Python" --> "hELLO pYTHON"
startswith(str) - "s" anding str
endswith(str) - "S" anding str 
"""

# google_mail = input("type gmail: ")
# if google_mail.endswith("@gmail.com"):
#     print("Successfully saved gmail")
# else: 
#     print("Error, we take only gamil accounts, please check it")

"""join"""
# my_tuple = ("John", "Raychel", "Peter", "Vicky")
# new_string = "###".join(my_tuple)
# print(new_string)

# dir_name = ["home", "bootcamp","lection3"]
# new_string = "/".join(dir_name)
# print(new_string)

"""
strip
lstrip
rstrip
"""
# name = "    hello world"     # lstrip
# print(name.lstrip())

# new = "hello           "
# print(new.rstrip())          # rstip

# var = "hello         world"
# print(var.replace(" ",""))   #replace


# string = "Danger"
# letter = string[len(string)//2]
# print(letter)  
# name = 'Python'
# version = '3'
# result = '{} - {}, {}.'.format(name[0], name, version)
# print(result)
