class Person:

    species = 'mammal'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name


ivan = Person('Ivan', 'Ivanov', 33)
maria = Person('Maria', 'Ivanova', 22)
print(ivan.species)
print(maria.species)
