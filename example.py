from system import System
from event import Event
import rand

ONE_DAY = 60 * 24 # in minutes

# this event would have a Passenger entity passed to it upon creation
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
        # schedule first event
        time = 5 # in minutes
        self.schedule_event(PassengerArriveEvent(time)) 
        
    def update(self):
        # might want to check if passengers have left a queue here
        pass
        
    def handle(self, event):
        if isinstance(event, PassengerArriveEvent):
            self.stats.num_passengers = rand.poisson(5, 1)
            self.schedule_event(PassengerDepartEvent(event.time+1))
        elif isinstance(event, PassengerDepartEvent):
            self.schedule_event(PassengerArriveEvent(event.time+5))
        
# Use Case #1: If we call run without a seed parameter, each call will be
#              different each time we run the program, and two calls to run
#              definitely won't be the same.
system = ElevatorSystem()
stats = system.run(ONE_DAY)

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers

# if we run it again, the results should be different
stats = system.run(ONE_DAY)

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers

# Use Case #2: If we call run with a seed parameter (just once), this call 
#              and any subsequent calls to run will be predictable (they 
#              will be the same each time we run the program), but the
#              individual results of each run() still won't be the same.
system = ElevatorSystem()
stats = system.run(ONE_DAY, seed=0xDEADBEEF)

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers

# if we run it again, the results should be different from the first
stats = system.run(ONE_DAY)

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers

# Use Case #3: If we call run with the same seed parameter each time, not
#              only will our results be predictable (reproducable) each time
#              we run the program, but the individual calls will have the
#              same random values. Therefore, in this example, the results
#              are the same for each call to run().
#
#              I believe this is what we could use for Correlated Sampling
#              as was discussed in class.
system = ElevatorSystem()
stats = system.run(ONE_DAY, seed=0xDEADBEEF)

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers

stats = system.run(ONE_DAY, seed=0xDEADBEEF)

print "num_passengers list:", stats.num_passengers
print "total num_passengers:", stats.total_num_passengers
print "median of num_passengers list:", stats.median_num_passengers
print "mode of num_passengers list:", stats.mode_num_passengers
print "mean of num_passengers list:", stats.mean_num_passengers
print "standard deviation of num_passengers list:", stats.stdev_num_passengers
