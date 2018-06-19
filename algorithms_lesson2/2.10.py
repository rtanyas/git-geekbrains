a = 10
b = 40

print()
for i in range(a):
    if i==0 or i==a-1:
        for j in range(b):
            print('п', end='')
    else:
        print('п',end='')
        for j in range(1, b-1):
            print('с', end='')
        print('п', end='')
    print()