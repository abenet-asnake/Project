"""
===================================================================================================================
  1. import os 
  2 pathlib import Path


==================================================================================================================

"""

import os
from pathlib import Path
# Your file paths (using raw strings for Windows paths)
csv_path = r"c:/Users/KIIT01/Desktop/Project BOX/Pythons/Project/students.csv"
text_path = r"c:/Users/KIIT01/Desktop/Project BOX/Pythons/Project/06File/data.text"


# using os.path to define a file path
print("=== Using os.path ===")
print("CSV file exists:", os.path.exists(csv_path))  # Check if files exist
print("Text file exists:", os.path.exists(text_path)) # Check if files exist

# get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)  # Display current directory

text_directory = os.path.dirname(text_path)  # Get directory of the text file
print("Text file directory:", text_directory)  # Display directory of the text file
text_file_name = os.path.basename(text_path)  # Get the file name from the path
print("Text file name:", text_file_name)  # Display the file name