# Base class
class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class: Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class: Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class: Bird
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"

# Example usage
if _name_ == "_main_":
    dog = Dog("dog")
    cat = Cat("cat")
    bird = Bird("bird")

    print(dog.speak())
    print(cat.speak())   
    print(bird.speak())
