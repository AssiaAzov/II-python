a = 6
b = 5


bit_or = a | b
bit_and = a & b
bit_xor = a ^ b

print(bit_and,(bin(a|b)),'\n',
    bit_or,(bin(a&b)),'\n',
    bit_xor,(bin(a^b)))

print(a>>2,a<<2)
