#1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
#заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import numpy

arr = numpy.random.randint(-100, 100, 10)
print(arr)

print()
length = len(arr)
for i in range(length-1):
    for j in range(i+1,length):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)