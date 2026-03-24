from pydantic import BaseModel, EmailStr, computed_field
from typing import Dict, List

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: str
    age: int
    weight: float
    height: float
    married: bool
    address: Address
    allergies: List[str]
    contact_info: Dict[str, str]

address_dict = {'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip_code': '12345'}
address = Address(**address_dict)


patient_info1 = {'name': 'John Doe', 'email': 'john.doe@dbbl.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'age': 10, 'weight': 70.5, 'height': 175.0, 'married': True, 'address': address, 'allergies': ['penicillin'], 'contact_info': {'phone': '123-456-7890', 'emergency_contact': '123-456-7891'}}
patient1 = Patient(**patient_info1)

def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient LinkedIn URL: {patient.linkedin_url}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Height: {patient.height}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Address: {patient.address.street}, {patient.address.city}, {patient.address.state} {patient.address.zip_code}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Info: {patient.contact_info}")
    print("Data inserted successfully.")

def update_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Height: {patient.height}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Address: {patient.address.street}, {patient.address.city}, {patient.address.state} {patient.address.zip_code}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Info: {patient.contact_info}")
    print("Data updated successfully.")

insert_patient_data(patient1)


# Benifits of Nested Models:
# 1. Reusability: The Address model can be reused across different parts of the application, such as for doctors, hospitals, or other entities that require address information.
# 2. Modularity: Nested models help in organizing the code better by separating concerns. This makes the codebase easier to maintain and understand.
# 3. Validation: Each model can have its own validation logic, ensuring that the data is consistent and valid at each level. For example, the Address model can validate that the zip code is in the correct format, while the Patient model can validate that the age is within a reasonable range.
# 4. Clarity: Using nested models can make the structure of the data clearer, especially when dealing with complex data structures. It allows developers to see the relationships between different pieces of data more easily.
