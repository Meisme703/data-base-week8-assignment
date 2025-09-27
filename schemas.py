from pydantic import BaseModel, ConfigDict
from datetime import date, time

# Shared fields for Patient
class PatientBase(BaseModel):
    name: str
    dob: date
    gender: str
    phone: str

# Schema for creating a new patient
class PatientCreate(PatientBase):
    pass

# Schema for returning patient data with ID
class Patient(PatientBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Shared fields for Appointment
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_name: str
    date: date
    time: time

# Schema for creating a new appointment
class AppointmentCreate(AppointmentBase):
    pass

# Schema for returning appointment data with ID
class Appointment(AppointmentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
