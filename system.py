import random

from future_events_queue import FutureEventsQueue
from clock import Clock
from stats import Stats

class System(object):
    def reset(self, seed=None):
        self.feq = FutureEventsQueue()
        self.clock = Clock()
        self.stats = Stats()
        if seed is not None:
            random.seed(seed)
        self.initialize()
        
    def run(self, duration, seed=None):
        self.reset(seed)
        while self.feq.has_events():
            event = self.feq.next_event()
            self.clock.update(event.time)
            if self.clock.has_run(duration):
                break
            self.update()
            self.handle(event)
        return self.stats
        
    def schedule_event(self, event):
        """ Convenience function """
        self.feq.schedule_event(event)
        
    def initialize(self):
        """ System-specific variables are initialized here and the
            first event is scheduled """
        pass
        
    def update(self):
        """ Anything that must be updated every single iteration
            regardless of event type goes here
        """
        pass
        
    def handle(self, event):
        """ Updating of system state and stats, and scheduling of next event
            should go here """
        pass
