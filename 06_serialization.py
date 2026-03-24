from pydantic import BaseModel, EmailStr
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

# temp = patient1.model_dump(exclude={'email'}, exclude_unset=True)
temp = patient1.model_dump_json(include={'name', 'email', 'age'})
print(temp)
print(type(temp))
