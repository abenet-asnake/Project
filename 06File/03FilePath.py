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