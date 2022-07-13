class PacientQueue:
    def __init__(self):
        self.queue = []

    def add(self, pacient):
        self.queue.append(pacient)
    
    def remove(self, hc):
        self.queue = filter(lambda p: p.hc != hc, self.queue)