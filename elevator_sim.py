from system import System
from event import Event
from elevator import Elevator
import rand
import elevator

ONE_DAY = 24*60*60 # in seconds

MORNING_END = 6*60*60 # 11am
AFTERNOON_END = MORNING_END + 6*60*60
EVENING_END = AFTERNOON_END + 6*60*60
        
def is_morning(time):
    return 0 <= time <= MORNING_END

def is_afternoon(time):
    return MORNING_END < time <= AFTERNOON_END
    
def is_evening(time):
    return AFTERNOON_END < time <= EVENING_END
    
class ElevatorArriveEvent(Event):
    def __init__(self, time, group, index):
        Event.__init__(self, time)
        self.elevator_group = group
        self.elevator_index = index

class ElevatorSystem(System):
    def initialize(self):
        self.elevator_groups = [ElevatorGroup(elevator.TYPE_F, 2),
                                ElevatorGroup(elevator.TYPE_L, 3),
                                ElevatorGroup(elevator.TYPE_I, 1),
                                ElevatorGroup(elevator.TYPE_E, 2)]
        time = 0
        for elevator_group in self.elevator_groups:
            # schedule arrival of all elevators at time 0
            for i in range(elevator_group.count):
                self.schedule_event(ElevatorArriveEvent(time, elevator_group, i))
        
    def update(self):
    	temp = self.clock.time() / 300
        for elevator_group in self.elevator_groups:
    		if elevator_group.next_gen <= temp:
        		while elevator_group.next_gen <= temp:
        			elevator_group.next_gen += 5
        		elevator_group.create_passengers()
        
    def handle(self, event):
        if isinstance(event, ElevatorArriveEvent):
            group = event.elevator_group
            index = event.elevator_index
            elevator = group.elevators[index]
            
            if group.pool > 0:
                if group.pool > elevator.capacity:
                    elevator.num_passengers = elevator.capacity
                    group.pool -= elevator.num_passengers
                else:
                    elevator.num_passengers = group.pool
                    group.pool = 0
                # schedule next arrival
                cur_time = self.clock.time()
                service_time = elevator.service_time(cur_time)
                time = cur_time + service_time
                self.schedule_event(ElevatorArriveEvent(time, group, index))
            else:
                # TODO
                # schedule next arrival at beginning of next 5 min period
                pass

        
        
        
        
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
