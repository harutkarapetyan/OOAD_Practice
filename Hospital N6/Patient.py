from validate_decorators import validate_non_empty_string, validate_positive_number

class Patient:
    @validate_positive_number("age")
    @validate_non_empty_string("name")
    @validate_non_empty_string("medical_history")
    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history

    def view_patient_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Medical History: {self.medical_history}")