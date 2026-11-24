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

    def drop_student(self):
        self.is_enrolled = False

    def view_student_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Enrollment Status:", self.is_enrolled)


# Create Student object
s1 = Student(101, "Rahim Ahmed", "CSE", True)

# Display student information
s1.view_student_info()