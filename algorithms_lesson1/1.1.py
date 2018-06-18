a = input("Введите трехзначное число: ")
sum = 0
mult = 1
for i in a:
    sum += int(i)
    mult *= int(i)

print("Сумма цифр введенного числа: ", sum)
print("Произведение цифр введенного числа: ", mult)