import heapq

class FutureEventsQueue(object):
    def __init__(self):
        self._priority_queue = []
        
    def schedule_event(self, event):
        # in case we have two events scheduled to happen at the same time
        # and we want/need one to happen before the other, we schedule
        # first according to the time and second according to the number
        # of the event (ie, event #1 before event #2)
        heapq.heappush(self._priority_queue, 
                      ((event.time, event.id), event))
                      
    def next_event(self):
        event_tuple = heapq.heappop(self._priority_queue)
        event = event_tuple[1]
        return event
        
    def has_events(self):
        return len(self._priority_queue) > 0
        
