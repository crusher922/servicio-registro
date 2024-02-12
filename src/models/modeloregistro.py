from src.database.db import get_connection
from .entities.registro import Registro


class ModeloRegistro():

    @classmethod
    def get_registros(self):

        try:
            connection = get_connection()
            registros = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registros")

                resultset = cursor.fetchall()

                for row in resultset:
                    registro = Registro(row[0], row[1], row[2], row[3], row[4], row[5])
                    registros.append(registro.to_JSON())

            connection.close()
            return registros
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_registro(self, id_paciente):
        try:
            connection = get_connection()
            registros = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registros WHERE id_paciente = %s", (id_paciente,))

                resultset = cursor.fetchall()

                for row in resultset:
                    registro = Registro(row[0], row[1], row[2], row[3], row[4], row[5])
                    registros.append(registro.to_JSON())

            connection.close()
            return registros
        except Exception as ex:
            raise Exception(ex)
