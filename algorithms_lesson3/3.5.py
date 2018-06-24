# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random

N = 10
arr = []
for i in range(N):
    arr.append(int(random() * 20) - 10)
print(arr)

indexes = []
index = -2
for i in range(N):
    if arr[i] < 0 and index == -2:
        index = i
        indexes.append(index)
    elif arr[i] < 0 and arr[i] > arr[index]:
        indexes = []
        index = i
        indexes.append(index)
    elif arr[i] < 0 and arr[i] == arr[index]:
        index = i
        indexes.append(i)

if len(indexes) != 0:
    print("Maximal negative element is: ", arr[index], ', the position in the array:', indexes)
else:
    print("No negative elements in the array.")