from validate_decorators import validate_non_empty_string, validate_email
class Student:
    @validate_email("contact_info")
    @validate_non_empty_string("name")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def enroll_course(self, course):
        course.add_student(self)

    def view_progress(self):
        print(f"Student Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")
