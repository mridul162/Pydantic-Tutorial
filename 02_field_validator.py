from pydantic import AnyUrl, BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description="Name must be a non-empty string", example="John Doe")]
    email: EmailStr = Field(description="Email must be a valid email address")
    age: int = Field(ge=0, lt=120, description="Age must be a non-negative integer")
    linkedin_url: AnyUrl = Field(description="LinkedIn URL must be a valid URL")
    weight: Annotated[float, Field(gt=0, strict=True, description="Weight must be a positive number")]
    married: Annotated[bool, Field(default=None, description="Marital status of the patient")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5, description="List of allergies")]
    contact_info: Annotated[Dict[str, str], Field(description="Contact information as a dictionary with string keys and values")]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['dbbl.com', 'city.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if value < 0 or value >= 120:
            raise ValueError("Age must be a non-negative integer less than 120")
        return value

patient_info = {'name': 'John Doe', 'email': 'john.doe@dbbl.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'age': 30, 'weight': 70.5, 'married': True, 'allergies': ['penicillin'], 'contact_info': {'phone': '123-456-7890'}}
patient1 = Patient(**patient_info)

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

# patient_info = {'name': 'John Doe', 'age': 35, 'weight': 75.0, 'married': False, 'contact_info': {'phone': '123-456-7890'}}
# patient2 = Patient(**patient_info)

# update_patient_data(patient2)