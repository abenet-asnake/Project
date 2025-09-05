# ===============================================
# Student Grade Management System
# ===============================================
# Features:
# 1. Add students and assign grades
# 2. View all students
# 3. Calculate average, highest, and lowest marks
# 4. Save data into a file (students.txt)
# 5. Load data back from the file
# ===============================================

# Store all students in a list of dictionaries
students = []

# -------------------------
# Function: Grade Assignment
# -------------------------
def assign_grade(marks):
    """Return grade based on marks."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# -------------------------
# Function: Add Student
# -------------------------
def add_student():
    """Add a student with name and marks."""
    name = input("Enter student name: ")
    try:
        marks = int(input("Enter marks (0–100): "))
        if marks < 0 or marks > 100:
            print("❌ Marks must be between 0 and 100.\n")
            return
    except ValueError:
        print("❌ Invalid input! Marks must be a number.\n")
        return
    
    grade = assign_grade(marks)
    students.append({"name": name, "marks": marks, "grade": grade})
    print(f"✅ Student '{name}' added successfully!\n")

# -------------------------
# Function: View Students
# -------------------------
def view_students():
    """Display all students in a formatted table."""
    if not students:
        print("📂 No students available.\n")
        return
    
    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}")
    print("-----------------------\n")

# -------------------------
# Function: Statistics
# -------------------------
def show_statistics():
    """Show average, highest, and lowest marks."""
    if not students:
        print("📂 No data to calculate statistics.\n")
        return
    
    marks_list = [s["marks"] for s in students]
    avg = sum(marks_list) / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)
    
    print("\n📊 Class Statistics:")
    print(f"Average Marks: {avg:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}\n")

# -------------------------
# Function: Save Data
# -------------------------
def save_data():
    """Save all student records into a file."""
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['marks']},{s['grade']}\n")
    print("💾 Data saved successfully into students.txt\n")

# -------------------------
# Function: Load Data
# -------------------------
def load_data():
    """Load student records from file."""
    students.clear()
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, marks, grade = line.strip().split(",")
                students.append({"name": name, "marks": int(marks), "grade": grade})
        print("📂 Data loaded successfully from students.txt\n")
    except FileNotFoundError:
        print("❌ No saved data found. Please save first.\n")

# -------------------------
# Main Program Loop
# -------------------------
def main():
    while True:
        print("===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Statistics (Average, Highest, Lowest)")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            save_data()
        elif choice == "5":
            load_data()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
