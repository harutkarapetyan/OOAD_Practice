from validate_decorators import validate_non_empty_string, validate_email

class Librarian:
    @validate_email("contact_info")
    @validate_non_empty_string("name")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
