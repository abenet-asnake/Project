from typing import List, Dict, TypeAlias    

# Type alias for a student record (dictionary) and list of records
type StudentRecord = Dict[str, str | int | float]
type StudentList = List[StudentRecord]

# Initialize a list of dictionaries (versatile for structured data storage)
students: StudentList = [
    {"id": 1001, "name": "Alice Smith", "grade": 92.5},
    {"id": 1002, "name": "Bob Jones", "grade": 88.0},
    {"id": 1003, "name": "Charlie Brown", "grade": 95.0}
]  # Lists and dictionaries are fundamental for data processing

def write_students_to_file(students: StudentList, filename: str) -> None:
    # Open file in write mode ('w') with context manager for safety
    with open(filename, 'w') as file:  # Versatile for saving collections
        # Write header
        file.write("ID,Name,Grade\n")  # Structured CSV-like format
        # Iterate over students (lists and dictionaries are iterable)
        for student in students:
            # Format each record as CSV line
            line = f"{student['id']},{student['name']},{student['grade']}\n"
            file.write(line)  # Write each line to file

# Write to file
write_students_to_file(students, "students.csv")  # Real-world usage: saving data
print("After writing to file:")

# Read back the file to verify
file_path = r"c:/Users/KIIT01/Desktop/Project BOX/Pythons/Project/students.csv"
print("Reading back the file to verify:")
# Function to read student records from a file

try:
    with open(file_path, "r") as file:
        content_with_error_handling = file.read()
        print("\nFile content (with error handling):")
        print(content_with_error_handling)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")