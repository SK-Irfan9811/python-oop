# Using properties to create read-only attributes in Python
from typing import List


class Circle:
    def __init__(self, radius: float):
        self._radius = radius  # private attribute
        self._area = None

    @property
    def radius(self) -> float:
        """Get the radius of the circle."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Set the radius of the circle with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value
        self._area = None  # Reset area since radius has changed

    @property
    def area(self) -> float:
        """Calculate and return the area of the circle."""
        if self._area is None:
            print("cache invalidated, calculating area...")
            self._area = 3.14159 * (self._radius ** 2)
        return self._area

c1=Circle(5)
print(c1.area)
print(c1.area)
c1.radius=10
print(c1.area)