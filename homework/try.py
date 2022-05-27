""" синтаксис try, excent """
"""
try:
    some code 1             # попробуй сделать эту инструкцию   
except:
    some code 2 (сюда пишется ошибка)  # если выдаст исключение(ошибка) то делай эту инструкцию
else:
    some code 3             # else срабатывает если try не вывел исключение т.е блок except не сработал
finally:
    some code 4             # finally будет работать всегда 
"""
"""except Exception as e  --> показывает что за ошибка выйдет""" 
# try:
#     num = int(input('Введите число: '))
# except:
#     print('Вы ввели не число!')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 / num2
# except ZeroDivisionError:         # если ввести не 0 а строку или симболы то программа не будет работать (выведет ошибку ValueError) т.е это часть срабатывает только если ввести 0
#     print('На ноль делить нельзя!')
# else:
#     print(res)
# finally:
#     print('Программа завершена')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Вы ввели не число')
# else:
#     print(res)
# finally:
#     print('Программа завершена'


# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# dict_.update({'except': 'Excention'})
# print(dict_)

# while True:
#     try:                              # мы говорим попробуй сделать вот это
#         key = input('Введите слово: ')
#         if key == 'exit':             # условие - если в инпуте введём exit то мы выходим из цикла
#             break
#         dict_[key] += 2 
#     except (KeyError, TypeError):     # в одну except  можно добавить несколько исключений и запринтить общее сообщение
#         print('Данного ключа нет либо произвести конкатенацию с числами нельза!')
#     # except KeyError:
#     #      print('Такого ключа нет в словаре!')
#     # except TypeError:
#     #     print('Вы не можете провести конкатенацию с числами')
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)



# list_ = [i for i in range(1, 31)]

# try:
#     index = int(input())
#     list_[index] = 'Makers'                   # меняем значение на слово Makers
# except IndexError:
#     print('You are out of list range')
# except ValueError:
#     print('Please enter the number, not a string')
# else
#     print('There is no exception')
# finally:
#     print(list_)


# try:
#     print(makers)
# except NameError:
#     print('Вы не создавали переменную Makers')


"""raise --> генерирует ошибку """

# num = int(input('Введите число от 1 до 70: '))
# if not num in range(1, 71):
#     raise Exception('Вы ввели число, которое не находится в данном промежутке')
# print('Okey')

"""task2"""
# b = 10
# c = 11
# try:
#     print(c + a + 'hello')
# except TypeError:
#     print('Вы не можете провести конкатенацию с числами')
# except NameError:
#     print('Введите перемунную правильно')
"""task3"""
    # try:
    #    num1 = int(input())
    #    num2 = int(input())
    #    res = num1 / num2 
    # except ZeroDivisionError:
    #     print('На ноль делить нельзя')
    # else:
    #     print(res)
"""task4"""
# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(res)
"""task5"""
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'}
#     dict_['key3']
# except KeyError:
#     print('Нет такого ключа!')
"""task6"""
# try:
#     list_ = [1, 4, 9, 16, 25, 36]
#     list_[6]
# except IndexError:
#     print('Нет такого элемента!')
"""task7"""
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else: 
#     print('Спасибо')
# finally:
#     print('До свидания!')
"""task8"""
# try:
#     num1 = int(input())
#     num2 = int(input())
#     num3 = num1 / num2
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')
# print(num3)
"""task9"""
# cash = int(input())
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)
"""extratask1"""
# inp1 = input()
# inp2 = input()
# try:
#     res = int(inp1) + int(inp2)
#     print(res)
# except ValueError:
#     res = inp1 + inp2
#     print(res)
"""----------------------------"""
# inp1 = input()
# inp2 = input()
# try:
#   inp1 = int(inp1)
#   inp2 = int(inp2)
# except ValueError:
#   print(str(inp1) + str(inp2))
# else:
#   print(inp1 + inp2)
"""extratask2"""
# inp1 = input()
# b = inp1.split(' ')
# list_ = []
# for i in b:
#     try:
#         number = int(i)
#         list_.append(number)
#     except:
#         raise ValueError('Данный элемент не является числом!')
"""-------------------------------------------------------"""
# inp1 = input().split()
# list_ = []
# for e in inp1:
#     try:
#         list_.append(int(e))
#     except ValueError:
#         raise Exception("Данный элемент не является числом!")


# try:
#     f = open("test.txt", 'w')
#     f.write("Hello world")
#     f.close()
# except IndexError:
#     print('Error')
# finally:
#     f.close()


