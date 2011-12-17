MORNING_START = 0 # 5am
MORNING_END = 6*60*60 # 11am
AFTERNOON_END = MORNING_END + 6*60*60 # 5pm
EVENING_END = AFTERNOON_END + 6*60*60 # 11pm

# a 'day' ends after the evening period as we are not interested in data
# after that point
# A day runs from 5am to 11pm with the day broken into 3 6-hour periods
ONE_DAY = EVENING_END
        
def is_morning(time):
    return 0 <= time <= MORNING_END

def is_afternoon(time):
    return MORNING_END < time <= AFTERNOON_END
    
def is_evening(time):
    return AFTERNOON_END < time <= EVENING_END
