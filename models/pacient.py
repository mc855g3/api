import json
class Pacient:
    def __init__(self, hc, arrived_timestamp, location):
        self.hc = hc
        self.arrived_timestamp = arrived_timestamp
        self.location = location

    def toJson(self):
        return json.dumps({
            "hc":self.hc,
            "arrived_timestamp":self.arrived_timestamp
            })

    def toData(self):
        return {
            "hc":self.hc,
            "arrived_timestamp":self.arrived_timestamp
            }