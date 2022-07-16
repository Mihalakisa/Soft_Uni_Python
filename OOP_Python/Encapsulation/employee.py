class Employee:
    name = 'Harsh'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)


employee = Employee()
print(getattr(employee, 'name'))
print(hasattr(employee, 'name'))
setattr(employee, 'height', 152)
print(getattr(employee, 'height'))
delattr(Employee, 'salary')