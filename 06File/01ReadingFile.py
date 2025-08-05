
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
      
