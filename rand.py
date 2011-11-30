import math
import random

random.seed(0xDEADBEEF)
    
def generator(distr_map):
    """ Returns a function that can be called to return a random value
        from the given distribution. 
        
        The map must have the form:
            { value: probability of being selected,
              next_value: probability of being selected,
              ... }
    """
    def generate():
        rand = random.random()
        lower_bound = 0
        cur_key = 0
        for key, val in distr_map.iteritems():
            cur_key += 1
            if lower_bound == 0:
                if rand <= val:
                    return key
            else:
                if lower_bound < rand <= (lower_bound + val):
                    return key
            lower_bound += val
    return generate
    
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
    
