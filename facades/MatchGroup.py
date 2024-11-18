class MatchGroup:
    def __init__(self, datetime):
        self.matches = []
        self.datetime = datetime

    def push(self, match):
        self.matches.append(match)
