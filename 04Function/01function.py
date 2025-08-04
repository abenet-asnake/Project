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
# Default values for parameters
def make_sandwich(bread_type='white', filling='ham'):
    """Make a sandwich with specified bread and filling."""
    return f"Sandwich with {bread_type} bread and {filling} filling."   
print(make_sandwich())  # Default values
print(make_sandwich('whole grain'))  # Custom bread type    
print(make_sandwich('whole grain', 'turkey'))  # Custom bread and filling

# 3. Type Annotations - Static type hints (PEP 484)
def square(number: int) -> int:
    """Return the square of a number."""
    return number ** 2  
# Calling the function with type annotations
print(square(4))  # Output: 16  
def add_numbers(a: float, b: float) -> float:
    """Return the sum of two floating-point numbers."""
    return a + b    
# Calling the function with type annotations
print(add_numbers(3.5, 2.5))  # Output: 6
def concatenate_strings(a: str, b: str) -> str:
    """Return the concatenation of two strings."""
    return a + b    
# Calling the function with type annotations
print(concatenate_strings("Hello, ", "World!"))  # Output: Hello, World!

# 4. Variable Arguments - *args and **kwargs
# Using *args to accept a variable number of positional arguments
# Collects any number of positional arguments into a tuple
def variable_args(*args: int) -> int:
    """Return the sum of variable number of integer arguments."""
    return sum(args)    
# Calling the function with variable arguments
print(variable_args(1, 2, 3))  # Output: 6
def variable_kwargs(**kwargs: str) -> str:
    """Return a formatted string from variable keyword arguments."""
    return ', '.join(f"{key}={value}" for key, value in kwargs.items())

# 
# Calling the function with variable keyword arguments
print(variable_kwargs(name="Abenet", age="30"))  # Output: name=Abenet, age=30  
def variable_args_kwargs(*args: int, **kwargs: str) -> str:
    """Return a formatted string from variable args and kwargs."""
    args_str = ', '.join(map(str, args))
    kwargs_str = ', '.join(f"{key}={value}" for key, value in kwargs.items())
    return f"Args: {args_str}, Kwargs: {kwargs_str}"    
# Calling the function with variable args and kwargs
print(variable_args_kwargs(1, 2, name="Abenet", age="30"))  # Output: Args: 1, 2, Kwargs: name=Abenet, age=30   



"""
=====================================================================
Multiple Returns - Using tuples

Python functions can return multiple values packaged in a tuple, which you can unpack into separate variables.

Basic Syntax
python
def function():
    return value1, value2  # Returns a tuple (value1, value2)

# Unpacking the result
x, y = function()


=====================================================================

"""

def calculate_investment(principal: float, rate: float, year: int) -> tuple [float, float]:
    """Calculate the final amount and interest earned."""
    future_value = principal * (1 + rate) ** year
    interest = future_value - principal
    return future_value, interest

# Calling the function and unpacking the result
final_amount, interest = calculate_investment(1000.0, 0.08, 5)
print(f"Final Amount: {final_amount}, Interest Earned: {interest}")  # Output: Final Amount: 1276.2815625000003, Interest Earned: 276.2815625000003
