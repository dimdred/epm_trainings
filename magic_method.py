class A:
    def __init__(self):
        self.__a = 1
    def __getattr__(self, name): #must be declare! getattr and setattr woudn`t work
        if name in ('a', 'b'):
            return self.__a

o = A()
#print o.a
#print o.b

print getattr(o,'a')
setattr(o, 'a', 5)
print o.a
print o.__dict__

class A1(object):
    __slots__ = ("a",)
    def __init__(self):
        self.a = 1
obj = A1()
obj.a = 1
print obj.a
#obj.b = 1

class A2(object):
    def __init__(self):
        self.__a = None
    def getx(self):
        return self.__a
    def setx(self, value):
        self.__a = value
    def delx(self):
        del self.__a

    x = property(getx, setx, delx, "'x' property")
o = A2()
o.x = 1
print o.x
print o.__dict__