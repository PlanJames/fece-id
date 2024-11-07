# database.py
import sqlite3

class BaseDeDatos:
    def __init__(self, db_name="db/usuarios.db"):
        self.db_name = db_name
        self.conectar()
        self.crear_tabla()

    def conectar(self):
        self.conexion = sqlite3.connect(self.db_name)
        self.cursor = self.conexion.cursor()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.conexion.commit()
