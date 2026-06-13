#This is a sample code to demonstrate the use of field validators in Pydantic models. Field validators are used to validate and transform the values of fields in a Pydantic model. In this example, we have defined a Patient model with various fields such as name, email, age, weight, married, allergies, and contact_details. We have also defined three field validators for the email, name, and age fields.

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Field validator for the email field and what it does is to check if the email domain is in the list of valid domains. If not, it raises a ValueError. This ensures that only emails from specific domains are accepted.
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    # Field validator for the name field and what it does is to transform the name value to uppercase. This ensures that the name is always stored in uppercase format in the model.
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    # Field validator for the age field and what it does is to check if the age value is between 0 and 100. If not, it raises a ValueError. This ensures that the age value is always within a valid range.
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion here is happening, age is string but it will be converted to int because of type hinting

update_patient_data(patient1)