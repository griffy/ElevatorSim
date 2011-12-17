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
        
    def update_averages(self, overall_stats):
        for stat in self.stats:
            overall_stats.add(stat, self.stats.get(stat))

    def run(self, trials, duration, seed=None):
        overall_stats = Stats()
        for i in range(trials):
            self.reset(seed)
            while self.feq.has_events():
                event = self.feq.next_event()
                self.clock.update(event.time)
                if self.clock.has_run(duration):
                    break
                self.update()
                self.handle(event)
            self.finalize()
            self.update_averages(overall_stats)
            print "Completed trial %d/%d" % (i+1, trials)
        print
        return overall_stats
        
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

    def finalize(self):
        """ All final calculations go here before the stats object is
            returned """
        pass
