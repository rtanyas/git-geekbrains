a = input("Число: ")
sum = 0
mult = 1
for i in a:
    sum += int(i)
    mult *= int(i)

print("Сумма: ", sum)
print("Произведение: ", mult)