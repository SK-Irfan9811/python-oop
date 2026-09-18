class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        if hasattr(self, "_color"):
            return self._color
        return "Color attribute is not set."

    @color.setter
    def color(self, color):
        print("Setting color...")
        self._color = color

    @color.deleter
    def color(self):
        print("Deleting color...")
        del self._color

red = Color("Red")
print(red.__dict__)
red.color = "Blue"
print(red.__dict__)
del red.color
print(red.__dict__)
print(red.color)
# del Color.color
print(Color.__dict__)
red.color = "Green"
print(red.__dict__)
    