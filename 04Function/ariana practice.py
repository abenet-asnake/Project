def student(name):
    """Return a greeting message."""
    return f"Hello, {name}!"
# Calling the function
print(student("Ariyana"))  # Output: Hello, Ariyana!

def twoAdd(a, b):
    """Return the sum of two numbers."""
    return a + b

def twomul(a, b):
    """Return the sum of two numbers."""
    return a * b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
# Calling the function
print(twoAdd(x, y))
print(twomul(x, y))
