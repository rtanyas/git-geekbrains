from random import random
n = round(random() * 100)
print(n)
i = 1
print("Сгенерировано случайное число от 0 до 100, попробуйте отгадать его за 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Сгенерированное число меньше')
    elif u < n:
        print('Сгенерированное число больше')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было сгенерировано число: ', n)