# 2. Отсортировать по возрастанию методом простого выбора (сортировка выбором) одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Вывести на экран исходный и отсортированный массивы.
import numpy

arr = numpy.random.uniform(0, 50, 5)
print(arr)

len_arr = len(arr)
for j in range(len_arr-1):
    id_min = j
    for i in range(j+1, len_arr):
        if arr[i] < arr[id_min]:
            id_min = i
    arr[j], arr[id_min] = arr[id_min], arr[j]
print(arr)