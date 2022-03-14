

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

obj1 = protected()#instantiates the protected class
obj1._protectedVar = 7#changes the value of the protected class
obj2 = private()#instantiates the private class
obj2.setPrivate(2002)#changes the varible within private
#access both changed values in the following print statement
print("My daughter is {} years old today, she was born in {}.".format(obj1._protectedVar,obj2.getPrivate()))

