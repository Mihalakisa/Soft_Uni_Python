class Person:
    value = 50

    def __init__(self):
        self.value = 30


print(Person.value)
obj = Person()
print(obj.value)
obj.value += 1
print(obj.value)
obj2 = Person()
print(obj2.value)