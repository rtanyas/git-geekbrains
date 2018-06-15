# 1. Получить значения координат первой точки и присвоить их переменным, например x1 и y1.
# 2. Получить значения координат (x2, y2) второй точки.
# 3. Вычислить значение k по формуле k = (y1 - y2) / (x1 - x2).
# 4. Вычислить значение b по формуле b = y2 - k * x2.
# 5. Вывести на экран полученное уравнение.

#import math

print("Координаты точки A(x1;y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Координаты точки B(x2;y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print("Уравнение прямой, проходящей через эти точки:")
if b > 0:
    print(" y = %.2f*x + %.2f" % (k, b))
elif b < 0:
    b = abs(b)
    #b = math.fabs(b)
    print(" y = %.2f*x - %.2f" % (k, b))
else:
    print(" y = %.2f*x" % k)