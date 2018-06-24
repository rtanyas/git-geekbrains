#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

first_divider = 2
dividers = range(first_divider,10)
a = [0]*len(dividers)

for i in range(2,100):
    for j in dividers:
        if i%j == 0:
            a[j-first_divider] += 1
i = 0
while i < len(dividers):
    print(i+first_divider, ' - ', a[i])
    i += 1