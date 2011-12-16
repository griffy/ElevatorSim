import rand
from elevator import Elevator
from period import is_morning, is_afternoon, is_evening

TYPE_F_ARRIVAL_DISTRS = {
    'morning': [3, 5, 1, 2, 2, 1, 3, 3, 8, 1, 8, 3],
    'afternoon': [1, 0, 1, 0, 1, 1, 2, 2, 1, 1, 0, 2, 3],
    'evening': [0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 0, 2]
}

TYPE_L_ARRIVAL_DISTRS = {
    'morning': [3, 3, 5, 5, 10, 1, 1, 1, 8, 11, 3, 11],
    'afternoon': [1, 10, 1, 4, 1, 6, 3, 2, 11, 11, 13, 2],
    'evening': [1, 1, 1, 3, 0, 0, 2, 0, 1, 3, 0, 0]
}

TYPE_I_ARRIVAL_DISTRS = {
    'morning': [8, 7, 4, 2, 2, 7, 3, 5, 5, 9, 10, 10],
    'afternoon': [1, 2, 5, 5, 5, 3, 12, 7, 1, 0, 11, 3],
    'evening': [0, 1, 0, 2, 1, 3, 3, 1, 1, 0, 1, 0]
}

TYPE_E_ARRIVAL_DISTRS = {
    'morning': [3, 0, 0, 0, 2, 2, 6, 3, 3, 5, 5, 5],
    'afternoon': [2, 2, 2, 0, 0, 2, 9, 5, 3, 6, 4, 4],
    'evening': [1, 2, 1, 0, 1, 1, 1, 0, 0, 0, 2, 0]
}

arrival_distrs = [
    TYPE_F_ARRIVAL_DISTRS,
    TYPE_L_ARRIVAL_DISTRS,
    TYPE_I_ARRIVAL_DISTRS,
    TYPE_E_ARRIVAL_DISTRS
]

class ElevatorGroup(object):
    def __init__(self, type_, count):
        self.type = type_
        self.count = count
        self.elevators = [Elevator(type_) for i in range(count)]
        self.pool = 0
        self.next_gen = 0
        
    def create_passengers(self, time):
        minute_period = (time / 60) % 60
        minute_period -= minute_period % 5
        
        index = minute_period / 5
        arrivals = 0
        
        if is_morning(time):
            arrivals = rand.poisson(5, arrival_distrs[self.type]['morning'][index])
        elif is_afternoon(time):
            arrivals = rand.poisson(5, arrival_distrs[self.type]['afternoon'][index])
        elif is_evening(time):
            arrivals = rand.poisson(5, arrival_distrs[self.type]['evening'][index])
            
        self.pool = arrivals
        
