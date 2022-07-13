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
    hc=data.get("hc")
    pacient = Pacient(hc, _current_timestamp(), hc)
    
    if _is_valid_location(pacient):
        queue.add(pacient)
        return pacient

def remove_pacient(hc):
    queue.remove(hc)
    return queue.toJson()

def list_queue():
    return queue.toJson()