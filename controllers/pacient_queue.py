from datetime import datetime

from models.pacient import Pacient
from models.pacient_queue import PacientQueue

queue = PacientQueue()

def _current_timestamp():
    return datetime.utcnow().isoformat()

def _is_valid_location(pacient):
    #TODO: implement validation
    return True

def add_pacient(data):
    pacient = Pacient(data.hc, _current_timestamp(), data.hc)
    
    if _is_valid_location(pacient):
        queue.add(pacient)
        return pacient

def remove_pacient(hc):
    queue.remove(hc)
    return queue.queue

def list_queue():
    return queue.queue