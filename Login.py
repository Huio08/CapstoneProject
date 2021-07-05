from tkinter import Tk,Label,Button,Entry, Frame
from tkinter import *
#import tkinter
import pyodbc
from tkinter import ttk
from tkinter import messagebox
from conexion import conexion

class FrInicio(Frame):
    
    def __init__(self, master=None):
        super().__init__(master,width=280,height=350, bg="lightgray")
        self.master = master
        self.pack()
        self.frTitulo()
        self.crearBotones()

    def frTitulo(self):
        self.image = PhotoImage(file="imagenes/imagen6.gif")
        self.image = self.image.subsample(2, 2)
        self.label = Label(image = self.image)
        self.label.place(x=90,y=0)

        self.label = Label(self, text="Ingresar usuario y contraseña", bg="lightgreen")
        self.label.place(x=0,y=117, width=280, height=40)

    def crearBotones(self):         
                        
        self.var=StringVar(root)        
        self.opciones=['Estandar','Admin','Estandar']
        self.opcion=ttk.OptionMenu(root,self.var, *self.opciones)
        self.opcion.place(x=140, y=164, width=80, height=22)
                         
        self.label1 = Label(self, text="USUARIO:", bg="lightblue")
        self.txtUsuario = Entry(self, bg="white")
        self.label2 = Label(self, text="CONTRASEÑA:", bg="lightblue")
        self.txtContrasena = Entry(self, bg="white", show="*")
        
        self.label1.place(x=40, y=198, width=60, height=20)
        self.txtUsuario.place(x=130, y=195, width=100, height=25)
        self.label2.place(x=40, y=238, width=85, height=20)
        self.txtContrasena.place(x=130, y=235, width=100, height=25)

        self.btn1 = Button(self, text="INGRESAR", command=self.validacionDatos)        
        self.btn1.place(x=100, y=275, width=90, height=50)

    def validacionDatos(self):
    
        while True:
            fcursor = conexion.cursor()
            tipoUsuario = self.var.get()
            fcursor.execute("Select usuario,pass from Usuarios where usuario='"+self.txtUsuario.get()+"' and pass='"+self.txtContrasena.get()+"' and tipoUsuario='"+tipoUsuario+"' ")            
            resultado = fcursor.fetchall()

            usuario = self.txtUsuario.get()
            
            if resultado:               
                                
                root.destroy()
                
                import Main
                if tipoUsuario=="Estandar":                                  
                    Main.Aplicacion(usuario)
                
                else: 
                    tipoUsuario=="Admin"
                    Main.FrameAdmin(usuario)                    
                    
                break      
            else:
                messagebox.showinfo(message="Error al ingresar los datos del usuario o verifique su tipo de Usuario",title="Incorrecto")
                break
            
root = Tk()
root.wm_title("Sistema de tickets TI")
root.wm_iconbitmap("imagenes/imagen6.ico")
root.resizable(width=0, height=0)
app = FrInicio(root)
app.mainloop()



