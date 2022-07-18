from random import *
print('Добро пожаловать в числовую угадайку')
print('введите границу интервала выбора числа')
n3 = int(input())
num = randint(1,n3)




def is_valid(n):
    if 1 <= int(n) <= n3:
        return True
    else:
        return False


def input_num():
    flag = True
    while flag == True:
        print('Введите ваше число')
        n2 = input()
        if is_valid(int(n2)) == False:
            print('А может быть все-таки введем целое число от 1 до', n3, '?')
        else:
            n2 = int(n2)
            flag = False
    return n2


def conclusion(n1):
    n2 = input_num()
    counter = 1
    flag = True
    while flag == True:
        if n2 < n1:
            counter +=1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            n2 = input_num()
        elif n2 > n1:
            counter +=1
            print('Ваше число больше загаданного, попробуйте еще разок')
            n2 = input_num()
        elif n2 == n1:
            break

    print('Вы угадали, поздравляем!')
                
    return counter
            



print('Количество попыток-',conclusion(num))
print('Хотите сыграть еще раз?')
answer = input()
if answer.lower() == 'да':
    print('введите границу интервала выбора числа')
    n3 = int(input())
    num = randint(1,n3)
    num1 = input_num()
    print('Количество попыток-',conclusion(num))


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
