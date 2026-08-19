# using bare attributes in class is highly discouraged
class Car:
    def __init__(self, color="WHITE"):
        self._color = color  # the _ indicates that the var is private and is not intended to use outside the class.

    # we can still use getter and setter inorder not to use private attrs directly
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    # this makes sure that color attribute can be set and get with dot notation but still uses getters and setters internally
    color = property(fget=get_color, fset=set_color)

print(Car.__dict__)
bmw = Car("YELLOW")
print(bmw.__dict__)
print(bmw.get_color())
bmw.set_color("GREEN")
print(bmw.get_color())

# now imagine a situation where the code is already written to use bare attributes and we need a mechanism to still use bare attrs
# without changing the interface code
# let's use the color property attribute
bmw.color = "BLACK"
print(bmw.color)
