from flask import Flask, request, jsonify
from models.patient import Patient
import time
import service.patient_queue_service as queue

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello MC855'


@app.route('/patient')
def get_list():
    patients = queue.get_patients()
    print(patients)
    return jsonify(patients)


@app.post('/patient')
def add():
    try:
        data = request.json
        patient = Patient(data['hc'], time.time(), data['lat'], data['long'])
        queue.add_patient(patient)
    except Exception as e:
        print(e)
        return jsonify({"error": "Unknown error while trying to add patient to queue"}), 500
    return app.response_class(
        response=patient.toJSON(),
        status=201,
        mimetype='application/json'
    )


@app.delete('/patient/<hc>')
def delete(hc):
    queue.delete_patient(hc)
    return app.response_class(
        status=204,
        mimetype='application/json'
    )

