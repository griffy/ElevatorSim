# We use a probability of 0.01 in place of floors that did not have any
# passengers get off on

TYPE_F_FLOOR_DISTRS = {
    'morning': generator({18: 1/38.0,
                          21: 3/38.0,
                          24: 6/38.0,
                          27: 13/38.0,
                          33: 1/38.0,
                          36: 14/38.0
               }),
    'afternoon': generator({18: ,
                          	21: ,
                          	24: ,
                          	27: ,
                          	30: ,
                          	33: ,
                          	36: 
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
    'afternoon': generator({5: 12/68.0,
                          	8: 5/68.0,
                          	10: 13/68.0,
                          	12: 5/68.0,
                          	14: 21/68.0,
                          	17: 7/68.0,
                          	23: 2/68.0
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

class Elevator(object):
    def __init__(self, type_):
        self.type = type_
        self.num_passengers = 0
        if self.type = TYPE_F:
        	self.capacity = 11
        elif self.type = TYPE_L:
        	self.capacity = 10
        elif self.type = TYPE_I:
        	self.capacity = 10
        elif self.type = TYPE_E:
        	self.capacity = 11
        
    def pick_floor(self, time):
        """ picks a floor it is going to based on the time of day and type
            time must be in seconds where 0 is 5am
        """
        
        if is_morning(time):
            return floor_distrs[self.type]['morning']()
        elif is_afternoon(time):
            return floor_distrs[self.type]['afternoon']()
        elif is_evening(time):
            return floor_distrs[self.type]['evening']()
            
    # TODO
    def service_time(self, time):
        return self.idle_time(time) + self.busy_time(time) + ...
        
    def idle_time(self, time):
        if self.type == TYPE_F:
            if is_morning(time):
                return 29
            elif is_afternoon(time):
                return -1
            elif is_evening(time):
                return 277
        elif self.type == TYPE_L:
            if is_morning(time): #11am
                return 20
            elif is_afternoon(time):
                return 6
            elif is_evening(time):
                return 294
        elif self.type == TYPE_I:
            if is_morning(time): #11am
                return 13
            elif is_afternoon(time):
                return 12
            elif is_evening(time):
                return 219
        elif self.type == TYPE_E:
            if is_morning(time):: #11am
                return 51
            elif is_afternoon(time):
                return 1
            elif is_evening(time):
                return 189
                
    def busy_time(self, time):
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
