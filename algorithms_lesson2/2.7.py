n = int(input("Введите любое натуральное число: "))

left_side = 0
for i in range(1, n+1):
    left_side += i
right_side = n * (n + 1) // 2
if left_side == right_side:
    print("Для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число")
else:
    print("Равенство: 1+2+...+n = n(n+1)/2 при n=%d: %s=%s" % (n, left_side, right_side))