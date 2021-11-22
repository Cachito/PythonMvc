import re
import mysql.connector
import sys
import re
import datetime
from clases import *
class Model:
    def get_all(self):
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        csr_cacho = db_cacho.cursor()
        sql_get = """
            SELECT
                Id
                , Fecha
                , Medio
                , Seccion
                , Titulo
                , Cuerpo
            FROM Noticias
            ORDER BY Fecha DESC
            """

        csr_cacho.execute(sql_get)
        resultado = csr_cacho.fetchall()

        db_cacho.close()

        return resultado

    def create_data(self):
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )

            try:
                csr_cacho = db_cacho.cursor()

                sql_drop = "DROP DATABASE IF EXISTS carro_maier"
                sql_create = "CREATE DATABASE carro_maier"

                csr_cacho.execute(sql_drop)
                csr_cacho.execute(sql_create)

                db_cacho.commit()
                db_cacho.close()
            except Exception as e:
                db_cacho.rollback()
                db_cacho.close()
                raise Exception(f'Error al crear base de datos carro_maier: {str(e)}')

        except Exception as e:
            raise Exception(f'error al abrir conexion: {str(e)}')

    def create_table(self):
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
            )
            try:
                csr_cacho = db_cacho.cursor()

                sql_drop = "DROP TABLE IF EXISTS `Noticias`"
                sql_create = """
                    CREATE TABLE `Noticias`(
                        Id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        Fecha DATE,
                        Medio VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                        Seccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                        Titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                        Cuerpo TEXT COLLATE utf8_spanish2_ci NOT NULL
                        )
                    """
                csr_cacho.execute(sql_drop)
                csr_cacho.execute(sql_create)
                db_cacho.commit()
                db_cacho.close()

            except Exception as e:
                db_cacho.rollback()
                db_cacho.close()
                raise Exception(f"error al crear tabla `Noticias`: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")

    def save_data(self, noticia):
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
                )

            try:
                csr_cacho = db_cacho.cursor()

                medio = re.sub("[\"']", r"", noticia.Medio)
                seccion = re.sub("[\"']", r"", noticia.Seccion)
                titulo = re.sub("[\"']", r"", noticia.Titulo)
                cuerpo = re.sub("[\"']", r"", noticia.Cuerpo)

                if noticia.Id == "0":
                    sql_insert = """
                        INSERT INTO Noticias (Fecha, Medio, Seccion, Titulo, Cuerpo)
                            VALUES (%s, %s, %s, %s, %s)
                        """
                    datos = (noticia.Fecha, medio, seccion, titulo, cuerpo)

                    csr_cacho.execute(sql_insert, datos)
                else:
                    sql_update = f"""
                        UPDATE Noticias SET
                            Fecha = '{noticia.Fecha}',
                            Medio = '{medio}',
                            Seccion = '{seccion}',
                            Titulo = '{titulo}',
                            Cuerpo = '{cuerpo}'
                        WHERE Id = {noticia.Id}
                        """
                    csr_cacho.execute(sql_update)

                db_cacho.commit()
                db_cacho.close()

            except Exception as e:
                db_cacho.rollback()
                db_cacho.close()
                raise Exception(f"error al {'insertar' if noticia.Id == '0' else 'actualizar'} registro en tabla Noticias: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")

    def get_datos(self, search_id):
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
            )

            try:
                csr_cacho = db_cacho.cursor()
                sql_get = f"""
                    SELECT
                        Id
                        , Fecha
                        , Medio
                        , Seccion
                        , Titulo
                        , Cuerpo
                    FROM Noticias
                    WHERE Id = {search_id}
                    """

                csr_cacho.execute(sql_get)
                resultado = csr_cacho.fetchone()
                db_cacho.close()

                return resultado

            except Exception as e:
                db_cacho.close()
                raise Exception(f"error al leer registros en tabla Noticias: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")

    def delete_data(self, search_id):
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
            )

            try:
                csr_cacho = db_cacho.cursor()
                sql_delete = f"""
                    DELETE FROM Noticias
                    WHERE Id = {search_id}
                    """
                csr_cacho.execute(sql_delete)
                db_cacho.commit()
                db_cacho.close()

            except:
                db_cacho.rollback()
                db_cacho.close()
                raise Exception(f"error al eliminar registro en tabla Noticias: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")
