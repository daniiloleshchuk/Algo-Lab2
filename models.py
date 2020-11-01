class Hamster:
    def __init__(self, daily_norm, greediness):
        self.daily_norm = daily_norm
        self.greediness = greediness

    def __str__(self):
        return "Daily norm = {}, greediness = {}".format(self.daily_norm, self.greediness)
