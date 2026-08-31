# class Car:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         print("getting car name...")
#         return self._name

#     @name.setter
#     def name(self, name):  
#         print("setting car name...")
#         self._name = name

# bmw=Car("BMW")
# # print(bmw.__dict__)
# print(Car.name.fget)
# print(Car.name.fset)
# print(bmw.name)

# @property
# def color(self):
#     print("getting color...")

# @color.setter
# def color(self, color):
#     print("setting color...")

# print(color.fget,color.fset, color.fdel)

# the idea here is to use the property object first with getter and use the same object with setter and deleter as well, - monkey patching
# the complete property object class below
class Shoe:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        print("getting brand...")
        return self._brand

    @brand.setter
    def brand(self, brand):
        print("setting brand...")
        self._brand = brand

    @brand.deleter
    def brand(self):
        print("deleting brand...")
        del self._brand


woodland= Shoe("Woodland")
print(woodland.__dict__)
woodland.brand = "Woodland Pro"
print(woodland.__dict__)
del woodland.brand
print(woodland.__dict__)