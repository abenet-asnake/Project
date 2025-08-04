"""
=====================================================================================================================
                                                       05DataStructures/03Sets.py
#a set is an unordered, mutable collection of unique, hashable elements (e.g., integers, strings, tuples)
# Sets are defined using curly braces {} or the set() constructor.
# They can grow and shrink in size, and elements can be accessed by their value.    
# Sets are useful for tasks such as membership testing, removing duplicates from a collection,
# and performing mathematical set operations like union, intersection, and difference.
# Sets are mutable, meaning you can change their content after creation.
# Sets do not allow duplicate elements, meaning each element must be unique.
# Sets are commonly used in Python for tasks such as data storage, manipulation, and processing.
# Sets are versatile and can be used for various purposes, such as storing unique items,
# implementing mathematical set operations, or managing collections of data.

Manipulable: Supports methods like add(), remove(), union(), intersection().
=====================================================================================================================

"""


# Empty set (must use set(), not {})
empty_set = set()

# With initial values
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From other iterables
letters = set("hello")  # {'h', 'e', 'l', 'o'} (duplicates removed)
