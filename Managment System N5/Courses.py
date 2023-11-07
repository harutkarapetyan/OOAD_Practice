from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name, instructor, content):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def display_info(self):
        print(f"Course Name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Content: {self.content}")
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student.name}")

    @abstractmethod
    def assign_assignment(self, student, assignment):
        pass

class UndergraduateCourse(Course):
    def assign_assignment(self, student, assignment):
        print(f"{student.name} submitted an assignment for the {self.name} course.")

class GraduateCourse(Course):
    def assign_assignment(self, student, assignment):
        print(f"{student.name} submitted an advanced assignment for the {self.name} course.")


class Assignment(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def display_info(self):
        pass

class RegularAssignment(Assignment):
    def display_info(self):
        print(f"Assignment Name: {self.name}")
        print(f"Description: {self.description}")

class AdvancedAssignment(Assignment):
    def display_info(self):
        print(f"Advanced Assignment Name: {self.name}")
        print(f"Description: {self.description}")