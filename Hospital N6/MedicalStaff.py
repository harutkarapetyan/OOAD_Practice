from validate_decorators import validate_non_empty_string

class MedicalStaff:
    @validate_non_empty_string("namme")
    @validate_non_empty_string("position")
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def manage_operations(self, operation, patient):
        print(f"{self.position} {self.name} is managing {operation.operation_type} for patient {patient.name}")
