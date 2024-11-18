import copy
import random
import math
from repository.Team import Team
from Participation import Participation
from connection import connection


def getMatchFixture():
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM match_fixture -- WHERE fixture_date = '2022-01-01 00:00:00' -- and home_team_id not in(1,3,2,4,5,7,6,8) and away_team_id not in(1,3,2,4,5,7,6,8)")

    return cursor.fetchall()


def updateDatetime(item, datetime):
    cursor = connection.cursor()
    cursor.execute(
        f'UPDATE match_fixture SET fixture_date="{datetime}" WHERE id={item[0]}')

    connection.commit()


def seed(result, next):
    length = len(next)

    if length == 0:
        return

    copyresult = copy.deepcopy(next)

    choosed = copyresult[random.randint(0, length - 1)]

    result.append(choosed)

    numberChoosed = [choosed[2], choosed[3]]

    for r in next:
        if r[2] in numberChoosed or r[3] in numberChoosed:
            copyresult.remove(r)

    seed(result, copyresult)


def convert(number, isHome):
    if not isHome:
        if number <= 50:
            return 0
        if number <= 70:
            return 1
        if number <= 80:
            return 2
        if number <= 90:
            return 3
        return math.ceil(number % 90 / 2)
    else:
        if number <= 40:
            return 0
        if number <= 60:
            return 1
        if number <= 70:
            return 2
        if number <= 80:
            return 3
        if number <= 90:
            return 4
        return math.ceil(number % 90 / 2)


def randomScore():
    home = random.randint(0, 100)
    away = random.randint(0, 100)

    return convert(home, True), convert(away, False)


class ParticipationUpdater:
    def __init__(self, teamId, goalScore, goalConceded):
        self.teamId = teamId
        self.goalScore = goalScore
        self.goalConceded = goalConceded
        self.generateStatus()

    def commit(self):
        cursor = connection.cursor()

        if self.status == "W":
            cursor.execute(
                f'UPDATE participation SET total_match_played= total_match_played + 1, wins = wins + 1, goal_scored = goal_scored + {self.goalScore}, goal_conceded = goal_conceded + {self.goalConceded}, points = points + {self.point} WHERE team_id={self.teamId}')
        elif self.status == "D":
            cursor.execute(
                f'UPDATE participation SET total_match_played= total_match_played + 1, draws = draws + 1, goal_scored = goal_scored + {self.goalScore}, goal_conceded = goal_conceded + {self.goalConceded}, points = points + {self.point} WHERE team_id={self.teamId}')
        else:
            cursor.execute(
                f'UPDATE participation SET total_match_played= total_match_played + 1, losses = losses + 1, goal_scored = goal_scored + {self.goalScore}, goal_conceded = goal_conceded + {self.goalConceded}, points = points + {self.point}  WHERE team_id={self.teamId}')

        connection.commit()

    def generateStatus(self):
        if (self.goalScore == self.goalConceded):
            self.point = 1
            self.status = "D"
        elif self.goalScore > self.goalConceded:
            self.point = 3
            self.status = "W"
        else:
            self.point = 0
            self.status = "L"


class Match:
    def __init__(self, id, homeId, awayId):
        self.id = id
        self.homeId = homeId
        self.awayId = awayId
        self.generateScore()

    def updatePoint(self):
        homeParticipant = ParticipationUpdater(
            self.homeId, self.homeScore, self.awayScore)

        awayParticipant = ParticipationUpdater(
            self.awayId, self.awayScore, self.homeScore)

        homeParticipant.commit()
        awayParticipant.commit()

        cursor = connection.cursor()

        cursor.execute(
            f'UPDATE match_fixture SET home_team_score = {self.homeScore}, away_team_score = {self.awayScore} WHERE id= {self.id}')

        connection.commit()

    def generateScore(self):
        self.homeScore, self.awayScore = randomScore()


def resetMatch():
    cursor = connection.cursor()

    cursor.execute(
        f'update participation set total_match_played = 0, wins = 0, draws = 0, losses = 0, goal_scored = 0, goal_conceded = 0, points = 0')

    connection.commit()


resetMatch()

for m in getMatchFixture():
    match = Match(m[0], m[2], m[3])

    match.updatePoint()

    # choosed = []
    #
    # print(len(result))
    #
    # seed(choosed, result)
    #
    # for c in choosed:
    #     updateDatetime(c, "2023-11-20 15:30:00")
