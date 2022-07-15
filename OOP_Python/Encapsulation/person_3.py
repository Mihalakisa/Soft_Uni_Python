class Person:
    def __init__(self):
        self.first_name = 'Petter'
        self.last_name = 'Parker'

    def __full_name(self):
        return f"{self.first_name} {self.last_name}"

    def info(self):
        return self.__full_name()


person = Person()
print(person.info())
# print(person.__full_name())
print(person._Person__full_name())
