# Here we are using computed_field decorator to calculate the BMI of a patient based on their weight and height. The BMI is calculated using the formula: weight (kg) / (height (m) ^ 2). The computed_field decorator allows us to define a property that is automatically calculated based on other fields in the model.

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    # Computed field for BMI and what it does is to calculate the BMI of a patient based on their weight and height. The BMI is calculated using the formula: weight (kg) / (height (m) ^ 2). The computed_field decorator allows us to define a property that is automatically calculated based on other fields in the model.
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)