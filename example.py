from system import System
from event import Event
import rand

class PassengerArriveEvent(Event): pass
class PassengerDepartEvent(Event): pass

class ElevatorSystem(System):
    def initialize(self):
        # this var is pointless for now, just want to show system state
        # would go here
        self.elevators = [1]
        # print is only here to show that initialize is called each
        # time we call .run() below
        print self.elevators
        
    def generate_initial_event(self):
        time = 5 # in minutes
        return PassengerArriveEvent(time)
        
    def simulate(self, event):
        # if we're past a day, end the sim by not creating anymore events
        if self.clock.time() > 60 * 24:
            return
            
        if isinstance(event, PassengerArriveEvent):
            self.stats.num_passengers = rand.poisson(5, 1)
            self.feq.schedule_event(PassengerDepartEvent(event.time+1))
        elif isinstance(event, PassengerDepartEvent):
            self.feq.schedule_event(PassengerArriveEvent(event.time+5))
        
system = ElevatorSystem()
stats = system.run()

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers

# if we run it again, the results should be different
stats = system.run()

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers
