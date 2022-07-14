from flask import Flask, request, jsonify
from flask_cors import CORS
from models.patient import Patient
import service.patient_queue_service as queue
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)


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
        patient = Patient(hc, datetime.utcnow().isoformat(), lat, long)
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


@app.before_request
def attempt_auth():
    if request.method != 'POST':
        if request.authorization is None or request.authorization['username'] is None or request.authorization['password'] is None:
            return jsonify({"error": "Missing authorization headers"}), 401
        with open('credentials') as f:
            data = f.read()
        credentials = json.loads(data)
        if credentials != request.authorization:
            return jsonify({"error": "Invalid credentials"}), 401


def is_distance_valid(lat2, long2):
    # Lat/Long HC
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
    # Limite 20km
    return distance <= 20
