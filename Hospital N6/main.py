from MedicalOperation import Surgery, Checkup
from Doctor import Doctor
from Patient import Patient
from MedicalStaff import MedicalStaff

if __name__ == "__main__":
    
    patient1 = Patient("Alice", 30, "Allergies")
    patient2 = Patient("Bob", 45, "Diabetes")

    doctor1 = Doctor("Dr. Smith", "dr.smith@example.com")
    doctor2 = Doctor("Dr. Johnson", "dr.johnson@example.com")

    surgery = Surgery("Appendectomy", "surgery")
    checkup = Checkup("Annual", "check-up")

    medical_staff1 = MedicalStaff("Nurse Linda", "Nurse")
    medical_staff2 = MedicalStaff("Administrator Sarah", "Administrator")

    doctor1.manage_patient_info(patient1)
    doctor2.manage_appointment(patient2, "2023-11-15", "10:00 AM")

    patient1.view_patient_info()
    patient2.view_patient_info()

    surgery.perform_operation(patient1)
    checkup.perform_operation(patient2)

    medical_staff1.manage_operations(surgery, patient1)
    medical_staff2.manage_operations(checkup, patient2)

