from pydantic import BaseModel, EmailStr, model_validator
from typing import Dict, List

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, values):
        if values.age > 60 or values.age < 18 and 'emergency_contact' not in values.contact_info:
            raise ValueError("Emergency contact information is required for patients under 18.")
        return values


patient_info1 = {'name': 'John Doe', 'email': 'john.doe@dbbl.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'age': 10, 'weight': 70.5, 'married': True, 'allergies': ['penicillin'], 'contact_info': {'phone': '123-456-7890', 'emergency_contact': '123-456-7891'}}
patient1 = Patient(**patient_info1)

def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient LinkedIn URL: {patient.linkedin_url}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Info: {patient.contact_info}")
    print("Data inserted successfully.")

def update_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Info: {patient.contact_info}")
    print("Data updated successfully.")

insert_patient_data(patient1)
