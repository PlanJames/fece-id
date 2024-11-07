from forms.register import form_register_designer
from tkinter import messagebox
import tkinter as tk
from forms.register.form_register_designer import FromRegisterDesigner
from forms.form_master import MasterPanel

class FormRegister(FromRegisterDesigner):
        def Verificar(self):
            usuario = self.usuario.get()
            password = self.password.get()
            if usuario == "jose" and password == "1234":
                self.ventana.destroy()
                MasterPanel()
            else:
                messagebox.showerror(message="Usuario o contraseña incorrecta", title="Mensaje")


        def __init__(self):
            super().__init__()
