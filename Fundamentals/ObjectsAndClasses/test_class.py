class MyClassIsPerson:
    def __init__(self, first_name, last_name, age=25):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f'Hello {self.first_name} {self.last_name}'


ivan = MyClassIsPerson('Ivan', 'Ivanov')
maria = MyClassIsPerson('Maria', 'Ivanova')
plamen = MyClassIsPerson('Plamen', 'Plamenov')

print(ivan.say_hello())
print(maria.say_hello())
print(plamen.say_hello())
