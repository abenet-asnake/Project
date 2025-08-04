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
# Adding elements
fruits.add("orange")  # Add a new fruit 
print(f"Fruits after adding orange: {fruits}")  # {'apple', 'banana', 'cherry', 'orange'}
fruits.update(["kiwi", "mango"])  # Add multiple fruits
print(f"Fruits after updating with kiwi and mango: {fruits}")  # {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'}
fruits.update({"grape", "pear"})  # Add multiple fruits from a set
print(f"Fruits after updating with grape and pear: {fruits}")  # {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'grape', 'pear'}


# Removing elements
fruits.remove("banana")  # Remove a specific fruit  
print(f"Fruits after removing banana: {fruits}")  # {'apple', 'cherry', 'orange', 'kiwi', 'mango', 'grape', 'pear'}
fruits.discard("kiwi")  # Remove a specific fruit, no error if not found
print(f"Fruits after discarding kiwi: {fruits}")  # {'apple', 'cherry', 'orange', 'mango', 'grape', 'pear'}
removed_fruit = fruits.pop()  # Remove and return an arbitrary fruit        
print(f"Removed fruit: {removed_fruit}")  # Output: Removed fruit: apple (or any other arbitrary fruit)
print(f"Fruits after popping an arbitrary fruit: {fruits}")  # Remaining fruits 

# set operations
set_a = {1, 2, 3}   
set_b = {3, 4, 5}
# Union
union_set = set_a | set_b  # or set_a.union(set_b)  
print(f"Union of set_a and set_b: {union_set}")  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a & set_b  # or set_a.intersection(set_b)    
print(f"Intersection of set_a and set_b: {intersection_set}")  # {3}