# word = input().lower()

# ru = 'б,в,г,д,ж,з,к,л,м,н,п,р,с,т,ф,х,ц,ч,ш,щ,а,е,ё,и,о,у,ы,э,ю,я,й,ъ'

# if word == "hello" or word == "Привет" or word == "hi":
#     print(word)
# elif word == 'bye' or word == 'до свидания':
#     print(word)
# else:
#     if word[0] in ru:
#        print("неожиданное слово")
#     else:
#         print("unexpected word")

# num = 5

# if num < 10 and num > 3:
#     print("< 10 and > 3")
# if num < 0:
#     print(" < 0")
# if num > 10:
#     print("> 10")

# string = input()
# banned = ['world', 'bootcamp']
# if banned[0] in string:
#     string = string.replace(banned[0], '*' * len(banned[0]))
# if banned[1] in string:
#     string = string.replace(banned[1], '*' * len(banned[1]))
# print(string)

# moms_list = ['milk', 'bread']
# i_bought = ['bread', 'cola']

# for item_in_moms_list in moms_list:
#     if item_in_moms_list in i_bought:
#         print("Good, you buy", item_in_moms_list)
#     else:
#         print("You forgot", item_in_moms_list)
# for item_in_i_bought in i_bought:
#     if item_in_i_bought not in moms_list:
#         print("You not buy", item_in_i_bought)
    
# moms_list = input("Mom ask: ").split()
# i_bought = input("I'm buy: ").split()

# for item_in_moms_list in moms_list:
#     if item_in_moms_list in i_bought:
#         print("Good, you buy", item_in_moms_list)
#     else:
#         print("You forgot", item_in_moms_list)
# for item_in_i_bought in i_bought:
#     if item_in_i_bought not in moms_list:
#         print("Why you buy", item_in_i_bought)
    
# list_ =[['hello', 'world'], ['bye']]
# print(list_)
# print(list_[1])
# print(list_[1][-1])
# print(list_[1][0][-1])

# list_ = ['b', 'a', 'N', 'u', 'R', 'U', 't']
# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# list3 = list1 + list2
# print(list3)
# list1.extend(list2)
# print(list1)
# print(list1.index(3))
# list_.append(8)                  # append - add to end
# list_.insert(2, 3)               # insert - (индекс, значение)
# list_.pop(0)                     # pop(index) - удаляет и возвращает значение
# list_.remove(1)                  # remove(index) - удаляет значение
# list_.clear()                    # clear() - очищает весь список
# print(list_.count(1))
# list_.sort()
# print(len(list_))
# print(len(list_)//2)
# list_.reverse()
# list_.extend()
# print(list_)




