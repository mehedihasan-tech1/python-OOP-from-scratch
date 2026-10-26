"""Multilevel inheritence: inherit from a parent which inherit from another parent"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"this {self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Mouse")
hawk = Hawk("hauk")
fish = Fish("salmon")

rabbit.eat()
fish.sleep()
