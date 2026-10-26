class Animal:
    # constractor
    def __init__(self, name):
        self.name = name,
        self.is_alive = True
        
    # method
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("bark")


class Cat(Animal):
    def speak(self):
        print("mewwwwo")


class Mouse(Animal):
    pass


dog = Dog("doggy")
cat = Cat("Kitty")
mouse = Mouse("Mise")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
