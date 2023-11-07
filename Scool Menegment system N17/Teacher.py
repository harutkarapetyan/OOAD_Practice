from validate_decorators import validate_email, validate_non_empty_string

class Teacher:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info, subject_taught):
        self.name = name
        self.contact_info = contact_info
        self.subject_taught = subject_taught

    def manage_course(self, course):
        course.teacher = self