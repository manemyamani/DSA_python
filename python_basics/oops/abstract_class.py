from abc import ABC,abstractmethod
class Computer(ABC): #abstract class
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def type(self):
        pass
class Laptop(Computer):
    def process(self):
        print("its processing") # we also need to implement the type method also,then only we can create object of it.
class Desktop(Laptop):
    def type(self):
        print("its typing")
lap=Desktop()
lap.process()