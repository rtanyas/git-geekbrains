print("Чтобы завершить работу программы, введите 0")

while True:
        s = input("Введите знак операции (+,-,*,/): ")
        if s == '0': break
        if s in ('+','-','*','/'):
                x = float(input("x="))
                y = float(input("y="))
                if s == '+':
                        print("%.2f" % (x+y))
                elif s == '-':
                        print("%.2f" % (x-y))
                elif s == '*':
                        print("%.2f" % (x*y))
                elif s == '/':
                        if y != 0:
                                print("%.2f" % (x/y))
                        else:
                                print("Деление на ноль невозможно")
        else:
                print("Неверный знак операции")