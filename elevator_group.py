from elevator import Elevator

class ElevatorGroup(object):
    def __init__(self, type_, count):
        self.type = type_
        self.count = count
        self.elevators = [Elevator(type_) for i in range(count)]
        self.in_period = False
        self.already_created = False
        self.pool = 0
        
    def create_passengers(self):
        if not self.already_created:
            # TODO
            pass
