

# =============================================
#           ASSIGNMENT OPERATORS IN PYTHON
# =============================================

# 1. Basic Assignment (=)
x = 10
print(f"Basic assignment: x = {x}")  # Output: x = 10

# 2. Compound Assignment Operators
# ---------------------------------
x += 5  # Equivalent to: x = x + 5
print(f"Add & assign (+=): {x}")  # Output: 15

x -= 3  # Equivalent to: x = x - 3
print(f"Subtract & assign (-=): {x}")  # Output: 12

x *= 2  # Equivalent to: x = x * 2
print(f"Multiply & assign (*=): {x}")  # Output: 24

x /= 4  # Equivalent to: x = x / 4
print(f"Divide & assign (/=): {x}")  # Output: 6.0 (becomes float)

x //= 2  # Equivalent to: x = x // 2 (floor division)
print(f"Floor divide & assign (//=): {x}")  # Output: 3.0

x **= 3  # Equivalent to: x = x ** 3 (power)
print(f"Power & assign (**=): {x}")  # Output: 27.0

x %= 5  # Equivalent to: x = x % 5 (modulus)
print(f"Modulus & assign (%=): {x}")  # Output: 2.0

# 3. Special Assignments
# ---------------------------------
# Multiple assignment
a, b, c = 1, 2, 3
print(f"\nMultiple assignment: a={a}, b={b}, c={c}")  # Output: a=1, b=2, c=3

# Swapping variables
x, y = 5, 10
x, y = y, x  # Swap values
print(f"Swapped variables: x={x}, y={y}")  # Output: x=10, y=5

# Chained assignment
x = y = z = 0
print(f"Chained assignment: x={x}, y={y}, z={z}")  # Output: x=0, y=0, z=0

# 4. Assignment with Sequences
# ---------------------------------
# With lists
nums = [1, 2, 3]
nums += [4, 5]  # Equivalent to: nums = nums + [4, 5]
print(f"\nList after +=: {nums}")  # Output: [1, 2, 3, 4, 5]

nums *= 2  # Repeats the list
print(f"List after *=: {nums}")  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# With strings
text = "Hello"
text += " World"
print(f"\nString after +=: '{text}'")  # Output: 'Hello World'

text *= 2
print(f"String after *=: '{text}'")  # Output: 'Hello WorldHello World'

# 5. Walrus Operator (:=) - Python 3.8+
# -------------------------------------
# Assign and check in one line
if (user_input := input("\nEnter a number: ")).isdigit():
    print(f"You entered the number: {user_input}")
else:
    print("That's not a valid number!")

# =============================================
#               OUTPUT SUMMARY
# =============================================
"""
Basic assignment: x = 10
Add & assign (+=): 15
Subtract & assign (-=): 12
Multiply & assign (*=): 24
Divide & assign (/=): 6.0
Floor divide & assign (//=): 3.0
Power & assign (**=): 27.0
Modulus & assign (%=): 2.0

Multiple assignment: a=1, b=2, c=3
Swapped variables: x=10, y=5
Chained assignment: x=0, y=0, z=0

List after +=: [1, 2, 3, 4, 5]
List after *=: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

String after +=: 'Hello World'
String after *=: 'Hello WorldHello World'

Enter a number: 42
You entered the number: 42
"""