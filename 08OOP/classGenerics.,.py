from typing import TypeVar, Generic

T = TypeVar('T', int, float)  # T can be int or float

class Calculator(Generic[T]):
    def __init__(self, value1: T, value2: T):
        self.value1 = value1
        self.value2 = value2

    def add(self) -> T:
        return self.value1 + self.value2

    def multiply(self) -> T:
        return self.value1 * self.value2

# Usage
calc_int = Calculator(3, 5)
print("Int Add:", calc_int.add())
print("Int Multiply:", calc_int.multiply())

calc_float = Calculator(2.5, 4.0)
print("Float Add:", calc_float.add())
print("Float Multiply:", calc_float.multiply())