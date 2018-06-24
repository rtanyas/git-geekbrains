# Найти максимальный элемент каждого столбца матрицы.

from random import random
N = 6
M = 5
arr = []
for i in range(N):
    lst = []
    for j in range(M):
        lst.append(int(random() * 100))
    arr.append(lst)
for i in range(N):
    for j in range(M):
        print(" |%3d| " % arr[i][j], end='')
    print()
for i in range(M):
    print(" ----- ", end='')
print()
for j in range(M):
    mx = arr[0][j]
    for i in range(N):
        if arr[i][j] > mx:
            mx = arr[i][j]
    print(" |%3d| " % mx, end='')
print()
