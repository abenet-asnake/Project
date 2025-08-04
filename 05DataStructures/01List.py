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

 # Insert at specific position( Add Items at Specific Position) using insert()
shopping_list.insert(1, "oranges")  # Inserting 'oranges' at index 1
print(f"List after inserting oranges: {shopping_list}")  # Now the list is ['apples', 'oranges', 'eggs', 'milk', 'bananas']

# Shrink the list (remove items) using remove()
shopping_list.remove("milk")  # Removing 'milk' from the list
print(f"List after removing milk: {shopping_list}")  # Now the list is ['apples', 'oranges', 'eggs', 'bananas']

# Shrink the list 
removed_item = shopping_list.pop(2)  # Removing the item at index 2 ( which is 'eggs')
print(f"Removed item: {removed_item}")  # Output: Removed item: eggs
print(f"List after popping item at index 2: {shopping_list}")  # Now the list is ['apples', 'oranges', 'bananas'](remove items) using pop()


# Lists can contain different data types
mixed_list = [42, "hello", True, 3.14, ["nested", "list"]]
print(f"\nMixed data types: {mixed_list}")

# Access nested list
print(f"Nested list item: {mixed_list[4][1]}")  # 'list'

# Lists allow duplicate elements
duplicate_list = [1, 2, 2, 3, 3, 3]
print(f"\nList with duplicates: {duplicate_list}")


"""

-----------------------------------------------------------------------------------------------------------------
# Lists can be sliced
# Slicing allows you to extract a portion of the list
# Slicing syntax: list[start:end:step]
# where 'start' is the index to start from, 'end' is the index to   
# stop at (exclusive), and 'step' is the increment between indices.
# If 'start' is omitted, it defaults to 0. If 'end' is omitted, it defaults to the length of the list.
# If 'step' is omitted, it defaults to 1.   
# Slicing returns a new list containing the specified elements.
# Example of slicing a list


----------------------------------------------------------------------------------------------------------------

"""

# Slicing a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal list: {numbers}")
# Slicing from index 2 to 5 (exclusive)
sliced_numbers = numbers[2:5]  # This will give [2, 3, 4]
print(f"Sliced list (2 to 5): {sliced_numbers}")
# Slicing from the beginning to index 4 (exclusive)
sliced_numbers_start = numbers[:4]  # This will give [0, 1, 2, 3]
print(f"Sliced list (start to 4): {sliced_numbers_start}")
# Slicing from index 5 to the end
sliced_numbers_end = numbers[5:]  # This will give [5, 6, 7, 8, 9]
print(f"Sliced list (5 to end): {sliced_numbers_end}")
# Slicing with a step of 2
sliced_numbers_step = numbers[::2]  # This will give [0, 2, 4, 6, 8]
print(f"Sliced list with step 2: {sliced_numbers_step}")
# Slicing with negative indices
sliced_numbers_negative = numbers[-5:-2]  # This will give [5, 6, 7]
print(f"Sliced list (-5 to -2): {sliced_numbers_negative}") 
# Slicing with a negative step (reversing the list)
sliced_numbers_reverse = numbers[::-1]  # This will give [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"Sliced list reversed: {sliced_numbers_reverse}")  # This will give [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
 #Get from 2nd element to 2nd from last
sliced_numbers_custom = numbers[2:-2]  # This will give [2, 3, 4, 5, 6, 7]
print(f"Sliced list (2 to 2nd from last): {sliced_numbers_custom}")  # This will give [2, 3, 4, 5, 6, 7]


# Create a list of squares for numbers from 0 to 4 compressive list
squares = [x * x for x in range(5)]
print(squares)

# matrix flattened in a single list using list comprehension
# Flattening a 2D list (matrix) into a 1D list using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)