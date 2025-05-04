class HospitalLedger:
    def __init__(self):
        self.patients = {}
        self.next_patient_id = 1

    def add_patient(self, name, disease):
        patient_id = self.next_patient_id
        self.patients[patient_id] = {"name": name, "disease": disease, "history": []}
        self.next_patient_id += 1
        print(f"Patient '{name}' added with ID: {patient_id}")
        return patient_id

    def record_visit(self, patient_id, date, notes):
        if patient_id in self.patients:
            self.patients[patient_id]["history"].append({"date": date, "notes": notes})
            print(f"Visit recorded for Patient ID {patient_id} on {date}")
        else:
            print(f"Patient ID {patient_id} not found.")

    def get_patient_details(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            print(f"\n--- Patient Details for ID: {patient_id} ---")
            print(f"Name: {patient['name']}")
            print(f"Disease: {patient['disease']}")
            if patient['history']:
                print("\n--- Visit History ---")
                for visit in patient['history']:
                    print(f"Date: {visit['date']}, Notes: {visit['notes']}")
            else:
                print("No visit history available.")
        else:
            print(f"Patient ID {patient_id} not found.")

    def list_all_patients(self):
        if self.patients:
            print("\n--- All Patients ---")
            for patient_id, details in self.patients.items():
                print(f"ID: {patient_id}, Name: {details['name']}, Disease: {details['disease']}")
        else:
            print("No patients in the ledger.")

# Example Usage
ledger = HospitalLedger()

patient1_id = ledger.add_patient("Alice Smith", "Flu")
patient2_id = ledger.add_patient("Bob Johnson", "Fractured Arm")

ledger.record_visit(patient1_id, "2025-05-04", "Initial check-up, prescribed rest and fluids.")
ledger.record_visit(patient1_id, "2025-05-06", "Follow-up, temperature reduced.")
ledger.record_visit(patient2_id, "2025-05-04", "Applied cast, scheduled for X-ray.")

ledger.get_patient_details(patient1_id)
ledger.get_patient_details(patient2_id)

ledger.list_all_patients() 