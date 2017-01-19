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

#method _init_(self) inside breakets propeties(svoistva)
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class T:
    def __init__(self):
        self.a = 1

o = T() #object of class
print o.a

o1 = T() #second object of class
o1.b = 3
print o1.b
#print o.b - error

#change behavior of class
#o.f()

def func(self):
    print(self)

func(o)

T.f = func
T.f(o)
o.f()

class D:
    def __init__(self):
        self.__a=1

q = D()
#print(q.__a) #error
print(q._D__a) #use private(_ _) variable a

# Inheritance

class P:
    def __init__(self):
        self.__a = 1

    def f(self):
        print "Hello!"

print(P.__dict__)
r = P()
print(r.__dict__)

class C(P):
    def __init__(self):
        self.__b = 2
        P.__init__(self)
        #super(P).__init__(self)
        P.__init__(self)
print(C.__dict__)
z = C()
print(z.__dict__)
print(z.f())

""" Not work
class C2(P):
    def __init__(self):
        P.__init__(self)
 #       super(P).__init__(self)
    def f(self):
 #       super(P, self).f()
print(C2.__dict__)
z = C2()
print(z.__dict__)
print(z.f())
"""

class A1(P):
    def __init__(self):
        #super(P).__init__(self)
        P.__init__(self)
        self.__a1 = 1

class A2(P):
    def __init__(self):
        #super(P).__init__(self)
        P.__init__(self)
        self.__a2 = 2

class B(A1, A2):
    def __init__(self):
        #super(A1).__init__(self)
        #super(A2).__init__(self)
        A1.__init__(self)
        A2.__init__(self)

o = B()
print (o.__dict__)


class A11:
    def __init__(self):
        self.a = 11
        self.__b = 11

class A22:
    def __init__(self):
        self.a = 22
        self.__b = 22

class B1(A11, A22):
    def __init__(self):
        A11.__init__(self)
        A22.__init__(self)

o = B1()
print o.__dict__ # var a rewrite