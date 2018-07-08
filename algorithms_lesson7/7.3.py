# 3. Отсортировать по возрастанию методом простого включения (сортировка вставкой) одномерный целочисленный массив, заданный с клавиатуры различными числами.
# Вывести на экран исходный и отсортированный массивы.

arr = list(map(int,input("Input your array please: ").split()))
print(arr)
for i in range(len(arr)):
    v = arr[i]
    j = i
    while (arr[j-1] > v) and (j > 0):
        arr[j] = arr[j-1]
        j = j - 1
    arr[j] = v
print(arr)
