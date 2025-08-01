"""
=====================================================================
1. args (Variable Positional Arguments)
What it is
Collects extra positional arguments into a tuple

The * unpacks arguments (name args is convention, not required)


======================================================================

"""

def calculate_total(*prices):
    """Calculate the total price from variable number of arguments."""
    return sum(prices)
# Calling the function with variable positional arguments
print(calculate_total(10.99, 5.49, 3.25))   # Output: 19.73

# using the function with antonations 
def calculate_total_with_annotations(*prices: float) -> float:
    """Calculate the total price from variable number of arguments with type annotations."""
    return sum(prices)  
# Calling the function with variable positional arguments and type annotations
print(calculate_total_with_annotations(10.99, 5.49, 3.25))  # Output: 19.73


