class Clock(object):
    def __init__(self, time=0):
        self._time = time
        
    def update(self, time):
        self._time = time
        
    def increment(self, dt):
        self._time += dt
        return self._time
        
    def time(self):
        return self._time
