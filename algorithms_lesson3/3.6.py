# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Их самих в сумму не включать.

from random import random

N = 10
arr = []
for i in range(N):
    arr.append(int(random()*10))
print(arr)

min_id = 0
max_id = 0
for i in range(1, N):
    if arr[i] < arr[min_id]:
        min_id = i
    elif arr[i] > arr[max_id]:
        max_id = i
print("Minimal array element: arr[%d] = %d, maximal array element: arr[%d] = %d" % (min_id, arr[min_id], max_id, arr[max_id]))

if min_id > max_id:
    min_id, max_id = max_id, min_id

sum = 0
for i in range(min_id+1, max_id):
    sum += arr[i]
print("Sum of array elements between the first minimal(or maximum) element and the first maximal(or minimal) element: ", sum)
