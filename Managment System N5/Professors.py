from validate_decorators import validate_non_empty_string, validate_email
from Courses import UndergraduateCourse, GraduateCourse

class Professor:
    @validate_email("contact_info")
    @validate_non_empty_string("name")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def create_course(self, name, content, course_type, students=[]):
        if course_type == "Undergraduate":
            course = UndergraduateCourse(name, self, content)
        else:
            course = GraduateCourse(name, self, content)

        for student in students:
            course.add_student(student)

        return course

    def manage_course(self, course):
        course.display_info()