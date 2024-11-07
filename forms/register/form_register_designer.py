import tkinter as tk
from tkinter import messagebox
import sqlite3
import util.generic as utl
from tkinter import ttk
from data.base_de_datos import BaseDeDatos  


class RegisterUsuario:
    
    def __init__(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Registro')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)

        #frame form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        #frame form top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        #frame form fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        self.ventana.mainloop()
