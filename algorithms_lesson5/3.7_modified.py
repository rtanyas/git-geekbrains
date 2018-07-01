# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.
# Варианты 2 и 3 одинаковы по использованию памяти и лучше, чем вариант 1.

from random import random
import sys

# pre-condition
N = 10
arr = []
for i in range(N):
    arr.append(int(random()*100) - 10)
print("For 'arr'", sys.getsizeof(arr), "bytes")
print(arr)


# version1
if arr[0] > arr[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if arr[i] < arr[min1]:
        b = min1
        min1 = i
        if arr[b] < arr[min2]:
            min2 = b
    elif arr[i] < arr[min2]:
        min2 = i
min1_v1 = arr[min1]
min2_v1 = arr[min2]

print("Version1: the first smallest array element %d" % min1_v1)
print("Version1: the second smallest array element %d" % min2_v1)
print()
v1 = 0
for k in [min1, min2, i, b, range(2, N), min1_v1, min2_v1, arr[min1], arr[min2], arr[i], arr[b]]:
    v1 += sys.getsizeof(k)
print("For version1: ", v1, "bytes")

# version2
print()
sort = sys.getsizeof(arr.sort())
#print("For 'arr.sort()'", sys.getsizeof(arr.sort()), "bytes")
#arr.sort()
print("Version2: the first smallest array element %d" % arr[0])
print("Version2: the second smallest array element %d" % arr[1])
print("For 'arr[0]'", sys.getsizeof(arr[0]), "bytes")
print("For 'arr[1]'", sys.getsizeof(arr[1]), "bytes")
print()
v2 = sys.getsizeof(arr[0]) + sys.getsizeof(arr[1]) + sort
print("For version2: ", v2, "bytes")

# version3
print()
min1_v3 = min(arr)
remove = sys.getsizeof(arr.remove(min1_v3))
#print("For 'arr.remove(min1_v3)'", sys.getsizeof(arr.remove(min1_v3)), "bytes")
#arr.remove(min1_v3)
min2_v3 = min(arr)
print("Version3: the first smallest array element %d" % min1_v3)
print("Version3: the second smallest array element %d" % min2_v3)
print("For 'min1_v3'", sys.getsizeof(min1_v3), "bytes")
print("For 'min2_v3'", sys.getsizeof(min2_v3), "bytes")
print()
v3 = sys.getsizeof(min1_v3) + sys.getsizeof(min2_v3) + remove
print("For version3: ", v3, "bytes")

