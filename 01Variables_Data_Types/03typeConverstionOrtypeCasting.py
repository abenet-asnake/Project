

"""
Type conversion (or type casting) is the process of converting a value from one data type to another.
 Python supports two types of conversion:

    1. Implicit Conversion (Automatically done by Python)

    2. Explicit Conversion (Manually done by the programmer)

"""
x=10
print(type(x))  # <class 'int'>
print(x)  # 10

y=str(x)  # Explicit conversion from int to str
print(type(y))  # <class 'str'>
print(y)  # '10'

z=float(x)  # Explicit conversion from int to float
print(type(z))  # <class 'float'>   

