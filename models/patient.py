import json

class Patient:
    def __init__(self, hc, arrived_timestamp, lat, long):
        self.hc = hc
        self.arrived_timestamp = arrived_timestamp
        self.lat = lat
        self.long = long

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)