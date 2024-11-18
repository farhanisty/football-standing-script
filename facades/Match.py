class Match:
    def __init__(self, home, away, time):
        self.home = home
        self.away = away
        self.time = time

    def swap(self):
        self.home, self.away = self.away, self.home
