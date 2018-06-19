n = int(input("Введите кол-во элементов следующего ряда чисел: 1 -0.5 0.25 -0.125...: "))
num_prev = 1
sum = num_prev
for i in range (0, n-1):
    if i % 2 == 0:
        num_next = -abs(num_prev)/2
    else:
        num_next = abs(num_prev)/2
    sum += num_next
    num_prev = num_next
if n != 0:
    print("Сумма элементов ряда: ", sum)
else:
    print("Сумма элементов ряда: ", 0)