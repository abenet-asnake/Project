import os
"""
=================================================================================================================
                                   import os 
                                   Writing  file 

        # 'w' mode is used to write to the file.
        # 'w+' mode is used to read and write the file, but it will overwrite
        file.write("This is a new line.\n")
        file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])  # Writing multiple lines
        file.flush()  # Flush the write buffer to the file


=================================================================================================================

"""

file_path = r"c:/Users/KIIT01/Desktop/Project BOX/Pythons/Project/06File/data.text"

# Writing to a file
with open(file_path, "w") as file:
    file.write("This is a new line.\n")
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])  # Writing multiple lines
    file.flush()  # Flush the write buffer to the file