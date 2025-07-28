# =============================================
#           MEMBERSHIP OPERATORS IN PYTHON
# Membership operators check if a value is present in a sequence (like lists, tuples, strings).
# =============================================

# 1. Membership with Lists
fruits = ["apple", "banana", "cherry"]
print("1. List Examples:")
print("'banana' in fruits:", "banana" in fruits)           # True
print("'mango' not in fruits:", "mango" not in fruits)     # True

# 2. Membership with Strings
sentence = "Hello, welcome to Python programming!"
print("\n2. String Examples:")
print("'Python' in sentence:", "Python" in sentence)       # True
print("'Java' not in sentence:", "Java" not in sentence)   # True

# 3. Membership with Tuples
colors = ("red", "green", "blue")
print("\n3. Tuple Examples:")
print("'green' in colors:", "green" in colors)             # True
print("'yellow' not in colors:", "yellow" not in colors)   # True

# 4. Membership with Dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\n4. Dictionary Examples:")  
print("'name' in person:", "name" in person)               # True (checks keys)
print("'Alice' in person:", "Alice" in person)             # False (checks values
print("'age' not in person:", "age" not in person)         # False (checks keys)
