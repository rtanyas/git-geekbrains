n = input("Введите натуральное число: ")
sum_even = sum_odd = 0

for s in n:
    num = int(s)
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Сумма четных - %d, сумма нечетных цифр введенного числа - %d" % (sum_even, sum_odd))