import sqlite3
import os

def crear_base_datos():
    conexion = sqlite3.connect("db/usuarios.db")
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()
    print("Base de datos creada en 'db/usuarios.db'.")

if __name__ == "__main__":
    crear_base_datos()
