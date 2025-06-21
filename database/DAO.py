#
#
# from database.DB_connect import DBConnect
#
# from model.airport import Airport
# from model.flight import Flight
# from model.airline import Airline
# from model.rotta import Rotta
#
#
# class DAO():
#
#     #Usi un metodo statico (non richiede istanze della classe per essere chiamato).
#     @staticmethod
#     def getAllAirports() -> list[Airport] | None:
#         cnx = DBConnect.get_connection()
#         risultato = []
#         if cnx is not None:
#             cursor = cnx.cursor(dictionary=True)
#             query = """select * from airports a """
#
#             cursor.execute(query)
#             for row in cursor:
#                 #Ogni riga del DB (dizionario) viene trasformata direttamente
#                 # in un oggetto Airport usando l'unpacking con **row.
#                 risultato.append(Airport(**row))
#
#             cursor.close()
#             cnx.close()
#             return risultato
#         else:
#             print("ERRORE NELLA CONNEXIONE")
#             return None
#
#     @staticmethod
#     def getAllAirlines() -> list[Airline] | None:
#         cnx = DBConnect.get_connection()
#         risultato = []
#         if cnx is not None:
#             cursor = cnx.cursor(dictionary=True)
#             query = """select * from airlines a """
#
#             cursor.execute(query)
#             for row in cursor:
#                 #Ogni riga del DB (dizionario) viene trasformata direttamente
#                 # in un oggetto Airport usando l'unpacking con **row.
#                 risultato.append(Airline(**row))
#
#             cursor.close()
#             cnx.close()
#             return risultato
#         else:
#             print("ERRORE NELLA CONNEXIONE")
#             return None
#
#     @staticmethod
#     def getAllFlights() -> list[Flight] | None:
#         cnx = DBConnect.get_connection()
#         risultato = []
#         if cnx is not None:
#             cursor = cnx.cursor(dictionary=True)
#             query = """select * from flights f """
#
#             cursor.execute(query)
#             for row in cursor:
#                 #Ogni riga del DB (dizionario) viene trasformata direttamente
#                 # in un oggetto Airport usando l'unpacking con **row.
#                 risultato.append(Flight(**row))
#
#             cursor.close()
#             cnx.close()
#             return risultato
#         else:
#             print("ERRORE NELLA CONNEXIONE")
#             return None
#
#     # Questo metodo legge le rotte dal db,senza aggregare i voli opposti sulla stessa tratta.
#     # La query è molto semplice. La Lista risultante quindi avrà una entry per i voli A->B, ed un'altra
#     # entry per i voli B->A
#
#     @staticmethod
#     def getAllRotteV1():
#         cnx = DBConnect.get_connection()
#         risultato = []
#         if cnx is not None:
#             cursor = cnx.cursor(dictionary=True)
#             query = """select f.ORIGIN_AIRPORT_ID as a1,f.DESTINATION_AIRPORT_ID as a2, sum(f.DISTANCE) as totDistance, count(*) as nVoli
#                         from flights f
#                         group by f.ORIGIN_AIRPORT_ID,f.DESTINATION_AIRPORT_ID"""
#
#             cursor.execute(query)
#             for row in cursor:
#                 #Ogni riga del DB (dizionario) viene trasformata direttamente
#                 # in un oggetto Airport usando l'unpacking con **row.
#                 risultato.append(Rotta(**row))
#
#             cursor.close()
#             cnx.close()
#             return risultato
#         else:
#             print("ERRORE NELLA CONNEXIONE")
#             return None
#
#         # Questo metodo legge le rotte dal db, aggregando già nella query i voli opposti sulla stessa tratta. Per fare
#         # questo, la query è abbastanza complicata, e sfrutta una join di due tabelle temporanee (una il flip
#         # dell'altra). Visto che alcune rotte non hanno voli in entrambe le direzioni, si fanno dei check sui NULL (che
#         # non vanno esclusi). COALESCE permette nella sommatoria di considerare i NULL come zero.
#     @staticmethod
#     def getAllRotteV2():
#         cnx = DBConnect.get_connection()
#         risultato = []
#         if cnx is not None:
#             cursor = cnx.cursor(dictionary=True)
#             query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2, COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as totDistance, COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as nVoli
#                 FROM
#                 (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
#                 FROM flights f
#                 GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
#                 LEFT JOIN
#                 (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
#                 FROM flights f
#                 GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
#                 ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
#                 WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""
#
#             cursor.execute(query)
#             for row in cursor:
#                 # Ogni riga del DB (dizionario) viene trasformata direttamente
#                 # in un oggetto Airport usando l'unpacking con **row.
#                 risultato.append(Rotta(**row))
#
#             cursor.close()
#             cnx.close()
#             return risultato
#         else:
#             print("ERRORE NELLA CONNEXIONE")
#             return None
#
#
#
# if __name__ == '__main__':
#     dao = DAO()
#     # for aeroporto in dao.getAllAirports():
#     #     print(aeroporto)
#
#     rotte = dao.getAllRotteV1()
#     rotte.sort()
#     for rotta in rotte:
#         print(rotta)
#
#     #for rotta in sorted(dao.getAllRotteV1(), reverse=True):
#     #   print(rotta)
#
#     for rotta in sorted(dao.getAllRotteV2(),reverse=False):
#         print(rotta)
#     print(len(dao.getAllRotteV1()))
#     print(len(dao.getAllRotteV2()))


from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight
from model.airline import Airline
from model.rotta import Rotta


class DAO():

    @staticmethod
    def getAllAirports():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from airports a"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllFlights():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from flights"""

        cursor.execute(query)

        for row in cursor:
            result.append(Flight(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirline():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from airlines"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airline(**row))

        cursor.close()
        conn.close()
        return result

    # Questo metodo legge le rotte dal db,senza aggregare i voli opposti sulla stessa tratta.
    # La query è molto semplice. La Lista risultante quindi avrà una entry per i voli A->B, ed un'altra
    # entry per i voli B->A
    @staticmethod
    def getAllRotteV1():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.ORIGIN_AIRPORT_ID as a1, f.DESTINATION_AIRPORT_ID as a2, SUM(f.DISTANCE) as totDistance, COUNT(*) as nVoli 
                    FROM flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        conn.close()
        return result

    # Questo metodo legge le rotte dal db, aggregando già nella query i voli opposti sulla stessa tratta. Per fare
    # questo, la query è abbastanza complicata, e sfrutta una join di due tabelle temporanee (una il flip
    # dell'altra). Visto che alcune rotte non hanno voli in entrambe le direzioni, si fanno dei check sui NULL (che
    # non vanno esclusi). COALESCE permette nella sommatoria di considerare i NULL come zero.
    @staticmethod
    def getAllRotteV2():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2, COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as totDistance, COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as nVoli
                    FROM
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
                    LEFT JOIN
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
                    ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
                    WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        conn.close()
        return result

if __name__ == '__main__':
    dao = DAO()
    for aeroporto in dao.getAllAirports():
         print(aeroporto)
#
#     rotte = dao.getAllRotteV1()
#     rotte.sort()
#     for rotta in rotte:
#         print(rotta)
#
#     #for rotta in sorted(dao.getAllRotteV1(), reverse=True):
#     #   print(rotta)
#
#     for rotta in sorted(dao.getAllRotteV2(),reverse=False):
#         print(rotta)
#     print(len(dao.getAllRotteV1()))
#     print(len(dao.getAllRotteV2()))