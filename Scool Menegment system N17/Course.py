from abc import ABC, abstractmethod

# Abstract class for school operations
class SchoolOperation(ABC):
    @abstractmethod
    def enroll_student(self, student):
        pass

    @abstractmethod
    def view_progress(self):
        pass

# Concrete classes for different types of courses
class MathCourse(SchoolOperation):
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.enrolled_students = []

    def enroll_student(self, student):
        self.enrolled_students.append(student)

    def view_progress(self):
        print(f"Progress for Math Course (Teacher: {self.teacher.name}):")
        for student in self.enrolled_students:
            print(f"- Student: {student.name}")

class EnglishCourse(SchoolOperation):
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.enrolled_students = []

    def enroll_student(self, student):
        self.enrolled_students.append(student)

    def view_progress(self):
        print(f"Progress for English Course (Teacher: {self.teacher.name}):")
        for student in self.enrolled_students:
            print(f"- Student: {student.name}")
