from abc import ABC, abstractmethod

class store(ABC):
    def customers(self, amount):
        print("We've had {} customer's today.".format(amount))

    @abstractmethod
    def soldUnits(self, units):
        pass

class brand(store):
    def soldUnits(self, units):
        print("Today we sold {} units today".format(units))


obj = brand()
obj.customers(30)
obj.soldUnits(7)
