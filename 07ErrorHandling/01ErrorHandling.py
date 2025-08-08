"""
===========================================================================================

Error Handling in Python

================================================

"""
def divide_numbers(num1: float, num2: float) -> float:
    """
    Divides two numbers and handles division by zero error.
    
    :param num1: The numerator.
    :param num2: The denominator.
    :return: The result of the division.

    """
    try:
        result = num1 / num2
        print(f"{num1} divided by {num2} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both values must be numbers.")
    finally:
        print("Division operation complete.")


divide_numbers(5,6)