from abc import ABC, abstractmethod

class Coffee(ABC):

    @property
    @abstractmethod
    def Description(self):
        pass

    @abstractmethod
    def getDescription(self):
        return self.Description

    @abstractmethod
    def cost(self):
        pass

class Expresso(Coffee):

    Description = "Expresso Shot"

    def getDescription(self):
        return self.Description

    def cost(self):
        return 5

class Dalgona(Coffee):

    Description = "Dalgona Shot"

    def getDescription(self):
        return self.Description

    def cost(self):
        return 10


class coffeeDecorator(Coffee): #Also abstract class

    _coffee : Coffee = None
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @property
    def coffee(self):
        return self._coffee

    def getDescription(self):
        pass


class Sugar(coffeeDecorator):

    Description = "Coffee + Sugar"

    def cost(self):
        return self.coffee.cost() + 1.5

    def getDescription(self):
        return self.Description


if __name__ == "__main__":
    ParshvawithCoffee = Expresso()

    print(ParshvawithCoffee.cost())
    print(ParshvawithCoffee.getDescription())

    ParshvawithCoffeewithSugar = Sugar(ParshvawithCoffee)
    print(ParshvawithCoffeewithSugar.cost())
    print(ParshvawithCoffeewithSugar.getDescription())

