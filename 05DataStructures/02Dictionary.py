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