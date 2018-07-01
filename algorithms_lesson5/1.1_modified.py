#1.1 (только часть с получением суммы цифр введенного числа): при получении sum_v1 удается сохратить использование памяти из-за неиспользование переменной i (которая используется для sum_v2)
import sys

# pre-condition
a = input("Enter a three-digit number: ")
print("For 'a': ", sys.getsizeof(a), "bytes")

# version 1
sum_v1 = sum(list(map(int, a)))

print("sum_v1 = ", sum_v1)
print()
print("For version1: ", sys.getsizeof(sum_v1), "bytes")

# version 2
sum_v2 = 0
print()
for i in a:
    sum_v2 += int(i)

print("sum_v2 = ", sum_v2)
print("For 'sum_v2'", sys.getsizeof(sum_v2), "bytes")
print("For 'i'", sys.getsizeof(i), "bytes")
print()
v2 = sys.getsizeof(sum_v2) + sys.getsizeof(i)
print("For version2: ", v2, "bytes")