# Определить, какое число в массиве встречается чаще всего

from random import random

N = 10
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 10)
print(arr)


counter = 1
max_frq = 2
for i in range(N - 1):
    frq_i = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq_i += 1
    if frq_i >= max_frq:
        max_frq = frq_i
        counter += 1
        print('There is a number', arr[i], max_frq, 'times')

if counter == 1:
    print('All items are unique')