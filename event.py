class Event(object):
    # keep a (static) class variable to keep track of total events
    count = 0
    def __init__(self, time):
        self.time = time
        self.id = Event.count
        Event.count += 1
