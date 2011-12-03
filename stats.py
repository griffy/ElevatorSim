import math

class Stats(object):
    def __init__(self):
        # stats is a dictionary
        self._stats = {}
        
    def _init_stat(self, stat):
        # each 'statistic' is really a collection of sample points
        self._stats[stat] = []
        
    def _length(self, stat):
        return len(self._stats[stat])
        
    def add(self, stat, sample_point):
        if stat not in self._stats:
            # the statistic does not exist yet, so we initialize it
            self._init_stat(stat)
        self._stats[stat].append(sample_point)
        
    def total(self, stat):
        return sum(self._stats[stat])
        
    def median(self, stat):
        length = self._length(stat)
        if length % 2 == 0:
            return (self._stats[stat][length/2] + 
                    self._stats[stat][length/2-1]) * 1.0 / 2
        return self._stats[stat][length/2]
        
    def mode(self, stat):
        # store the occurrences of each sample point in stat in a dictionary
        counts = {}
        for point in self._stats[stat]:
            if point not in counts:
                counts[point] = self._stats[stat].count(point)
        # filter the list so that only the points with the max occurrences are
        # returned
        max_count = max(counts.values())
        return filter(lambda x: counts[x] == max_count, counts.keys())

    def mean(self, stat):
        n = self._length(stat)
        return self.total(stat) * 1.0 / n
        
    def stdev(self, stat):
        n = self._length(stat)
        u = self.mean(stat)
        deviations = [(x - u) * (x - u) for x in self._stats[stat]]
        return math.sqrt(sum(deviations) / n)

    def __getattr__(self, name):
        """ Pretends that everything is an attribute.
        
            Example:
                total = stats.total('num_passengers')
                
                can be rewritten as
                
                total = stats.total_num_passengers
        """
        if name.startswith('_'):
            # if the name begins with _, it's been defined inside this class
            # and so should follow the standard rules
            return object.__getattr__(self, name)

        if name.startswith('total_'):
            stat = name.replace('total_', '', 1)
            return self.total(stat)
        elif name.startswith('median_'):
            stat = name.replace('median_', '', 1)
            return self.median(stat)
        elif name.startswith('mode_'):
            stat = name.replace('mode_', '', 1)
            return self.mode(stat)
        elif name.startswith('mean_'):
            stat = name.replace('mean_', '', 1)
            return self.mean(stat)
        elif name.startswith('stdev_'):
            stat = name.replace('stdev_', '', 1)
            return self.stdev(stat)
        # else they must want the list of sample points stored in the stat
        return self._stats[name]
            
    def __setattr__(self, name, val):
        """ Syntactic sugar to add a sample point to a statistic
            so it feels more natural.
            
            Example:
                stats.add('num_passengers', 1)
                
                can be rewritten as
                
                stats.num_passengers = 1
        """
        if name.startswith('_'):
            # if the name begins with _, it's been defined inside this class
            # and so should follow the standard rules
            object.__setattr__(self, name, val)
        else:
            self.add(name, val)
        
