"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# An ordered, mutable collection of elements that can hold heterogeneous data (e.g., integers, strings). 
# Lists are like dynamic arrays.

# They can grow and shrink in size, and elements can be accessed by their index.
# Lists are defined using square brackets [] and can contain duplicate elements.
# Lists are versatile and can be used for various purposes, such as storing sequences of items, 
# implementing stacks and queues, or managing collections of data.
# Lists are a fundamental data structure in Python and are widely used in programming.

# Lists are mutable, meaning you can change their content after creation.
# You can add, remove, or modify elements in a list.
# Lists can contain elements of different data types, including other lists.
# Lists are zero-indexed, meaning the first element is at index 0.  
# Lists can be nested, meaning you can have lists within lists.
# Lists can be sliced, allowing you to extract a portion of the list.
# Lists can be iterated over using loops, making it easy to process each element.
# Lists can be sorted, reversed, and manipulated using various built-in methods.
# Lists are commonly used in Python for tasks such as data storage, manipulation, and processing.
# Lists are a fundamental data structure in Python and are widely used in programming.
# Lists are versatile and can be used for various purposes, such as storing sequences of items,
# implementing stacks and queues, or managing collections of data.
# Lists are a fundamental data structure in Python and are widely used in programming.
# allows duplicate elements, meaning you can have multiple occurrences of the same value.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""

# They can grow and shrink in size, and elements can be accessed by their index
shopping_list = ["apples", "bread", "milk"]  # Initial list
print(f"Original list: {shopping_list}")

# Access elements by index (zero-indexed)
print(f"First item: {shopping_list[0]}")  # Accessing the first item which is apples
print(f"Second item: {shopping_list[1]}")  # Accessing the second item  which is bread
print(f"Third item: {shopping_list[2]}")  # Accessing the third item which is milk

# Lists are mutable - modify elements
shopping_list[1] = "eggs"  # Changing 'bread' to 'eggs'
print(f"Modified list: {shopping_list}")  # Now the list is ['apples', 'eggs', 'milk']

# Grow the list (add items)
shopping_list.append("bananas")  # Adding 'bananas' to the end of the list
print(f"List after adding bananas: {shopping_list}")  # Now the list is ['apples', 'eggs', 'milk', 'bananas']