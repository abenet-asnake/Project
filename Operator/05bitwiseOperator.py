# =============================================
#           BITWISE OPERATORS IN PYTHON
# =============================================

# Helper function to print binary representation
def bin_format(num, bits=8):
    return format(num & 0b11111111, f'0{bits}b')  # Show 8 bits by default

# Sample numbers
a = 0b1100  # 12 in binary
b = 0b1010  # 10 in binary

print(f"a = {bin_format(a)} (decimal: {a})")
print(f"b = {bin_format(b)} (decimal: {b})\n")

# 1. AND (&) - Sets bit to 1 if BOTH bits are 1
result = a & b
print(f"1. AND (&)       {bin_format(a)} & {bin_format(b)} = {bin_format(result)} (decimal: {result})")

# 2. OR (|) - Sets bit to 1 if EITHER bit is 1
result = a | b
print(f"2. OR (|)        {bin_format(a)} | {bin_format(b)} = {bin_format(result)} (decimal: {result})")

# 3. XOR (^) - Sets bit to 1 if ONLY ONE bit is 1
result = a ^ b
print(f"3. XOR (^)       {bin_format(a)} ^ {bin_format(b)} = {bin_format(result)} (decimal: {result})")

# 4. NOT (~) - Inverts all bits (flips 0s to 1s and vice versa)
result = ~a
print(f"4. NOT (~)       ~{bin_format(a)} = {bin_format(result)} (decimal: {result}) [2's complement]")

# 5. Left Shift (<<) - Shifts bits left, fills with 0s
result = a << 2
print(f"5. LEFT SHIFT (<<) {bin_format(a)} << 2 = {bin_format(result)} (decimal: {result})")

# 6. Right Shift (>>) - Shifts bits right, fills with 0s
result = a >> 2
print(f"6. RIGHT SHIFT (>>) {bin_format(a)} >> 2 = {bin_format(result)} (decimal: {result})")

# 7. Practical Examples
print("\n7. Practical Applications:")

# Check if number is odd/even using AND
num = 15
print(f"Is {num} odd? {bool(num & 1)}")  # True (last bit is 1)

# Swap two numbers without temp variable
x, y = 5, 9
print(f"Before swap: x={x}, y={y}")
x ^= y
y ^= x
x ^= y
print(f"After XOR swap: x={x}, y={y}")

# Check if power of 2
n = 16
is_power_of_two = n > 0 and (n & (n - 1)) == 0
print(f"Is {n} a power of 2? {is_power_of_two}")

# =============================================
#               OUTPUT SUMMARY
# =============================================
"""
a = 00001100 (decimal: 12)
b = 00001010 (decimal: 10)

1. AND (&)       00001100 & 00001010 = 00001000 (decimal: 8)
2. OR (|)        00001100 | 00001010 = 00001110 (decimal: 14)
3. XOR (^)       00001100 ^ 00001010 = 00000110 (decimal: 6)
4. NOT (~)       ~00001100 = 11110011 (decimal: -13) [2's complement]
5. LEFT SHIFT (<<) 00001100 << 2 = 00110000 (decimal: 48)
6. RIGHT SHIFT (>>) 00001100 >> 2 = 00000011 (decimal: 3)

7. Practical Applications:
Is 15 odd? True
Before swap: x=5, y=9
After XOR swap: x=9, y=5
Is 16 a power of 2? True
"""