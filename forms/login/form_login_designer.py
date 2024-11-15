import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
from forms.register.form_register_designer import RegisterUsuario
from data.base_de_datos import BaseDeDatos  # Importa la clase de base de datos
from face_register import FaceRegister  # Import the FaceRegister class

class App:

    def RegisterUsuario(self):
        self.ventana.destroy()
        RegisterUsuario(self.__init__)

    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()

        # Conectar a la base de datos y verificar el usuario y la contraseña
        db = BaseDeDatos()
        db.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND password = ?", (usu, password))
        user_data = db.cursor.fetchone()
        db.conexion.close()

        if user_data:
            # Si los datos coinciden, procede a la siguiente ventana
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="El usuario o la contraseña es incorrecto", title="Mensaje")

    def open_face_register(self):
        self.ventana.destroy()
        FaceRegister()

    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana, 800, 500)
        
        logo = utl.leer_imagen("./images/133566662558833129.jpg", (200, 200))
        # frame logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # frame form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
                 
        # frame form top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # frame form fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))
        
        register = tk.Button(frame_form_fill, text="Registrarse", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.RegisterUsuario)
        register.pack(fill=tk.X, padx=20, pady=20)        
        register.bind("<Return>", (lambda event: self.RegisterUsuario()))

        self.ventana.mainloop()
        
if __name__ == "__main__":
   App()
