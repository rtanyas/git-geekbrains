# 5. Массив размером m, где m – натуральное число, заполнен случайным образом. Найти в массиве моду. Модой называется элемент ряда, который встречается наиболее часто.

from collections import Counter

arr = list(map(int,input("Input your array please: ").split()))

data = Counter(arr)
#print(data.most_common())   # Returns all unique items and their counts
print(data.most_common(1)[0][0])  # Returns the highest occurring item (mode)

#from statistics import mode
#arr = list(map(int,input("Input your array please: ").split()))
#print(mode(arr))