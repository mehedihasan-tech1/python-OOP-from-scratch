
"""Abstract Class: A class that cannot be instantiated on its own; Meant to be subclassed. 
    They can contain abstract methods, which are declared but have no implementation. Abstract class benefits:
    1. Prevents instantiation of the class itself
    2. Requires children to use inherited abstract methods
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("you drive the car")


    def stop(self):
        print("you stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")


motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()
