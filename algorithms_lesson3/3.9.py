# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 6
N = 5
MAX = 10
arr = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * MAX)
        b.append(n)
        print(' |%3d| ' % n, end='')
    arr.append(b)
    print()

mx = -1
for j in range(M):
    mn = MAX
    for i in range(N):
        if arr[i][j] < mn:
            mn = arr[i][j]
    if mn > mx:
        mx = mn
print("The maximum element among the minimum elements of columns of the matrix: ", mx)
