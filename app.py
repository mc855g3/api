from flask import Flask, Response, abort
from flask import request
import controllers.pacient_queue as pacient_queue
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello MC855'

@app.post('/pacient')
def post_pacient():
    data = request.form
    pacient = pacient_queue.add_pacient(data)
    
    if pacient:
        return pacient.toJson(), 201
    
    abort(403)

@app.get('/queue')
def list_queue():
    #TODO: auth system
    return pacient_queue.list_queue(), 200

@app.delete('/pacient/<hc>')
def remove_pacient(hc):
    #TODO: auth system
    return pacient_queue.remove_pacient(hc), 200