from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Model validator for the Patient model and what it does is to check if the patient is older than 60 and if they have an emergency contact in their contact_details. If the patient is older than 60 and does not have an emergency contact, it raises a ValueError. This ensures that patients older than 60 must have an emergency contact.
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
# This patient is below 60 and does not have an emergency contact, so it will not raise any error
patient_info1 = {'name':'nitish', 'email':'abc@icici.com', 'age': '35', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

# This patient is above 60 and does not have an emergency contact, so it will raise a ValueError
patient_info2 = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

# This patient is above 60 and has an emergency contact, so it will not raise any error
patient_info3 = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info1) 
patient2 = Patient(**patient_info2) 
patient3 = Patient(**patient_info3)

update_patient_data(patient1)
update_patient_data(patient2)
update_patient_data(patient3)