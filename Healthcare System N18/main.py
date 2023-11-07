from Appointment import InPersonAppointment, VirtualAppointment
from Patient import Patient
from Doctor import Doctor

if __name__ == "__main__":
    primary_care_doctor = Doctor("Dr. Smith", "drsmith@examplegmail.com", "Primary Care")
    specialist_doctor = Doctor("Dr. Johnson", "drjohnson@examplegmail.com", "Cardiology")

    in_person_appointment = InPersonAppointment(None, primary_care_doctor, "10:00 AM")
    virtual_appointment = VirtualAppointment(None, specialist_doctor, "2:30 PM")

    patient1 = Patient("Patient1", "patient1@example.com")
    patient2 = Patient("Patient2", "patient2@example.com")

    primary_care_doctor.manage_schedule(in_person_appointment)
    specialist_doctor.manage_schedule(virtual_appointment)

    in_person_appointment.patient = patient1
    virtual_appointment.patient = patient2

    in_person_appointment.view_medical_history()
    virtual_appointment.view_medical_history()

