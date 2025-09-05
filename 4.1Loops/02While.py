# simple Calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero error"

while True:
    print("Select operation:")
    print("1. Press one to Add")
    print("2. Press two to Subtract")
    print("3. Press three to Multiply")
    print("4. Press four to Divide")
    print("5. Press five to Exit \n")

    choice = input("Enter choice (1/2/3/4/5): \n")

    if choice == '5':
        print("Exiting the calculator....")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}\n")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}\n")
    else:
        print("Invalid choice. Please select a valid operation.\n")