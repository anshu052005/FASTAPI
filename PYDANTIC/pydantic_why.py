# Import BaseModel to create data models
# EmailStr validates email addresses
# AnyUrl validates URLs of any valid scheme (https, ftp, etc.)
# Field allows us to add validation rules and metadata to fields
# field_validator is used to create custom validation logic for specific fields
from pydantic import BaseModel, EmailStr, AnyUrl , Field , field_validator

# Import typing helpers for complex data types
# List for lists, Dict for dictionaries, Optional for optional fields, Annotated for adding metadata to fields

from typing import List, Dict, Optional , Annotated


# Patient model
# Inherits from BaseModel so that Pydantic can perform automatic validation
class Patient(BaseModel):

    # Unique patient identifier
    id: str

    # Patient's full name
    name: str = Field(max_length=100, description="Full name of the patient, max 100 characters")
    # Alternative way to define the same field with additional metadata using Annotated
    name1 : Annotated[str , Field(max_length=100, title="Name of the patient", description="Full name of the patient, max 100 characters")]
    # Validates that the provided value is a properly formatted email address
    # Requires: pip install email-validator
    email: EmailStr

    # Validates that the value is a valid URL
    # Example: https://linkedin.com/in/johndoe
    linkedin_url: AnyUrl

    # Integer age
    age: int = Field(gt=0 , lt=120, description="Age must be between 1 and 120") #gt=greaterthan , lt=lessthan
    age1 : Annotated[int , Field(gt=0 , lt=120, description="Age must be between 1 and 120")]
    # Height in centimeters
    height: float

    # Weight in kilograms
    # gt=0 ensures that the weight is greater than zero

    weight: float = Field(gt=0, description="Weight must be greater than zero")
    # Alternative way to define the same field with additional metadata using Annotated
    # strict=True ensures that only float values are accepted, not integers
    weight1 : Annotated[float , Field(gt=0, description="Weight must be greater than zero" , strict=True)] #strict=True ensures that only float values are accepted, not integers
    # Optional field
    # If BMI is not provided, its value will automatically become None
    bmi: Optional[float] = None

    # Boolean field
    # Accepts True/False values
    married: bool

    # Optional list of strings
    # Example: ["pollen", "dust"]
    # If not provided, value becomes None
    # max_length=5 ensures that the list cannot contain more than 5 items
    allergies: Optional[List[str]] = Field(default=None, max_length=5, description="Maximum of 5 allergies allowed")

    # Dictionary containing contact information
    # Key must be string
    # Value must be string
    #
    # Example:
    # {
    #     "phone": "1234567890",
    #     "emergency_contact": "9876543210"
    # }
    contact_details: Dict[str, str]

    # Custom validator for email field to ensure it belongs to specific domains
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com' , 'icici.com']
        #abcd@gmail.com
        #
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value


# Function that accepts a Patient object
# Type hint ensures only Patient instances should be passed
def insert_patient_data(patient: Patient):

    print(f"Inserting patient data: {patient}")
    print("-" * 50)

    print(f"Patient ID: {patient.id}")
    print(f"Patient Name: {patient.name}")
    print(f"Patient Email: {patient.email}")
    print(f"Patient LinkedIn URL: {patient.linkedin_url}")

    print(f"Patient Age: {patient.age}")
    print(f"Patient Height: {patient.height} cm")
    print(f"Patient Weight: {patient.weight} kg")

    print(f"Patient BMI: {patient.bmi}")

    print(f"Patient Married: {patient.married}")

    print(f"Patient Allergies: {patient.allergies}")

    print(f"Patient Contact Details: {patient.contact_details}")


# Raw data usually comes from:
# - API Request
# - Database
# - User Input
# - JSON File
patient_info = {
    "id": "P001",
    "name": "John Doe",
    "name1" : "John Doe",
    "email": "abc@hdfc.com",
    "linkedin_url": "https://www.linkedin.com/in/johndoe",
    "age": 30,
    "age1" : 50,
    "height": 175.5,
    "weight": 70.2,
    "weight1": 70.2,
    "bmi": 22.8,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {
        "phone": "1234567890"
    }
}


# ** unpacks the dictionary into keyword arguments
#
# Equivalent to:
#
# Patient(
#     id="P001",
#     name="John Doe",
#     email="abc@gmail.com",
#     ...
# )
#
# Pydantic validates every field before creating the object
# idhar validation ho rahi hai , agar koi field invalid hoga to error throw karega aur idhar hi type coverting bhi ho rahi hai jaise ki age1 ko int me convert kar diya jaa raha hai agar wo string me hoga to
patient1 = Patient(**patient_info)

# Pass validated object to the function
insert_patient_data(patient1)