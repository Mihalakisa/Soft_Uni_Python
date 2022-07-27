from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        return "Drawing rectangle"


class Circle(Shape):
    def draw(self):
        return "Drawing circle"
