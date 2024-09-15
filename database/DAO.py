from database.DB_connect import DBConnect


class DAO:
    def __init__(self):
        pass

    def getAnniDAO(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=False)
        query = """select year (s.`datetime`), count(*) 
from ufo_sightings.sighting s 
where s.country = "us" 
group by year (s.`datetime`)"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    def getNodiDAO(self,anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=False)
        query = """select s.state 
from ufo_sightings.sighting s 
where year(s.`datetime`)= %s and s.country ="us"
group by s.state 
"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    def getArchiDAO(self, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=False)
        query = """select  s1.state, s2.state
from 
(select *
from ufo_sightings.sighting s 
where year(s.`datetime`)= %s and s.country ="us"
) s1, (select *
from ufo_sightings.sighting s 
where year(s.`datetime`)= %s and s.country ="us"
) s2
where year (s1.`datetime`) = year (s2.`datetime`)
and s1.id <>s2.id and s1.state <> s2.state and s1.datetime < s2.datetime
group by s1.state, s2.state

"""

        cursor.execute(query, (anno,anno,))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
