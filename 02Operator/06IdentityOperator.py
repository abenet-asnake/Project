# =============================================
#           IDENTITY OPERATORS IN PYTHON
# Identity operators compare the memory locations of two objects (whether they are the same object),
#  unlike == which compares values.
# =============================================


x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y:", x is y)      # False (different objects)
print("x is z:", x is z)      # True (same object)
print("x is not y:", x is not y)  # True

# 2. None Comparison (Most Common Use Case)
print("\n2. None Checks:")
value = None
print("value is None:", value is None)      # True
print("value is not None:", value is not None)  # False