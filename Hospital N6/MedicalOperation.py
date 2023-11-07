from abc import ABC, abstractmethod

# Abstract class for medical operations
class MedicalOperation(ABC):
    def __init__(self, operation_name, operation_type):
        self.operation_name = operation_name
        self.operation_type = operation_type

    @abstractmethod
    def perform_operation(self, patient):
        pass

# Concrete classes for different types of medical procedures
class Surgery(MedicalOperation):
    def perform_operation(self, patient):
        print(f"Performing {self.operation_type} surgery on patient {patient.name}")

class Checkup(MedicalOperation):
    def perform_operation(self, patient):
        print(f"Conducting {self.operation_type} check-up for patient {patient.name}")
