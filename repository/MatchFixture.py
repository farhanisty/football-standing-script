from connection import connection


class MatchFixture:
    def insert(self, match, leagueId):
        cursor = connection.cursor()

        sql = "INSERT INTO match_fixture(league_id, home_team_id, away_team_id, stadium_id, fixture_date) value (%s, %s, %s, %s, %s)"
        val = (leagueId, match.home[0], match.away[0],
               match.home[4], "2022-01-01 00:00:00")

        cursor.execute(sql, val)

        connection.commit()
