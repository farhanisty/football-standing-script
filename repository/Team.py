from connection import connection


class Team:
    def getAll(self):
        cursor = connection.cursor()

        cursor.execute("select * from team")

        return cursor.fetchall()
