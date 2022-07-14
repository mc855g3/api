from flask import Flask, request, jsonify
from models.patient import Patient
import time
import service.patient_queue_service as queue
from math import sin, cos, sqrt, atan2, radians


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
        hc = data['hc']
        lat = data['lat']
        long = data['long']
        if not is_distance_valid(lat, long):
            return jsonify({"error": "Invalid location"}), 403
        patient = Patient(hc, time.time(), lat, long)
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


def is_distance_valid(lat2, long2):
    lat1 = radians(-22.8269585)
    long1 = radians(-47.064116)
    lat2 = radians(lat2)
    long2 = radians(long2)
    dlong = long2 - long1
    dlat = lat2 - lat1
    R = 6373.0
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance <= 20