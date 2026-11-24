class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print("Student enrolled successfully!")
        else:
            print("Student is already enrolled!")

    def drop_student(self):
        self.is_enrolled = False
        print("Student dropped successfully!")


# Create Student object
s1 = Student(101, "Rahim Ahmed", "CSE", True)

# Drop student
s1.drop_student()

print(s1.is_enrolled)