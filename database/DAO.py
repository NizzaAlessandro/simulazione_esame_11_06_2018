from database.DB_connect import DBConnect
from model.state import State


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year (s.`datetime`) as anno, count(s.id) as count
                    from new_ufo_sightings.sighting s 
                    group by year(s.`datetime`)   """

        cursor.execute(query, ())

        for row in cursor:
            result.append((str(row["anno"]), str(row["count"])))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.*
                    from new_ufo_sightings.state s, new_ufo_sightings.sighting s2 
                    where s.id = s2.state 
                    and year(s2.`datetime`) = %s
                    group by id 
                    having count(s2.id) > 0"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinctrow upper(s.state) as s1, upper(s2.state) as s2
                    from new_ufo_sightings.sighting s, new_ufo_sightings.sighting s2 
                    where s.state != s2.state 
                    and year (s2.`datetime`) = %s
                    and year (s.`datetime`)=year (s2.`datetime`)
                    and datediff(s2.`datetime`, s.`datetime`) > 0"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append((row["s1"], row["s2"]))

        cursor.close()
        conn.close()
        return result

