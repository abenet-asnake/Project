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


