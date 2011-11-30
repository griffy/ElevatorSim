import math
import random

random.seed(0xDEADBEEF)
    
def uniform(a, b):
    """ Returns a random number from the uniform distribution [a, b]
    """
    # python's random() returns a number from [0, 1)
    return int(random.random() * (b - a + 1)) + a
    
def bernoulli(p):
    """ Returns either 0 (fail) or 1 (success) given probability of success p
    """
    rand = random.random()
    if rand > p:
        return 0
    else:
        return 1
        
def exponential(lambda_):
    """ Returns duration of time between events given rate of arrival lambda_
    """
    rand = random.random()
    return -1 / lambda_ * math.log(1-rand)

def poisson(t, lambda_):
    """ Returns number of events in time t given rate lambda_
    """
    time = 0
    num_events = 0
    while time < t:
        time += rand_exponential(lambda_)
        if time < t:        
            num_events += 1
    return num_events

def erlang(k, lambda_):
    """ Returns a duration of time for k events to happen given rate of
        arrival lambda_
    """
    time = 0
    num_events = 0
    while num_events < k:
        time += rand_exponential(lambda_)
        num_events += 1
    return time
    
def is_heads():
    """ Returns True or False with a 50/50 chance of either occurring """
    if bernoulli(0.5):
        return True
    return False
    
