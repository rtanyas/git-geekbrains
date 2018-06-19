for i in range(32, 128):
    print("%5d-%s" % (i, chr(i)), end='')
    if (i - 1) % 10 == 0:
        print()