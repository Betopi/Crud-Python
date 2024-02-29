#Librerias necesarias
import os 
import mysql.connector
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def conectar():
    # Obtine los valores de las variables de entorno
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    # Establece la conexión a la base de datos
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            return conn
    except mysql.connector.Error as e:
        print("Error al conectarse a la base de datos:", e)


