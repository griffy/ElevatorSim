import math
import random

random.seed(0xDEADBEEF)

def bernoulli(p):
    rand = random.random()
    if rand > p:
        return 0
    else:
        return 1
        
# duration of time between events given rate of arrival lambda_
def exponential(lambda_):
    rand = random.random()
    return -1 / lambda_ * math.log(1-rand)

# number of events in time t given rate lambda_ 
def poisson(t, lambda_):
    time = 0
    num_events = 0
    while time < t:
        time += rand_exponential(lambda_)
        if time < t:        
            num_events += 1
    return num_events

# duration of time for k events to happen given rate of arrival lambda_
def erlang(k, lambda_):
    time = 0
    num_events = 0
    while num_events < k:
        time += rand_exponential(lambda_)
        num_events += 1
    return time
