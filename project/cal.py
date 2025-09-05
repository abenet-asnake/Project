def calculator():
    print("Simple Calculator")
    print("Enter numbers one by one. Type '=' to finish and choose operation.")

    numbers = []
    while True:
        val = input("Enter number (or '=' to finish): ")
        if val == "=":
            break
        try:
            num = float(val)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or '='.")

    if not numbers:
        print("No numbers entered.")
        return

    op = input("Choose operation (+, -, *, /): ")
    if op not in ["+", "-", "*", "/"]:
        print("Invalid operation.")
        return

    result = numbers[0]
    for num in numbers[1:]:
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        elif op == "*":
            result *= num
        elif op == "/":
            if num == 0:
                print("Error: Division by zero.")
                return
            result /= num

    print(f"Result: {result}")

calculator()