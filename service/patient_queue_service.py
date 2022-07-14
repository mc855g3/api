import json
from service.firebase_service import add_entry, read_entries, delete_entry


def add_patient(patient):
    data = patient.toJSON()
    add_entry(data, patient.hc)


def get_patients():
    data = read_entries()
    patients = []
    if data is not None:
        for val in data.items():
            patients.append(json.loads(val[1]))
    return patients


def delete_patient(hc):
    delete_entry(hc)