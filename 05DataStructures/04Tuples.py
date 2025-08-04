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

