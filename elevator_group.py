from elevator import Elevator

class ElevatorGroup(object):
    def __init__(self, type_, count):
        self.type = type_
        self.count = count
        self.elevators = [Elevator(type_) for i in range(count)]
        self.in_period = True
