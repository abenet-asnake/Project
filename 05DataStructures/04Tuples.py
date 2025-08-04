"""
=====================================================================================================================
# 05DataStructures/04Tuples.py
# A tuple is an ordered, immutable collection of elements, which can be of mixed types (e.g., integers, strings, lists).
# Tuples are defined using parentheses () and can contain duplicate elements.
# Tuples are similar to lists but have the key difference that they cannot be modified after creation.
# Tuples are useful for tasks such as grouping related data, returning multiple values from a function 
=====================================================================================================================

"""

# Tuples are immutable, meaning you cannot change their content after creation.
# Tuples can contain elements of different data types, including other tuples.  
# Tuples are commonly used in Python for tasks such as data storage, manipulation, and processing.
# Tuples are versatile and can be used for various purposes, such as storing fixed collections of

#example, coordinates, or returning multiple values from a function.

coordinates = (10.0, 20.0)  # A tuple representing coordinates
print(f"Coordinates: {coordinates}")  # Output: Coordinates: (10.0, 20.0)

# Creating a tuple with mixed data types
mixed_tuple = (1, "apple", 3.14, True)
print(f"Mixed tuple: {mixed_tuple}")  # Output: Mixed tuple: (1, 'apple', 3.14, True)
# Accessing elements by index (zero-indexed)
print(f"First element: {mixed_tuple[0]}")  # Output: First element: 1
print(f"Second element: {mixed_tuple[1]}")  # Output: Second element: apple     
print(f"Third element: {mixed_tuple[2]}")  # Output: Third element: 3.14
print(f"Fourth element: {mixed_tuple[3]}")  # Output: Fourth element: True

# Tuples can be nested, meaning you can have tuples within tuples
nested_tuple = (1, (2, 3), (4, 5))
print(f"Nested tuple: {nested_tuple}")  # Output: Nested tuple: (1, (2, 3), (4, 5))
# Accessing nested tuple elements
print(f"Nested element: {nested_tuple[1][0]}")  # Output: Nested element: 2 
print(f"Nested element: {nested_tuple[2][1]}")  # Output: Nested element: 5
print(f"Nested element: {nested_tuple[0]}")  # Output: Nested element: 1

# Tuples can be used to return multiple values from a function
def get_user_info():
    """Return user information as a tuple."""
    return ("Abenet", 30, "abeneta@flipperschools.com", True)
user_info = get_user_info()
print(f"User Info: {user_info}")  # Output: User Info: ('Abenet', 30, 'abeneta@flipperschools.com', True)
# Accessing returned tuple elements
print(f"User Name: {user_info[0]}")  # Output: User Name: Abenet
print(f"User Age: {user_info[1]}")  # Output: User Age: 30
print(f"User Email: {user_info[2]}")  # Output: User Email: abeneta@flipperschools.com
print(f"User Premium Status: {user_info[3]}")  # Output: User Premium Status: True

# Tuples can be used as dictionary keys because they are immutable
user_profile = {
    "username": "abenet_asnake",
    "email": "abeneta@flipperschools.com",
    "premium": True,    
}
print(f"User Profile: {user_profile}")  # Output: User Profile: {'username': 'abenet_asnake', 'email': 'abeneta@flipperschools.com', 'premium': True}
# Accessing dictionary values
print(f"Username: {user_profile['username']}")  # Output: Username: abenet_asnake
print(f"Email: {user_profile['email']}")  # Output: Email: abeneta@flipperschools.com
print(f"Premium Status: {user_profile['premium']}")  # Output: Premium Status: True


# Tuples can be unpacked into variables
x, y = coordinates
print(f"x: {x}, y: {y}")  # Output: x: 10.0, y: 20.0
# Unpacking nested tuples
a, (b, c), (d, e) = nested_tuple    
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")  # Output: a: 1, b: 2, c: 3, d: 4, e: 5