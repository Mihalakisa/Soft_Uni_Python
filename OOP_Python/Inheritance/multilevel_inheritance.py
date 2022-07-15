class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address


grand_child = GrandChild('Grand Name', 19, 'Address 15-17')
print(grand_child.name)
print(grand_child.age)
print(grand_child.address)