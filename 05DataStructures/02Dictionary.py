"""

========================================================================================================
                                         Dictionaries
#Dictionaries (dict) are Python's built-in key-value pair data structure, providing fast lookups by unique keys.
# They are mutable, unordered collections that allow you to store and retrieve data efficiently.
# Dictionaries are commonly used for tasks such as data storage, configuration management, and data retrieval.
# They are versatile and can be used for various purposes, such as storing mappings of keys to values,
# implementing caches, or managing collections of related data.
# Dictionaries are a fundamental data structure in Python and are widely used in programming.
# Dictionaries do not allow duplicate keys, meaning each key must be unique.

Syntax:
# my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
# my_dict = dict(key1="value1", key2="value2", key3="value3")
# They can grow and shrink in size, and elements can be accessed by their keys
# Access elements by key


=========================================================================================================

"""


# Example of a dictionary
shopping_dict = {
    "apples": 3,
    "bread": 2,
    "milk": 1
}

print(f"Original dictionary: {shopping_dict}")

# Empty dictionary
empty_dict = {}

# With initial values
user = {
    "name": "Abenet",
    "age": 30,
    "is_active": True
}

# Using dict() constructor
config = dict(server="localhost", port=8080)

print(user["name"])  # Abenet

# Safe access with get()
print(user.get("email", "abeneta@flipperschools.com"))  # Returns default if key missing

# Adding new key-value pairs
user["email"] = "abenetasnake@gmail.com"
print(f"Updated user dictionary: {user}") # {'name': 'Abenet', 'age': 30, 'is_active': True, 'email': 'abenet,asnake@gmail.com'}

# Modifying existing values or updating values
user["age"] = 31  # Update age  
print(f"User after age update: {user}")  # {'name': 'Abenet', 'age': 31, 'is_active': True, 'email': 'abenet.asnake@gmail.com'}

# removing items using pop() and clear()
user.pop("is_active")  # Remove key-value pair by key   
print(f"User after removing is_active: {user}")  # {'name': 'Abenet', 'age': 31, 'email': 'benet.asnake@gmail.com'}


"""

================================================================================================================

# The dict() constructor provides several ways to create dictionaries beyond the standard {} syntax.
# It can take keyword arguments, tuples, or lists of key-value pairs.
# Example of using dict() constructor with keyword arguments
# Using dict() constructor with keyword arguments
user = dict(name="Abenet", age=30, is_active=True)  
# Using dict() constructor with a list of tuples
user_info = dict([("name", "Abenet"), ("age", 30), ("is_active", True)])




================================================================================================================

"""

user = dict(name="Abenet", age=30, is_active=True)  
print(f"User dictionary created with dict(): {user}")  # {'name': 'Abenet', 'age': 30, 'is_active': True}
# Using dict() constructor with a list of tuples
user_info = dict([("name", "Abenet"), ("age", 30), ("is_active", True)])
print(f"User info dictionary created with list of tuples: {user_info}")  # {'name': 'Abenet', 'age': 30, 'is_active': True}

