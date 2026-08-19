class Car:
    def __init__(self, color):
        self.set_color(color)  # we can even set the validation here itself

    def get_color(self):
        print("getter called")
        return self._color

    def set_color(self, color):
        print("setter called")
        if isinstance(color, str) and len(color.strip()) > 0:
            self._color = color.strip()
        else:
            raise ValueError("color should be a non empty string")

    color = property(fget=get_color, fset=set_color)


jaguar = Car("GREEN")
print(jaguar.color)
# jaguar.color = "BLACK"
# print(jaguar.color)
# # let's try an invalid color
# try:
#     jaguar.color = ""
# except ValueError as ex:
#     print(ex)
# try:
#     jaguar.color = 200
# except ValueError as ex:
#     print(ex)
# # but the private var is still accessible and can be changed with direct interaction
# print(jaguar.__dict__)
# jaguar._color = 500
# print(jaguar.__dict__)
# print(jaguar.color)
