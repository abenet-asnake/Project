import os
"""
=================================================================================================================
                                   import os 
                                   Reading file 

                                   'r' mode is used to read only the file.
                                   'r+' mode is used to read and write the file.
                                   'w' mode is used to write to the file.
                    'w+' mode is used to read and write the file, but it will overwrite the file if it exists.
                                      'a' mode is used to append to the file.
                                      'a+' mode is used to read and append to the file.
                                      'x' mode is used to create a new file, if it already exists it will raise an error.
                                      'b' mode is used to read or write binary files.
                                      't' mode is used to read or write text files (default).


=================================================================================================================

"""

# Reading a file with the entire file at once
file_path = r"c:/Users/KIIT01/Desktop/Project BOX/Pythons/Project/06File/data.text"


with open(file_path, "r") as file:
    content = file.read()
    print("File content (entire file):")
    print(content)


# Reading a file line by line
with open(file_path, "r") as file:
    print("\nFile content (line by line):")
    for line in file:
        print(line.strip())  # Using strip() to remove leading/trailing whitespace 


# Reading a file into a list of lines
with open(file_path, "r") as file:
    lines = file.readlines()
    print("\nFile content (as a list of lines):")
    for line in lines:
        print(line.strip())  # Using strip() to remove leading/trailing whitespace


# Reading a file with a specific encoding
with open(file_path, "r", encoding="utf-8") as file:
    content_utf8 = file.read()
    print("\nFile content (with UTF-8 encoding):")
    print(content_utf8) # Note: Adjust the encoding as needed based on your file's encoding


# Reading a file with error handling
try:
    with open(file_path, "r") as file:
        content_with_error_handling = file.read()
        print("\nFile content (with error handling):")
        print(content_with_error_handling)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")