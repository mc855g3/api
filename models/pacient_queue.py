import json
class PacientQueue:
    def __init__(self):
        self.queue = []

    def add(self, pacient):
        self.queue.append(pacient)
    
    def remove(self, hc):
        self.queue = list(filter(lambda p: p.hc != hc, self.queue))

    def toJson(self):
        data=[pacient.toData() for pacient in self.queue]
        return json.dumps(data)
