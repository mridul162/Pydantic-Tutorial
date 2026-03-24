def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        else:
            print(f"Patient Name: {name}, Age: {age}")
            print("Data inserted successfully.")
    else:
        raise ValueError("Invalid data type for name or age.")
insert_patient_data("John Doe", 30)  

def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(f"Patient Name: {name}, Age: {age}")
        print("Data updated successfully.")
    else:        
        raise ValueError("Invalid data type for name or age.")
update_patient_data("John Doe", 35)