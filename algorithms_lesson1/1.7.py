a = float(input("Сторона треугольника a = "))
b = float(input("Сторона треугольника b = "))
c = float(input("Сторона треугольника c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний треугольник")
elif a == b == c:
    print("Равносторонний треугольник")
else:
    print("Равнобедренный треугольник")