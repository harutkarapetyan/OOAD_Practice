from validate_decorators import validate_email, validate_non_empty_string

class JobSeeker:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info, resume):
        self.name = name
        self.contact_info = contact_info
        self.resume = resume