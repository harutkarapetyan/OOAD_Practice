from validate_decorators import validate_non_empty_string, validate_email
class Doctor:
    @validate_email("contact_info")
    @validate_non_empty_string("name")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def manage_patient_info(self, patient):
        print(f"{self.name} is managing patient information for {patient.name}")

    def manage_appointment(self, patient, date, time):
        print(f"{self.name} is scheduling an appointment for {patient.name} on {date} at {time}")
