#4. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

import numpy
from random import randint

n = randint(5, 9)
if n % 2 == 0:
    n += 1
arr = numpy.random.randint(1, 50, n)
##arr = [randint(1, 90) for _ in range(n)]

sorted_arr = sorted(arr)
print(sorted_arr)
if len(sorted_arr) % 2 == 1:
    print(sorted_arr[len(sorted_arr)//2])