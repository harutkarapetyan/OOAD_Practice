from abc import ABC, abstractmethod

# Abstract class for healthcare operations
class HealthcareOperation(ABC):
    @abstractmethod
    def schedule_appointment(self, appointment):
        pass

    @abstractmethod
    def view_medical_history(self):
        pass

# Concrete classes for different types of appointments
class InPersonAppointment(HealthcareOperation):
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def schedule_appointment(self, appointment):
        pass

    def view_medical_history(self):
        print(f"Medical history for In-Person Appointment (Doctor: {self.doctor.name}):")
        print(f"- Patient: {self.patient.name}")

class VirtualAppointment(HealthcareOperation):
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def schedule_appointment(self, appointment):
        pass

    def view_medical_history(self):
        print(f"Medical history for Virtual Appointment (Doctor: {self.doctor.name}):")
        print(f"- Patient: {self.patient.name}")
