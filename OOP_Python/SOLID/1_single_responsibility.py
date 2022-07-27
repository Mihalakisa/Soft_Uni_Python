class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_name(self):
        return self.name


class StudentRecords:
    @staticmethod
    def get_student(id):
        with open("students.txt", "r") as file:
            for line in file.readlines():
                if str(id) == line.split()[0]:
                    return line

    @staticmethod
    def register(student):
        with open("students.txt", "a") as file:
            file.write(f"{student.id} {student.name}")


# Every class is good to have < Single Responsibility >

student = Student(1, "Test")
student_2 = Student(2, "Test 2")

record = StudentRecords()
