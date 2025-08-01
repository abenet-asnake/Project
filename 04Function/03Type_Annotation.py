"""
# Type annotations (introduced in PEP 484) 
# They are a way to explicitly declare the expected data types of function parameters, return values, and variables. 
# They make Python code more maintainable and catch bugs early.


def add_numbers(a: int, b: int) -> int:
    #Return the sum of two integers. 
    return a + b
# Calling the function with type annotations

"""
def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b    
# Calling the function with type annotations
print(add_numbers(3, 4))  # Output: 7
print(add_numbers(2.5, 3.5))  # Output: 6.0 (Python allows float inputs, but type hints suggest int)
