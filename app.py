from flask import Flask, Response, abort
from flask import request
import controllers.patient_queue as patient_queue
from models.patient import Patient


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello MC855'

@app.post('/patient')
def post_patient():
    data = request.form
    patient = patient_queue.add_patient(data)
    
    if patient:
        return patient, 201
    
    abort(403)

@app.get('/queue')
def list_queue():
    #TODO: auth system
    return patient_queue.list_queue(), 200

@app.delete('/patient/<hc>')
def remove_patient(hc):
    #TODO: auth system
    return patient_queue.remove_patient(hc), 200