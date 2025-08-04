"""
====================================================================================================================
The collections module provides high-performance alternatives to 
Python's built-in containers (dict, list, set, tuple). 
Here's a comprehensive guide to its most useful classes:
====================================================================================================================

"""

# 1. defaultdict - Dictionary with Default Values
from collections import defaultdict
# defaultdict is a subclass of dict that provides a default value for nonexistent keys.
# It allows you to specify a default factory function that returns the default value when a key is  not found.
# Example of using defaultdict
default_dict = defaultdict(int)  # Default value is 0 for int   
default_dict["apples"] += 1  # Incrementing the count of apples
default_dict["bananas"] += 2  # Incrementing the count of bananas
print(f"Defaultdict: {default_dict}")  # Output: defaultdict(<class 'int'>, {'apples': 1, 'bananas': 2})


# 2. Counter - Counting Hashable Objects
from collections import Counter
# Counter is a subclass of dict that counts the occurrences of hashable objects.
# It is useful for counting elements in an iterable or for counting occurrences of items in a collection.
# Example of using Counter
counter = Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
print(f"Counter: {counter}")  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
# Counter can also be used with strings
char_counter = Counter("hello world")
print(f"Character Counter: {char_counter}")  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# Counter can be used to find the most common elements
most_common = counter.most_common(2)  # Get the two most common elements
print(f"Most common elements: {most_common}")  # Output: [('apple', 3), ('banana', 2)]
# Counter can also be used to subtract counts
counter2 = Counter(["apple", "banana", "banana"])
counter.subtract(counter2)  # Subtract counts from counter
print(f"Counter after subtraction: {counter}")  # Output: Counter({'apple': 2, 'banana': 0, 'orange': 1})


inventory = Counter(apples=5, oranges=3)
inventory.update(["apples", "apples", "pears"])  # Add items

print(inventory)
# Counter({'apples': 7, 'oranges': 3, 'pears': 1})

# Most common items
print(inventory.most_common(2)) # Output: [('apples', 7), ('oranges', 3)]