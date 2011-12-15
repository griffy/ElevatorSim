from stats import Stats

class Simulation(object):
    def __init__(self, system):
        self.system = system
        self.stats = Stats()
        
    def run(self, num_trials):
        self.stats = Stats()
        for i in range(self.trials):
            run_stats = self.system.run()
            # update stats
            
    def print_results(self):
        # for stat in self.stats:
            # print stat


