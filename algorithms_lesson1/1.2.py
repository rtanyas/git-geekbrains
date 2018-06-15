a = 5
b = 6

print(bin(a))
print(bin(b))

bit_or = a | b
bit_and = a & b
bit_xor = a ^ b

bit_r = a >> 2
bit_l = a << 2

print("Результат побитового OR в bit: %s" % bin(bit_or))
print("Результат побитового AND в bit: %s" % bin(bit_and))
print("Результат побитового XOR в bit: %s" % bin(bit_xor))
print("Результат побитового сдвига вправо на 2 знака в bit: %s" % bin(bit_r))
print("Результат побитового сдвига влево на 2 знака в bit: %s" % bin(bit_l))

print("Результат побитового OR в int: %s" % bit_or)
print("Результат побитового AND в int: %s" % bit_and)
print("Результат побитового XOR в int: %s" % bit_xor)
print("Результат побитового сдвига вправо на 2 знака в int: %s" % bit_r)
print("Результат побитового сдвига влево на 2 знака в int: %s" % bit_l)