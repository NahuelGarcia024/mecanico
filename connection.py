import mysql.connector

class DataBase:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="mecanicov2",
            )
            print("Conectado correctamente a la base de datos")
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            self.cursor = None