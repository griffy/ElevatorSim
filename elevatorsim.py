from system import System
from event import Event
from elevator import Elevator
import rand
import elevator

ONE_DAY = 24*60*60 # in seconds

# this event would have a Passenger entity passed to it upon creation
class PassengerArriveEvent(Event): pass
class PassengerDepartEvent(Event): pass

class ElevatorSystem(System):
    def initialize(self):
        self.elevator_groups = [ElevatorGroup(elevator.TYPE_F, 3),
                                ElevatorGroup(elevator.TYPE_L, 3),
                                ElevatorGroup(elevator.TYPE_I, 3),
                                ElevatorGroup(elevator.TYPE_E, 3)]
        time = 0
        self.schedule_event(PassengerArriveEvent(time))
        
    def update(self):
        pass
        
    def handle(self, event):
        if isinstance(event, PassengerArriveEvent):
            self.stats.num_passengers = rand.poisson(5, 1)
            self.stats.floor_selected = self.elevators[0].pick_floor(self.clock.time())
            self.schedule_event(PassengerDepartEvent(event.time+1))
        elif isinstance(event, PassengerDepartEvent):
            self.schedule_event(PassengerArriveEvent(event.time+5))
        
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
