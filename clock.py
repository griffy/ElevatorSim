class Clock(object):
    def __init__(self, time=None):
        self._time = time
   
    def increment(self, dt):
        self.update(self.time() + dt)
        return self.time()
             
    def update(self, time):
        if self._time is None:
            self.start_time = time
        self._time = time
        
    def time(self):
        if self._time is None:
            return 0
        return self._time
       
    def has_run(self, duration):
        if self.time() - self.start_time > duration:
            return True
        return False
