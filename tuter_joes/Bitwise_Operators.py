

# Bitwise_Operators

# 1. AND (&)
a = 5  # In binary: 101
b = 3  # In binary: 011
print(f'1. AND (&)                   {a} & {b}:', a & b)  # Result: 1 (binary: 001)

# 2. OR (|)
a = 5  # In binary: 101
b = 3  # In binary: 011
print(f'2. OR (|)                    {a} | {b}:', a | b)  # Result: 7 (binary: 111)

# 3. XOR (^)
a = 5  # In binary: 101
b = 3  # In binary: 011
print(f'3. XOR (^)                   {a} ^ {b}:', a ^ b)  # Result: 6 (binary: 110)

# 4. NOT (~)
a = 5  # In binary: 101
print(f'4. NOT (~)                  ~{a}:', ~a)  # Result: -6 (Inverts all the bits)

# 5. Zero-fill Left Shift (<<)
# Shift the bits of a number to the left by a given number of positions
a = 5  # In binary: 101
shift = 2
print(f'5. Zero-fill Left Shift (<<) {a} << {shift}:', a << shift)  # Result: 20 (binary: 10100)

# 6. Signed Right Shift (>>)
# Shift the bits of a number to the right by a given number of positions
a = 20  # In binary: 10100
shift = 2
print(f'6. Signed Right Shift (>>)   {a} >> {shift}:', a >> shift)  # Result: 5 (binary: 101)

'''

4. NOT (~): Bitwise NOT
       The bitwise NOT operator (~) inverts the bits of a number. In binary, this means flipping every 1 to 0 and every 0 to 1. In Python, it also involves using two's complement to represent negative numbers.

       For example:

       The number 5 in binary is 101 (in an 8-bit system, it’s 00000101).
       Applying ~5 inverts all the bits: 11111010, which is -6 in two's complement form.
       The two's complement method represents negative numbers by inverting the bits and adding 1. That’s why ~5 equals -6.

5. Zero-fill Left Shift (<<): Left Shift
       The left shift operator (<<) shifts the bits of a number to the left by a specified number of positions, and fills the right side with zeros.

       For example:

       The number 5 in binary is 101.
       Shifting 5 left by 2 positions (5 << 2) moves the bits 101 to 10100, which is 20 in decimal.
       In essence, every left shift operation by n positions multiplies the number by 2^n:

       5 << 1 results in 10 (multiplication by 2),
       5 << 2 results in 20 (multiplication by 4).
6. Signed Right Shift (>>): Right Shift
       The right shift operator (>>) shifts the bits of a number to the right by a specified number of positions. For positive numbers, it fills the left side with 0s. For negative numbers, it fills the left side with 1s to preserve the sign.

       For example:

       The number 20 in binary is 10100.
       Shifting 20 right by 2 positions (20 >> 2) moves the bits to 101, which is 5 in decimal.
       A right shift by n positions effectively divides the number by 2^n:

       20 >> 1 results in 10 (division by 2),
       20 >> 2 results in 5 (division by 4).
       For negative numbers, the sign bit (the leftmost bit) is preserved during the shift, so the result remains negative.
'''