import os
import mysql.connector
from mysql.connector import Error
import logging
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env automaticamente
load_dotenv()

class Database:
    @staticmethod
    def conectar():
        try:
            conn = mysql.connector.connect(
                host=os.environ["DB_HOST"],
                database=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"]
            )
            if conn.is_connected():
                return conn
        except Error as e:
            logging.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

    @staticmethod
    def executar_sql(sql, dados=None):
        conn = Database.conectar()
        if conn is None:
            logging.error("Erro: Conexão não estabelecida.")
            return None
        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, dados or ())
            conn.commit()
            return cursor.rowcount
        except Error as e:
            logging.error(f"Erro ao executar SQL: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            conn.close()