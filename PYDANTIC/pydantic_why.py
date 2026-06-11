from pydantic import BaseModel 
from typing import List , Dict , Optional
class Patient(BaseModel):
    id : str
    name : str
    age : int
    height : float
    weight : float
    bmi : Optional[float] = None
    married : bool
    allergies: Optional[List[str]] = None #optional field aise set krte hai jab value nhi present hogi to none show hoga 
    contact_details : Dict[str,str]

def insert_patient_data(patient : Patient):
    print(f"Inserting patient data: {patient}")
    print(f"Patient ID: {patient.id}")
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Height: {patient.height}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient BMI: {patient.bmi}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Details: {patient.contact_details}")



patient_info = {'id' : 'P001' , 'name' : 'John Doe' , 'age' : 30 , 'height' : 175.5 , 'weight' : 70.2 , 'bmi' : 22.8 , 'married' : True , 'allergies' : ['pollen' , 'dust'] , 'contact_details' : {'email' : 'abcd@gamil.com' , 'phone' : '1234567890'} }


patient1 = Patient(**patient_info)

insert_patient_data(patient1)