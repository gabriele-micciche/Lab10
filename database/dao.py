from database.DB_connect import DBConnect
from model.filiale import Filiale
from model.collegamento import Collegamento

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def read_all_filiali():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT id, codice, nome, citta, provincia, latitudine, longitudine 
                    FROM filiale
                    ORDER BY id
                """
                cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(Filiale(**row))
                return result
            finally:
                cursor.close()
        finally:
            conn.close()
    @staticmethod
    def read_all_collegamenti():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """
                    SELECT LEAST(id_filiale_origine, id_filiale_destinazione) AS id_filiale_1,
                           GREATEST(id_filiale_origine, id_filiale_destinazione) AS id_filiale_2,
                           AVG(importo) AS importo_medio
                    FROM bonifico
                    WHERE id_filiale_origine <> id_filiale_destinazione
                    GROUP BY LEAST(id_filiale_origine, id_filiale_destinazione),
                             GREATEST(id_filiale_origine, id_filiale_destinazione)
                """
                cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(Collegamento(**row))
                return result
            finally:
                cursor.close()
        finally:
            conn.close()