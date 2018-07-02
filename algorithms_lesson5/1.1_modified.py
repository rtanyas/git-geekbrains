#1.1 Для version1 удается сохратить использование памяти из-за неиспользование переменной i (которая используется для version2)
import sys
from functools import reduce

# pre-condition
a = input("Enter a three-digit number: ")
print("For 'a': ", sys.getsizeof(a), "bytes")

# version 1
#numbers = list(map(int, a))
#sum_v1 = sum(numbers)
sum_v1 = sum(list(map(int, a)))
mult_v1 = reduce(lambda a,b: a*b, list(map(int, a)))

print("sum_v1 = ", sum_v1)
print("mult_v1 = ", mult_v1)
print()
print("For version1 (sum): ", sys.getsizeof(sum_v1), "bytes")
print("For version1 (mult): ", sys.getsizeof(mult_v1), "bytes")


# version 2
sum_v2 = 0
mult_v2 = 1
print()
for i in a:
    sum_v2 += int(i)
    mult_v2 *= int(i)
	
print("sum_v2 = ", sum_v2)
print("mult_v2 = ", mult_v2)
print("For 'sum_v2'", sys.getsizeof(sum_v2), "bytes")
print("For 'i'", sys.getsizeof(i), "bytes")
print()
v2_sum = sys.getsizeof(sum_v2) + sys.getsizeof(i)
v2_mult = sys.getsizeof(mult_v2) + sys.getsizeof(i)
print("For version2 (sum): ", v2_sum, "bytes")
print("For version2 (mult): ", v2_mult, "bytes")
