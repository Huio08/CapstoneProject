import tkinter
from tkinter import *
from tkinter import messagebox
from conexion import conexion
import pyodbc
import Principal

def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x320")
    pantalla.title("Sistema de Tickets (TI)")
    pantalla.iconbitmap("imagenes/imagen6.ico")

    image = PhotoImage(file="imagenes/imagen6.gif")
    image = image.subsample(2, 2)

    label = Label(image = image)
    label.pack()

    Label(text="Acceso al sistema", bg="green", fg="white", width="350", height="2", font=("calibri", 15)).pack()
    Label(text="").pack()

    Button(text="USUARIO", height="2", width="20", command= lambda:clic_boton(1)).pack()
    Label(text="").pack()
    Button(text="ADMIN", height="2", width="20", command= lambda:clic_boton(2)).pack()

    pantalla.mainloop()

def clic_boton(boton):
    
    global tipoUsuario
    pantalla.destroy()
    #tipoUsuario=1
    if boton == 1:
        tipoUsuario ="Estandar"
        
    if boton == 2:
        tipoUsuario ="Admin"
    inicio_sesion()

def inicio_sesion():
    
    #pantalla.destroy()
    
    global pantalla1
    pantalla1 = Tk()
    #pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("350x280")
    pantalla1.title("Inicio de Sesión ("+tipoUsuario+")")
    pantalla1.iconbitmap("imagenes/imagen6.ico")

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña", bg="green", fg="white", width="300", height="3", font=("calibri", 14)).pack()
    Label(pantalla1, text="").pack()

    global nombreUsuario_verify
    global contrasenaUsuario_verify
    
    nombreUsuario_verify=StringVar()
    contrasenaUsuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="USUARIO").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreUsuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="CONTRASEÑA").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*", textvariable=contrasenaUsuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()
    
def validacion_datos():
    
    while True:
        fcursor = conexion.cursor()

        fcursor.execute("Select usuario,pass from Ingreso where usuario='"+nombreUsuario_verify.get()+"' and pass='"+contrasenaUsuario_verify.get()+"'")
        
        resultado = fcursor.fetchall()
   
        if resultado:
            pantalla1.destroy()
            #from Principal import formulario

            Principal.formulario(tipoUsuario)
            #for i in resultado:
             #   pantalla1.destroy()
              #  formulario()
               # i+=1
                #messagebox.showinfo(message="Ingreso exitoso",title="CORRECTO"+i[0])                
            break      
        else:
            messagebox.showinfo(message="Usuario y/o contraseña incorrecto",title="ERROR")
            break    

        conexion.close()
   
menu_pantalla()


