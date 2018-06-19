n = int(input("Сколько будет введено чисел? "))
d = int(input("Какую цифру в введенных числах считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Кол-во цифр %d равно %d" % (d, count))