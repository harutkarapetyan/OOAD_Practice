from Student import Student 
from Teacher import Teacher
from Course import MathCourse, EnglishCourse

if __name__ == "__main__":
    math_teacher = Teacher("Math Teacher", "mathteacher@example.com", "Math")
    english_teacher = Teacher("English Teacher", "englishteacher@example.com", "English")

    math_course = MathCourse("Math 101", math_teacher)
    english_course = EnglishCourse("English 101", english_teacher)

    student1 = Student("Student1", "student1@example.com")
    student2 = Student("Student2", "student2@example.com")

    math_teacher.manage_course(math_course)
    english_teacher.manage_course(english_course)

    math_course.enroll_student(student1)
    english_course.enroll_student(student2)

    math_course.view_progress()
    english_course.view_progress()
