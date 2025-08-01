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


"""
=====================================================================
2. kwargs (Variable Keyword Arguments)
What it is
Collects extra keyword arguments into a dictionary

The ** unpacks key-value pairs (name kwargs is convention)


======================================================================

"""

def create_user_profile(**user_info):
    profile = {
        'username': user_info.get('username', 'Guest'),
        'email': user_info.get('email'),
        'premium': user_info.get('is_premium', False)
    }

    return profile
# Calling the function with variable keyword arguments
print(create_user_profile(username="abenet_asnake", 
                          email="abenet.asnaketesfaye@gmail.com",
                           is_premium=True,
                           joined="2023-10-01"))