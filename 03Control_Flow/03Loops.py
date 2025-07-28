# =============================================
#           COMPLETE LOOP GUIDE IN PYTHON
#for loop, while loop, nested loop, break, continue, pass
# =============================================
# 1. For Loop
print("\n1. For Loop:") 
for i in range(5):
    print("Iteration", i)   # Output: Iteration 0 to 4  

# Practical Example
print("\nPractical Example:")       
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)  # Output: Fruit: apple, banana, cherry
# 2. While Loop
print("\n2. While Loop:")   
count = 0
while count < 5:
    print("Count:", count)  # Output: Count: 0 to 4
    count += 1              
# Practical Example
print("\nPractical Example:")       
number = 0
while number < 10:
    print("Number:", number)  # Output: Number: 0 to 9
    number += 2  # Increment by 2   
# 3. Nested Loops
print("\n3. Nested Loops:") 
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")  # Output: i=0, j=0; i=0, j=1; i=1, j=0; i=1, j=1; i=2, j=0; i=2, j=1
# Practical Example
print("\nPractical Example:")   
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for value in row:
        print("Value:", value)  # Output: Value: 1 to 9 (each element in the matrix)    

# 4. Break Statement
print("\n4. Break Statement:")  
for i in range(5):
    if i == 3:
        print("Breaking at i =", i)  # Output: Breaking at i = 3
        break  # Exit the loop when i is 3
    print("i =", i)  # Output: i = 0, 1, 2  
# Practical Example
print("\nPractical Example:")           
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 4:
        print("Found 4, breaking the loop")  # Output: Found 4, breaking the loop
        break  # Exit the loop when 4 is found
    print("Number:", num)  # Output: Number: 1, 2, 3    

# 5. Continue Statement
print("\n5. Continue Statement:")   
for i in range(5):
    if i == 2:
        print("Skipping i =", i)  # Output: Skipping i = 2
        continue  # Skip the rest of the loop when i is 2
    print("i =", i)  # Output: i = 0, 1, 3, 4   
# Practical Example
print("\nPractical Example:")   
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print("Skipping even number:", num)  # Output: Skipping even number: 2, 4
        continue  # Skip even numbers
    print("Odd Number:", num)  # Output: Odd Number: 1, 3, 5    
# 6. Pass Statement
print("\n6. Pass Statement:")   
for i in range(5):
    if i == 2:
        print("Pass at i =", i)  # Output: Pass at i = 2
        pass  # Do nothing, just a placeholder
    print("i =", i)  # Output: i = 0, 1, 2, 3, 4
# Practical Example
print("\nPractical Example:")   
for i in range(5):
    if i == 3:
        print("Pass at i =", i)  # Output: Pass at i = 3
        pass  # Placeholder, no action taken
    print("i =", i)  # Output: i = 0, 1, 2, 3, 4    

# 7. Practical Example with Break, Continue, and Pass
print("\n7. Practical Example with Break, Continue, and Pass:")
for i in range(10): 
    if i == 5:
        print("Breaking at i =", i)  # Output: Breaking at i = 5
        break  # Exit the loop when i is 5
    elif i % 2 == 0:
        print("Skipping even number:", i)  # Output: Skipping even number: 0, 2, 4
        continue  # Skip even numbers
    else:
        print("Odd Number:", i)  # Output: Odd Number: 1, 3

# 8. Practical Example with Nested Loops
print("\n8. Practical Example with Nested Loops:")  
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        if i == 1 and j == 0:
            print("Breaking inner loop at i =", i, "j =", j)  # Output: Breaking inner loop at i = 1 j = 0
            break  # Exit the inner loop when i is 1 and j is 0
        print(f"i={i}, j={j}")  # Output: i=0, j=0; i=0, j=1; i=1, j=0; i=1, j=1; i=2, j=0; i=2, j=1

# Iterate over multiple sequences together zip
print("\nIterating over multiple sequences together using zip:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")  # Output: Alice is 25 years old, Bob is 30 years old, Charlie is 35 years old
# 9. Practical Example with Enumerate
print("\n9. Practical Example with Enumerate:") 
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")  # Output: Index 0: apple, Index 1: banana, Index 2: cherry    
# 10. Practical Example with List Comprehension
print("\n10. Practical Example with List Comprehension:")   
squares = [x**2 for x in range(10)]  # Create a list of squares from 0 to 9
print("Squares:", squares)  # Output: Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

