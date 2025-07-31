# =============================================
#       PYTHON FUNCTIONS & TYPE ANNOTATIONS
# =============================================
"""
# This module demonstrates the use of functions in Python,
Basic Functions - Definition and calling

Parameters - Positional, keyword, default values

Type Annotations - Static type hints (PEP 484)

Variable Arguments - *args and **kwargs

Multiple Returns - Using tuples

Lambda Functions - Anonymous functions

Functions as Objects - Passing functions as arguments

Decorators - Modifying function behavior

Generators - yield for memory-efficient iteration

Type Aliases - Creating custom type names

"""

# 1. Basic Functions
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
# Calling the function
print(greet("Abenet"))  # Output: Hello, Abenet!

def greeting(name):
    """Return a greeting message."""
    return f"Hello, {name}!"
# Calling the function
print(greeting("Abenet"))  # Output: Hello, Abenet!


# 2.Parameters - Positional, keyword, default values
def add(a: int, b: int = 5) -> int:
    """Return the sum of two numbers with a default value for b."""
    return a + b
# Calling the function with positional and keyword arguments
print(add(3))          # Output: 8 (b defaults to 5)    
print(add(3, 4))       # Output: 7 (b is overridden to 4)
def multiply(a: int, b: int = 2) -> int:
    """Return the product of two numbers with a default value for b."""
    return a * b
# Calling the function with positional and keyword arguments
print(multiply(3))          # Output: 6 (b defaults to 2)   
print(multiply(3, 4))       # Output: 12 (b is overridden to 4)

# Positional arguments (required)
def power(base, exponent):
    return base ** exponent

print("2³ =", power(2, 3))  # 8
# Keyword arguments (optional)
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")
describe_pet('Bob')  # Default animal_type is 'dog'
describe_pet('lol', 'Big lol')  # animal_type is 'big lol'