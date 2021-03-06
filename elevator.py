from rand import generator
from period import is_morning, is_afternoon, is_evening

# stores a function as the value of each key, where the function will
# generate a random value from the list according to the stated probabilities
TYPE_F_FLOOR_DISTRS = {
    'morning': generator({18: 1/38.0,
                          21: 3/38.0,
                          24: 6/38.0,
                          27: 13/38.0,
                          33: 1/38.0,
                          36: 14/38.0
               }),
    'afternoon': generator({18: 1/14.0,
                          	21: 2/14.0,
                          	24: 2/14.0,
                          	27: 5/14.0,
                          	36: 4/14.0
    			}),
    'evening': generator({24: 2/7.0,
                          27: 1/7.0,
                          30: 2/7.0,
                          36: 2/7.0
               })
}

TYPE_L_FLOOR_DISTRS = {
    'morning': generator({5: 13/62.0,
                          8: 17/62.0,
                          10: 7/62.0,
                          12: 2/62.0,
                          14: 9/62.0,
                          17: 5/62.0,
                          18: 5/62.0,
                          23: 4/62.0
               }),
    'afternoon': generator({5: 12/65.0,
                          	8: 5/65.0,
                          	10: 13/65.0,
                          	12: 5/65.0,
                          	14: 21/65.0,
                          	17: 7/65.0,
                          	23: 2/65.0
               }),
    'evening': generator({5: 4/13.0,
                          8: 2/13.0,
                          10: 1/13.0,
                          12: 1/13.0,
                          14: 1/13.0,
                          17: 1/13.0,
                          23: 3/13.0
               })
}

TYPE_I_FLOOR_DISTRS = {
    'morning': generator({5: 23/71.0,
                          8: 7/71.0,
                          10: 7/71.0,
                          12: 5/71.0,
                          14: 17/71.0,
                          17: 5/71.0,
                          18: 1/71.0,
                          23: 6/71.0
               }),
    'afternoon': generator({3: 10/55.0,
                          	4: 4/55.0,
                          	5: 12/55.0,
                          	8: 4/55.0,
                          	10: 4/55.0,
                          	12: 3/55.0,
                          	14: 10/55.0,
                          	17: 1/55.0,
                          	18: 3/55.0,
                          	23: 4/55.0
               }),
    'evening': generator({3: 4/13.0,
                          10: 2/13.0,
                          12: 1/13.0,
                          14: 3/13.0,
                          17: 1/13.0,
                          23: 2/13.0
               })
}

TYPE_E_FLOOR_DISTRS = {
    'morning': generator({3: 4/28.0,
                          4: 3/28.0,
                          5: 1/28.0,
                          6: 2/28.0,
                          9: 3/28.0,
                          16: 1/28.0,
                          22: 3/28.0,
                          23: 6/28.0,
                          24: 1/28.0,
                          26: 1/28.0,
                          27: 1/28.0,
                          28: 1/28.0,
                          31: 2/28.0,
               }),
    'afternoon': generator({3: 4/39.0,
                          4: 3/39.0,
                          5: 1/39.0,
                          6: 1/39.0,
                          7: 1/39.0,
                          9: 1/39.0,
                          10: 1/39.0,
                          11: 2/39.0,
                          13: 2/39.0,
                          15: 2/39.0,
                          16: 3/39.0,
                          18: 1/39.0,
                          19: 1/39.0,
                          20: 1/39.0,
                          23: 8/39.0,
                          26: 1/39.0,
                          27: 1/39.0,
                          28: 1/39.0,
                          34: 1/39.0,
                          36: 3/39.0
               }),
    'evening': generator({3: 4/10.0,
                          4: 3/10.0,
                          16: 2/10.0,
                          29: 1/10.0,
                          36: 1/10.0
               })
}

# how long it takes to travel a difference of x floors
TRAVEL_TIMES = {
		0: 0,
		1: 4,
		2: 7,
		3: 8,
		4: 9,
		5: 10,
		6: 10,
		7: 12,
		8: 13,
		9: 14,
		10: 15,
		11: 16,
		12: 11,
		13: 17,
		14: 19,
		15: 20,
		16: 21,
		17: 22,
		18: 23,
		19: 24,
		20: 25,
		21: 25,
		22: 26,
		23: 26,
		24: 28,
		25: 29,
		26: 30,
		27: 31,
		28: 32,
		29: 33,
		30: 34,
		31: 35,
		32: 36,
		33: 37,
		34: 38,
		35: 39,
}

floor_distrs = [
    TYPE_F_FLOOR_DISTRS,
    TYPE_L_FLOOR_DISTRS,
    TYPE_I_FLOOR_DISTRS,
    TYPE_E_FLOOR_DISTRS
]

TYPE_F = 0
TYPE_L = 1
TYPE_I = 2
TYPE_E = 3

types = [
    'F',
    'L',
    'I',
    'E'
]

class Elevator(object):
    def __init__(self, type_):
        self.type = type_
        self.num_passengers = 0
        # types F and E had larger capacities than L and I
        if self.type == TYPE_F:
        	self.capacity = 11
        elif self.type == TYPE_L:
        	self.capacity = 10
        elif self.type == TYPE_I:
        	self.capacity = 10
        elif self.type == TYPE_E:
        	self.capacity = 11
        
    def pick_floor(self, time):
        """ picks a floor as a passenger would based on the time of day 
            and type of elevator.
            
            time must be in seconds.
        """
        
        if is_morning(time):
            f = floor_distrs[self.type]['morning']
            return f()
        elif is_afternoon(time):
            f = floor_distrs[self.type]['afternoon']
            return f()
        elif is_evening(time):
            f = floor_distrs[self.type]['evening']
            return f()
            
    def generate_floor_selections(self, time):
        floors = [self.pick_floor(time) for i in range(self.num_passengers)]
        floors.sort()
        return floors

    def travel_time(self, time):
        """ returns how long it would take to reach every floor
            selected by each passenger as they get on the elevator
        """
        floors = self.generate_floor_selections(time)
        t_time = 0
        cur_floor = 1 
        for i in range(len(floors)):
            floor_diff = floors[i] - cur_floor
            t_time += TRAVEL_TIMES[floor_diff]
            cur_floor = floors[i]
        return t_time

    def idle_time(self, time):
        """ returns the time the elevator spends not moving and not being
            called by anyone
            
            the values returned are averages derived from data collection
        """
        if self.type == TYPE_F:
            if is_morning(time):
                return 29
            elif is_afternoon(time):
                return 6
            elif is_evening(time):
                return 277
        elif self.type == TYPE_L:
            if is_morning(time):
                return 20
            elif is_afternoon(time):
                return 6
            elif is_evening(time):
                return 294
        elif self.type == TYPE_I:
            if is_morning(time):
                return 13
            elif is_afternoon(time):
                return 12
            elif is_evening(time):
                return 219
        elif self.type == TYPE_E:
            if is_morning(time):
                return 51
            elif is_afternoon(time):
                return 1
            elif is_evening(time):
                return 189
                
    def busy_time(self, time):
        """ returns the time the elevator spends not moving and not being
            called by anyone
            
            the values returned are averages derived from data collection
        """
        if self.type == TYPE_F:
            if is_morning(time):
                return 98
            elif is_afternoon(time):
                return 54
            elif is_evening(time):
                return 256
        elif self.type == TYPE_L:
            if is_morning(time):
                return 86
            elif is_afternoon(time):
                return 71
            elif is_evening(time):
                return 107
        elif self.type == TYPE_I:
            if is_morning(time):
                return 62
            elif is_afternoon(time):
                return 72
            elif is_evening(time):
                return 110
        elif self.type == TYPE_E:
            if is_morning(time):
                return 135
            elif is_afternoon(time):
                return 156
            elif is_evening(time):
                return 169
