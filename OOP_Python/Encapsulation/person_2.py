class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than zero")
        self.__age = value


p = Person("test", 5)
print(p.age)
try:
    p.age = 0
except Exception:
    print(p.age)
