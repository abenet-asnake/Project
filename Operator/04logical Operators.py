# =============================================
#           LOGICAL OPERATORS IN PYTHON
# =============================================

# 1. AND Operator (Returns True if BOTH conditions are True)
print("\n1. AND Operator (both conditions must be True):")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("False and True:", False and True)   # False
print("False and False:", False and False) # False

# Practical Example
age = 25
has_license = True
print("\nCan drive?:", age >= 18 and has_license)  # True (both conditions met)

# 2. OR Operator (Returns True if AT LEAST ONE condition is True)
print("\n2. OR Operator (at least one True):")
print("True or True:", True or True)       # True
print("True or False:", True or False)     # True
print("False or True:", False or True)     # True
print("False or False:", False or False)   # False

# Practical Example
has_cash = False
has_card = True
print("\nCan make payment?:", has_cash or has_card)  # True (card available)

# 3. NOT Operator (Reverses the boolean value)
print("\n3. NOT Operator (inverts the value):")
print("not True:", not True)               # False
print("not False:", not False)             # True

# Practical Example
is_raining = False
print("\nShould take umbrella?:", not is_raining)  # True (since it's NOT raining)

# 4. Combined Logical Operators
print("\n4. Combined Operators:")
# Example: Eligible for discount if (member OR over 65) AND has coupon
is_member = True
age = 70
has_coupon = False

eligible = (is_member or age >= 65) and has_coupon
print("Discount eligible?:", eligible)  # False (no coupon)

# 5. Truthy/Falsy Evaluation
print("\n5. Truthy/Falsy Evaluation:")
# Falsy values: None, False, 0, "", [], {}, etc.
name = ""
print("not name:", not name)  # True (empty string is Falsy)

value = 10
print("value and 100:", value and 100)  # 100 (returns last Truthy value)

# 6. Short-Circuiting Behavior
print("\n6. Short-Circuiting:")
def check():
    print("Function was called!")
    return True

print("False and check():", False and check())  # check() never runs (short-circuited)
print("True or check():", True or check())      # check() never runs (short-circuited)
