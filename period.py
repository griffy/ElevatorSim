MORNING_END = 6*60*60 # 11am
AFTERNOON_END = MORNING_END + 6*60*60
EVENING_END = AFTERNOON_END + 6*60*60

# FIXME: a 'day' ends after the evening period
ONE_DAY = EVENING_END
        
def is_morning(time):
    return 0 <= time <= MORNING_END

def is_afternoon(time):
    return MORNING_END < time <= AFTERNOON_END
    
def is_evening(time):
    return AFTERNOON_END < time <= EVENING_END
