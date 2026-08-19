# with the help of MethodType we can make an instance's method to access the object namespace at runtime.
from types import MethodType


class Car:
    brand = "Porsche"

    def __init__(self, brand="Jaguar"):
        self.brand = brand


c = Car("BMW")
print(c.brand)
c.drive = MethodType(lambda self, v: f"driving {self.brand, v.brand}", Car)
print(c.drive(Car))
