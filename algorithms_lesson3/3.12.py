# Задана матрица неотрицательных чисел. Посчитать сумму элементов в каждом столбце.
# Определить, какой столбец содержит максимальную сумму.

from random import random

M = 6
N = 5
arr = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 10))
        print(" |%3d| " % b[j], end='')
    arr.append(b)
    print()

for i in range(M):
    print(" ----- ", end='')
print()

max_sum = 0
col = 0
for i in range(M):
    s = 0
    for j in range(N):
        s += arr[j][i]
    print(" |%3d |" % s, end='')
    if s > max_sum:
        max_sum = s
        col = i
print()
print("The %d-th column contains the maximum sum of column elements" % (col + 1))