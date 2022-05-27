import random
user = input("Введите имя: ")
game = input("Хотете ли вы сыграть? \nВыберите да или нет: ")
i = 0
while i == 0:
    num = random.randint(1, 10)
    count = 1
    j = 0
    while j == 0:
        if game == 'да' or game == 'Да':
            usernum = input("Введите число от 1 до 10: ")
            if usernum.isdigit():
                usernum = int(usernum)
                if usernum == num:
                    print(f'Вы угадали число за {count} попыток')
                    game = input("Хотете ли вы сыграть? \nВыберите да или нет: ")
                    j = 1
                elif usernum != num:
                    print("Вы не угадали число")
                    count += 1
            else:
                print('Введите именно цифры')
        elif game == 'нет' or game == 'Нет':
            print("Игра закончена!")
            j = 1
            i = 1   
        else:
            print('Введите именно да или нет')
            game = input("Хотете ли вы сыграть? \nВыберите да или нет: ")