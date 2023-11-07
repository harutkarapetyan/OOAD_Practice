from Courses import RegularAssignment, AdvancedAssignment
from Professors import Professor
from Students import Student

if __name__ == "__main__":

    professor = Professor("Professor Smith", "prof.smith@examplegmail.com")
    student1 = Student("Alice", "alice@examplegmail.com")
    student2 = Student("Bob", "bob@examplegmail.com")

    undergrad_course = professor.create_course("Introduction to Programming", "Basic curriculum for undergraduates", "Undergraduate", [student1, student2])
    grad_course = professor.create_course("Advanced Algorithms", "Advanced curriculum for graduates", "Graduate", [student2])

    student1.enroll_course(undergrad_course)
    student2.enroll_course(undergrad_course)
    student2.enroll_course(grad_course)

    professor.manage_course(undergrad_course)
    professor.manage_course(grad_course)

    student1.view_progress()
    student2.view_progress()

    assignment1 = RegularAssignment("Homework 1", "Complete exercises 1-5")
    assignment2 = AdvancedAssignment("Research Paper", "Write a research paper on advanced algorithms")

    undergrad_course.assign_assignment(student1, assignment1)
    grad_course.assign_assignment(student2, assignment2)








