

class protected:
    def __init__(self):
        self._protectedVar = 0

class private:
    def __init__(self):
        self.__privateVar = 0
    def getPrivate(self):
        return self.__privateVar
    def setPrivate(self, value):
        self.__privateVar = value        

obj1 = protected()
obj1._protectedVar = 7
obj2 = private()
obj2.setPrivate(2002)
print("My daughter is {} years old today, she was born in {}.".format(obj1._protectedVar,obj2.getPrivate()))

