from connection import connection


class Participation:
    def insert(self, team, leagueId):
        cursor = connection.cursor()

        sql = "INSERT INTO participation(team_id, league_id) value (%s, %s)"
        val = (team[0], leagueId)

        cursor.execute(sql, val)

        connection.commit()
