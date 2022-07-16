class Student:
    def __init__(self, number, id_number):
        self.number = number
        self.__id_number = id_number
        self._grades = [5, 6]

    def calculate_age(self):
        year = self.__id_number[:2]
        # age = datetime.now() - year

    def get_id_number(self):
        return self.__id_number[:6] + "****"

    def set_id_number(self, value):
        if value[:2] != "90":
            raise ValueError("Only '90 students are accepted!")
        self.__id_number = value


# class UniversityStudent(Student):
#     def clc_avg_grades(self):
#         self._grades


student = Student("1234a", "2000101001")
print(student.get_id_number())
print(student._Student__id_number)
print(student._grades)
print(student.set_id_number("90001041"))
