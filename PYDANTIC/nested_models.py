from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)


# This temp here shows that the patient1 object is being converted to a dictionary using the model_dump() method. The model_dump() method is a built-in method in Pydantic that converts a Pydantic model instance into a dictionary. This is useful for serialization, debugging, or when you need to work with the data in a standard Python dictionary format.
temp = patient1.model_dump()
temp1 = patient1.model_dump_json() # this will convert the patient1 object to a JSON string format

temp2 = patient1.model_dump_json(include= {'name', 'age'}) # this will include only the name and age fields in the JSON output
temp3 = patient1.model_dump_json(exclude= {'address'}) # this will exclude the address field from the JSON output


print(temp)
print(type(temp))

print(temp1)
print(type(temp1))

print(temp2)
print(type(temp2))

print(temp3)
print(type(temp3))



# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed