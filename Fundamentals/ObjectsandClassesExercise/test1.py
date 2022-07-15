class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        return f"Hello {self.first_name} {self.last_name}"


# obj = Person('Ivan', 'Ivanov')
obj = Person(last_name='Ivanov', first_name='Ivan')

print(obj.say_hello())