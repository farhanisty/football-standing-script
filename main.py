import copy
import random
from repository.Team import Team
from Participation import Participation


class Match:
    def __init__(self, home, away, time):
        self.home = home
        self.away = away
        self.time = time

    def swap(self):
        self.home, self.away = self.away, self.home


def makeMatch(matches, teams):
    lengthTeam = len(teams)
    if lengthTeam == 0:
        return

    lengthTeam = lengthTeam - 1

    homeTeam = random.randint(0, lengthTeam)

    awayTeam = random.randint(0, lengthTeam)

    while awayTeam == homeTeam:
        awayTeam = random.randint(0, lengthTeam)

    match = Match(teams[homeTeam], teams[awayTeam], "2023-07-01 15:30:00")

    teams.pop(homeTeam)
    teams.pop(awayTeam)

    matches.append(match)

    makeMatch(matches, teams)


teamRepository = Team()
# participation = Participation()

teams = teamRepository.getAll()

leagueOneTeams = teams[:10]
# leagueTwoTeams = teams[10:]

leagueOneTeamsFix = copy.deepcopy(leagueOneTeams)

matches = []

makeMatch(matches, leagueOneTeamsFix)

print(matches)
