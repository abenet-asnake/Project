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

# 6. Ternary Operator (Conditional Expression)
# A concise way to write an if-else statement
is_adult = "Yes" if age >= 18 else "No"
print(f"Is the person an adult? {is_adult}")  # Outputs "Yes" if age is 18 or older, otherwise "No"
# 7. Short-Circuit Evaluation
# Python evaluates conditions from left to right and stops as soon as the result is determined.     
# This is known as short-circuit evaluation.
# Example with AND operator 
is_raining = False
has_umbrella = True 
if is_raining and has_umbrella:
    print("You can go outside with your umbrella.") 
else:
    print("You should stay indoors or find another way to protect yourself from the rain.")     
# Example with OR operator
is_sunny = True     
has_sunglasses = False
if is_sunny or has_sunglasses:
    print("You can enjoy the weather outside.")     
else:
    print("You might need to stay indoors or find some shade.")

# 8. Practical Example with Multiple Conditions
# Check if a user can access a feature based on their role and subscription status      
user_role = "editor"
has_subscription = True
if user_role == "admin" or (user_role == "editor" and has_subscription):
    print("Access granted to the feature.")  # This will execute if user is admin or editor with subscription
else:
    print("Access denied. You do not have the required role or subscription.")  
# 9. Using Logical Operators in Conditions
# You can combine multiple conditions using logical operators (and, or, not)    
is_logged_in = True
has_permission = False  
if is_logged_in and has_permission:
    print("You can access the dashboard.")  # This will execute if both conditions are True
else:
    print("Access denied. Please log in or check your permissions.")    
# 10. Practical Example with User Input
# Check if a user can access a restricted area based on their age and security clearance level  
user_age = 25
security_clearance = "high" 
if user_age >= 21 and security_clearance == "high":
    print("Access granted to the restricted area.")  # This will execute if both conditions are True
else:
    print("Access denied. You do not meet the age or security clearance requirements.") 





