"""
class ClassName:
    <statement -1>
    ...
    <statement -N>
"""
# pass - blank class. can add later
class Name1:
    pass

class MyClass:
    """A simple example class """
    i = 12345

    def f(self):
        return 'helo world'

t = MyClass()
print(t.f(),t.i)

#create object
"""
object._new_(cls[, ...]) #
object._init_(self[, ...]) #confirm filds
object._del_(self) #use with _new_ , not recomended
"""

x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)