"""
When a function is defined inside a class, it is a normal function.,nothing special...
But when we create an object from that class, it ofcourse creates a separate namespace in which we can see
that the function defined inside the class became method.
Basically method is something that is bound to an instance of class and the same instance is being sent as a first
param to that function.
The bound method has nothing to do with the instance namespace, it is created on demand in the stack space and gets
deleted
after the usage.The only persistence is the function defined at class level.
The bound method has 2 attrs - __self__(returns the object of itself) and __func__(reference to the original
function from the class)
"""
import inspect
import json


class Cricket:
    def __init__(self, _format):
        self._format = _format

    def play(self, overs):
        print(self, overs)
        # to know the details of what the current stack frame contains.
        # current_frame = inspect.currentframe()
        # print(f"Locals in frame: {current_frame.f_locals}")
        # print(f"Function code name: {current_frame.f_code.co_name}")
        # print(f"Current frame: {current_frame}")
        # print(f"No.of overs in this {self._format} format : {overs}")


print(Cricket.__dict__)
print(Cricket.play(100, 900))
t = Cricket("TEST")
o=Cricket("ODI")
print(t.play.__func__, t.play.__self__)
print(o.play.__func__, o.play.__self__)
print(t.__dict__)

# print(c.play.__func__, c.play.__self__)
# print(id(c))
# c.play(90)
# o = []
# print(bool(o and all(o)))


# class MyClass:
#     def __init__(self, var):
#         self.var = var


# print(MyClass.__init__)
# o = MyClass(2)
# print(o.__init__)
