from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Cannot set name less than 2 chars")
        self.__name = value


class Cat(Animal):
    def __init__(self, name, laziness):
        super().__init__(name)
        self.laziness = laziness

    def make_sound(self):
        return "Meow!"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Bark!"


a = Cat('asd', 10)
b = Dog('asd')
print(a.make_sound())

animals = [a, b]

for animal in animals:
    print(animal.make_sound())