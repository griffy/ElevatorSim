# We use a probability of 0.01 in place of floors that did not have any
# passengers get off on

TYPE_F_DISTRS = {
    'morning': generator({18: 1/38.0,
                          21: 3/38.0,
                          24: 6/38.0,
                          27: 13/38.0,
                          30: 0.01,
                          33: 1/38.0,
                          36: 14/38.0
               }),
    'afternoon': None,
    'evening': generator({18: 0.01,
                          21: 0.01,
                          24: 2/7.0,
                          27: 1/7.0,
                          30: 2/7.0,
                          33: 0.01,
                          36: 2/7.0
               })
}

TYPE_L_DISTRS = {
    'morning': generator({5: 13/62.0,
                          8: 17/62.0,
                          10: 7/62.0,
                          12: 2/62.0,
                          14: 9/62.0,
                          17: 5/62.0,
                          18: 5/62.0,
                          23: 4/62.0
               }),
    'afternoon': None,
    'evening': generator({5: 4/13.0,
                          8: 2/13.0,
                          10: 1/13.0,
                          12: 1/13.0,
                          14: 1/13.0,
                          17: 1/13.0,
                          18: 0.01,
                          23: 3/13.0
               })
}

TYPE_I_DISTRS = {
    'morning': generator({3: 0.01,
                          4: 0.01,
                          5: 23/71.0,
                          8: 7/71.0,
                          10: 7/71.0,
                          12: 5/71.0,
                          14: 17/71.0,
                          17: 5/71.0,
                          18: 1/71.0,
                          23: 6/71.0
               }),
    'afternoon': None,
    'evening': generator({3: 4/13.0,
                          4: 0.01,
                          5: 0.01,
                          8: 0.01,
                          10: 2/13.0,
                          12: 1/13.0,
                          14: 3/13.0,
                          17: 1/13.0,
                          18: 0.01,
                          23: 2/13.0
               })
}

TYPE_E_DISTRS = {
    'morning': generator({3: 4/28.0,
                          4: 3/28.0,
                          5: 1/28.0,
                          6: 2/28.0,
                          7: 0.01,
                          8: 0.01,
                          9: 3/28.0,
                          10: 0.01,
                          11: 0.01,
                          12: 0.01,
                          13: 0.01,
                          14: 0.01,
                          15: 0.01,
                          16: 1/28.0,
                          17: 0.01,
                          18: 0.01,
                          19: 0.01,
                          20: 0.01,
                          21: 0.01,
                          22: 3/28.0,
                          23: 6/28.0,
                          24: 1/28.0,
                          25: 0.01,
                          26: 1/28.0,
                          27: 1/28.0,
                          28: 1/28.0,
                          29: 0.01,
                          30: 0.01,
                          31: 2/28.0,
                          33: 0.01,
                          34: 0.01,
                          35: 0.01,
                          36: 0.01
               }),
    'afternoon': None,
    'evening': generator({3: 4/10.0,
                          4: 3/10.0,
                          5: 0.01,
                          6: 0.01,
                          7: 0.01,
                          8: 0.01,
                          9: 0.01,
                          10: 0.01,
                          11: 0.01,
                          12: 0.01,
                          13: 0.01,
                          14: 0.01,
                          15: 0.01,
                          16: 2/10.0,
                          17: 0.01,
                          18: 0.01,
                          19: 0.01,
                          20: 0.01,
                          21: 0.01,
                          22: 0.01,
                          23: 0.01,
                          24: 0.01,
                          25: 0.01,
                          26: 0.01,
                          27: 0.01,
                          28: 0.01,
                          29: 1/10.0,
                          30: 0.01,
                          31: 0.01,
                          33: 0.01,
                          34: 0.01,
                          35: 0.01,
                          36: 1/10.0
               })
}

distrs = [
    TYPE_F_DISTRS,
    TYPE_L_DISTRS,
    TYPE_I_DISTRS,
    TYPE_E_DISTRS
]

TYPE_F = 0
TYPE_L = 1
TYPE_I = 2
TYPE_E = 3

class Elevator(object):
    def __init__(self, type_):
        self.type = type_
        
    def pick_floor(self, time):
        """ picks a floor it is going to based on the time of day and type
            time must be in seconds where 0 is 5am
        """
        
        morning_end = 6*60*60 # 11am
        afternoon_end = morning_end + 6*60*60
        evening_end = afternoon_end + 6*60*60
        
        if 0 <= time <= morning_end: #11am
            return distrs[self.type]['morning']()
        elif morning_end < time <= afternoon_end:
            return distrs[self.type]['afternoon']()
        elif afternoon_end < time <= evening_end:
            return distrs[self.type]['evening']()
            
