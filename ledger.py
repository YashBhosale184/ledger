import streamlit as st
from datetime import date

# HospitalLedger class here
class HospitalLedger:
    def __init__(self):
        self.patients = {}
        self.next_patient_id = 1

    def add_patient(self, name, disease):
        patient_id = self.next_patient_id
        self.patients[patient_id] = {"name": name, "disease": disease, "history": []}
        self.next_patient_id += 1
        return patient_id

    def record_visit(self, patient_id, visit_date, notes):
        if patient_id in self.patients:
            self.patients[patient_id]["history"].append({"date": visit_date, "notes": notes})
            return True
        return False

    def get_patient_details(self, patient_id):
        return self.patients.get(patient_id, None)

    def list_all_patients(self):
        return self.patients

# Initialize ledger
if 'ledger' not in st.session_state:
    st.session_state.ledger = HospitalLedger()

ledger = st.session_state.ledger

# Streamlit UI
st.title("🏥 Hospital Ledger System")

menu = st.sidebar.radio("Select Action", ["Add Patient", "Record Visit", "View Patient", "List All Patients"])

if menu == "Add Patient":
    st.header("Add New Patient")
    name = st.text_input("Patient Name")
    disease = st.text_input("Disease/Condition")
    if st.button("Add Patient"):
        if name and disease:
            pid = ledger.add_patient(name, disease)
            st.success(f"Patient '{name}' added with ID: {pid}")
        else:
            st.error("Please fill in all fields.")

elif menu == "Record Visit":
    st.header("Record a Visit")
    pid = st.number_input("Patient ID", min_value=1, step=1)
    visit_date = st.date_input("Visit Date", value=date.today())
    notes = st.text_area("Visit Notes")
    if st.button("Record Visit"):
        success = ledger.record_visit(pid, str(visit_date), notes)
        if success:
            st.success(f"Visit recorded for Patient ID {pid} on {visit_date}")
        else:
            st.error("Patient ID not found.")

elif menu == "View Patient":
    st.header("View Patient Details")
    pid = st.number_input("Enter Patient ID", min_value=1, step=1)
    if st.button("Get Details"):
