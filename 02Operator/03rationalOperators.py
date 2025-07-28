# =============================================
#           RELATIONAL OPERATORS IN PYTHON
# =============================================

# 1. Equality Operators
print("\n1. Equality Operators:")
print("5 == 5:", 5 == 5)          # True (equal)
print("5 == 3:", 5 == 3)          # False
print("'hello' == 'hello':", "hello" == "hello")  # True
print("'Hello' == 'hello':", "Hello" == "hello")  # False (case-sensitive)

# 2. Inequality Operators
print("\n2. Inequality Operators:")
print("5 != 3:", 5 != 3)          # True (not equal)
print("5 != 5:", 5 != 5)          # False
print("'apple' != 'orange':", "apple" != "orange")  # True

# 3. Greater/Less Than
print("\n3. Greater/Less Than:")
print("10 > 7:", 10 > 7)          # True
print("7 > 10:", 7 > 10)          # False
print("10 < 7:", 10 < 7)          # False
print("7 < 10:", 7 < 10)          # True

# 4. Greater/Less Than or Equal
print("\n4. Greater/Less Than or Equal:")
print("10 >= 10:", 10 >= 10)      # True
print("9 >= 10:", 9 >= 10)        # False
print("5 <= 5:", 5 <= 5)          # True
print("6 <= 5:", 6 <= 5)          # False

# 5. Special Cases
print("\n5. Special Cases:")
# String comparison (lexicographical order)
print("'apple' < 'banana':", "apple" < "banana")  # True ('a' < 'b')
print("'cat' > 'dog':", "cat" > "dog")           # False ('c' < 'd')

# Mixed numeric types
print("5 == 5.0:", 5 == 5.0)     # True (value equality)
print("5 == '5':", 5 == "5")      # False (different types)

# Chained comparisons
x = 5
print("1 < x < 10:", 1 < x < 10)  # True (equivalent to 1 < x and x < 10)

# 6. Practical Example
print("\n6. Practical Example (Age Check):")
age = 18
if age >= 18:
    print("Status: Adult")  # This will execute
else:
    print("Status: Minor")
