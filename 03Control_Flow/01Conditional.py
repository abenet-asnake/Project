# =============================================
#           CONDITIONAL STATEMENTS IN PYTHON
# Conditional statements allow you to execute code based on certain conditions.
# =============================================

# 1. Basic If Statement
age = 20
if age >= 18:
    print("You are an adult.")  # This will execute if age is 18 or older   

# 2. If-Else Statement
if age < 18:
    print("You are a Teenager.")  # This will execute if age is less than 18   
else:
    print("You are an Adult.")  # This will execute if age is 18 or older 

# 3. If-Elif-Else Statement
marks = 85  
if marks >= 90:
    print("Grade: A")   
elif marks >= 80:
    print("Grade: B")   
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")        

# 4. Nested If Statements
# Check if a number is positive, negative, or zero
number = -5 
if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")        
else:
    print("Zero")           

# 5. Practical Example
# Check if a user is eligible to vote based on age and citizenship  
# Assuming the user is a citizen and at least 18 years old
# This is a practical example of using conditional statements
is_citizen = True   
is_eligible = age >= 18 and is_citizen
if is_eligible:
    print("You are eligible to vote.")  # This will execute if both conditions are True
else:
    print("You are not eligible to vote.")      
       




