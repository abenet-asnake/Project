# Enums (short for Enumerations) in Python are a way to define a set of valued constant values. 

from enum import Enum

class MathOperation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

print(MathOperation.ADD)
print(MathOperation.SUBTRACT)
print(MathOperation.MULTIPLY)
print(MathOperation.DIVIDE)

print(MathOperation.ADD.value)
print(MathOperation.SUBTRACT.value)
print(MathOperation.MULTIPLY.value)
print(MathOperation.DIVIDE.value)

for operation in MathOperation:
    print(operation.name, operation.value)