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
    