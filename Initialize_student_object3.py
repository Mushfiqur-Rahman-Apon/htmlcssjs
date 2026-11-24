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

        # Add student object to student_list
        StudentDatabase.add_student(self)


# Manually create Student objects
s1 = Student(101, "Rahim Ahmed", "CSE", True)
s2 = Student(102, "Karim Hasan", "EEE", True)

# Check student_list
for student in StudentDatabase.student_list:
    print(student.student_id, student.name,
          student.department, student.is_enrolled)