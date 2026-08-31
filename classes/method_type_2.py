class Car:
    def __init__(self, brand):
        self.brand = brand

bmw=Car("BMW")
jaguar=Car("Jaguar")
print(bmw.__dict__,jaguar.__dict__)

#creating a method dynamically and binding it to an instance of the class - the first arg is passed as self to the method and the second arg is passed as v to the method.
# this is nothing but just simulating the method of the class and binding it to the instance of the class at runtime in the object namespace.
from types import MethodType
bmw.drive=MethodType(lambda self, v: f"driving {self.brand, v.brand}", Car)
print(bmw.drive(jaguar))

# creating a normal function here have to call it with the instance of the class as first argument
bmw.normal_drive=lambda self, v: f"driving {self.brand, v.brand}"

# bmw.normal_drive(jaguar)

# print(type(bmw.normal_drive),type(bmw.drive),type(bmw.__init__), type(Car.__init__))