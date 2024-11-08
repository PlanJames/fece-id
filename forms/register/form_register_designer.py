import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter.font import BOLD
import util.generic as utl
from tkinter import ttk

class RegisterUsuario:
    def __init__(self, ventana_login_func):
        self.ventana_login_func = ventana_login_func  # Guarda la funcion de inicio de sesion

        self.ventana = tk.Tk()                             
        self.ventana.title('Registro')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)

        # Frame form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        # Frame form top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # Frame form fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_newuser = tk.Label(frame_form_fill, text="Ingresa un usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_newuser.pack(fill=tk.X, padx=20, pady=5)
        self.newusuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.newusuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Crea una contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        etiqueta_secondpassword = tk.Label(frame_form_fill, text="Repite la contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_secondpassword.pack(fill=tk.X, padx=20, pady=5)
        self.second_password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.second_password.pack(fill=tk.X, padx=20, pady=10)
        self.second_password.config(show="*")


        boton_registrar = tk.Button(frame_form_fill, text="Registrar", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.registrar_usuario)
        boton_registrar.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()

    def registrar_usuario(self):
        usuario = self.newusuario.get()
        password = self.password.get()
        second_password = self.second_password.get()

        # Verifica si las contraseñas coinciden
        if password != second_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        # Conecta con la base de datos y agregar el usuario
        try:
            conexion = sqlite3.connect("db/usuarios.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, password))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
            self.ventana.destroy()  # cierra la ventana de registro despues  de crearse la cuenta
            self.ventana_login_func()  # Volver a la ventana de inicio de sesion
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
