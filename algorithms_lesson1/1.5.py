a = input("Первая буква: ")
b = input("Вторая буква: ")
a_ord = ord(a)
b_ord = ord(b)
print("Порядковый номер первой буквы %s: %i" % (a, a_ord))
print("Порядковый номер второй буквы %s: %i" % (b, b_ord))
if a_ord < b_ord:
    print("Число букв между %s и %s: %i" % (a, b, b_ord-a_ord-1))
elif a_ord > b_ord:
    print("Число букв между %s и %s: %i" % (a, b, abs(b_ord-a_ord+1)))
else:
    print("Вы ввели одну и ту же букву в качестве первой и второй букв")
