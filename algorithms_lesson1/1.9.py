print("Введите три числа: ")
a = int(input())
b = int(input())
c = int(input())

if b < a < c or c < a < b:
    print("Среднее из трех чисел: ", a)
elif a < b < c or c < b < a:
    print("Среднее из трех чисел: ", b)
else:
    print("Среднее из трех чисел: ", c)