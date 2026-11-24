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

    def view_student_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Enrollment Status:", self.is_enrolled)


# Manually create students
s1 = Student(101, "Rahim Ahmed", "CSE", True)
s2 = Student(102, "Karim Hasan", "EEE", False)
s3 = Student(103, "Sakib Hasan", "BBA", True)


# Menu-driven system
while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== All Students =====")

        for student in StudentDatabase.student_list:
            student.view_student_info()
            print("----------------------")

    elif choice == "2":
        student_id = int(input("Enter Student ID to enroll: "))

        found = False

        for student in StudentDatabase.student_list:
            if student.student_id == student_id:
                student.enroll_student()
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "3":
        student_id = int(input("Enter Student ID to drop: "))

        found = False

        for student in StudentDatabase.student_list:
            if student.student_id == student_id:
                student.drop_student()
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "4":
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")