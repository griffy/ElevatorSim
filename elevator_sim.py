from system import System
from event import Event
from elevator import Elevator
from elevator_group import ElevatorGroup
import rand
import period
from elevator import types, TYPE_F, TYPE_L, TYPE_I, TYPE_E

ELEVATOR_PASSENGERS_STAT = 'elevator_%s_%d_num_passengers'
GROUP_POOL_STAT = 'elevator_group_%s_pool_size'
ELEVATOR_IDLE_STAT = 'elevator_%s_%d_idle_time'
ELEVATOR_BUSY_STAT = 'elevator_%s_%d_busy_time'
ELEVATOR_TRAVEL_STAT = 'elevator_%s_%d_travel_time'

class ElevatorArriveEvent(Event):
    def __init__(self, time, group, index):
        Event.__init__(self, time)
        self.elevator_group = group
        self.elevator_index = index

class ElevatorSystem(System):
    def initialize(self):
        self.elevator_groups = [ElevatorGroup(TYPE_F, 2, 2),
                                ElevatorGroup(TYPE_L, 3, 3),
                                ElevatorGroup(TYPE_I, 1, 1),
                                ElevatorGroup(TYPE_E, 2, 2)]
        time = 0
        for elevator_group in self.elevator_groups:
            # schedule arrival of all elevators at time 0
            for i in range(elevator_group.count):
                self.schedule_event(ElevatorArriveEvent(time, elevator_group, i))
        
    def update(self):
    	time_in_minutes = self.clock.time() / 60
        for elevator_group in self.elevator_groups:
    		if elevator_group.next_gen <= time_in_minutes:
        		while elevator_group.next_gen <= time_in_minutes:
        			elevator_group.next_gen += 5
        		elevator_group.create_passengers(self.clock.time())
                # mark down this amount
                self.stats.add(GROUP_POOL_STAT % types[elevator_group.type],
                               elevator_group.pool)

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
                self.stats.add(ELEVATOR_PASSENGERS_STAT % 
                                    (types[elevator.type], index),
                               elevator.num_passengers)
                # schedule next arrival
                cur_time = self.clock.time()
                
                idle_time = elevator.idle_time(cur_time)
                busy_time = elevator.busy_time(cur_time)
                travel_time = elevator.travel_time(cur_time)
                # track the times
                self.stats.add(ELEVATOR_IDLE_STAT % 
                                    (types[elevator.type], index),
                               idle_time)
                self.stats.add(ELEVATOR_BUSY_STAT % 
                                    (types[elevator.type], index),
                               busy_time)
                self.stats.add(ELEVATOR_TRAVEL_STAT % 
                                    (types[elevator.type], index),
                               travel_time)

                service_time = idle_time + busy_time + travel_time

                time = cur_time + service_time
                self.schedule_event(ElevatorArriveEvent(time, group, index))
            else:
            	time = group.next_gen*60
            	self.schedule_event(ElevatorArriveEvent(time, group, index))
        
    def finalize(self):
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
stats = system.run(period.ONE_DAY, seed=0xDEADBEEF)

print stats
