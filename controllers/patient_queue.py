from datetime import datetime

from models.patient import Patient
from models.patient_queue import PatientQueue

queue = PatientQueue()

def _current_timestamp():
    return datetime.utcnow().isoformat()

def _is_valid_location(patient):
    #TODO: implement validation
    return True

def add_patient(data):
    patient = Patient(data.hc, _current_timestamp(), data.hc)
    
    if _is_valid_location(patient):
        queue.add(patient)
        return patient

def remove_patient(hc):
    queue.remove(hc)
    return queue.queue

def list_queue():
    return queue.queue