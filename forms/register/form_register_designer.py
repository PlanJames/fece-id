import tkinter as tk
from tkinter import messagebox
import sqlite3
from data.base_de_datos import BaseDeDatos  # Asegúrate de tener una función para obtener la conexión de la BD


class RegisterUsuario:

# Configuración de la ventana de Tkinter
    ventana = tk.Tk()
    ventana.title("Registro de Usuario")
    ventana.geometry("300x200")

    # Etiquetas y campos de entrada
    label_username = tk.Label(ventana, text="Nombre de usuario:")
    label_username.pack(pady=5)
    entry_username = tk.Entry(ventana)
    entry_username.pack(pady=5)

    label_password = tk.Label(ventana, text="Contraseña:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(ventana, show="*")
    entry_password.pack(pady=5)

    # Botón para registrar
    btn_registrar = tk.Button(ventana, text="Registrar")
    btn_registrar.pack(pady=10)

    ventana.mainloop()
