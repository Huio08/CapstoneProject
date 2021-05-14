import tkinter
from tkinter import *
from tkinter import messagebox
from conexion import conexion

def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Sistema de Tickets (TI)")
    pantalla.iconbitmap("imagenes/imagen6.ico")

    image = PhotoImage(file="imagenes/imagen6.gif")
    image = image.subsample(2, 2)
    label = Label(image = image)
    label.pack()

    Label(text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()
    Button(text="Registrar", height="3", width="30").pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("imagenes/imagen6.ico")

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña", bg="navy", fg="white", width="300", height="3", font=("calibri", 14)).pack()
    Label(pantalla1, text="").pack()

    global nombreUsuario_verify
    global contrasenaUsuario_verify

    nombreUsuario_verify=StringVar()
    contrasenaUsuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreUsuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*", textvariable=contrasenaUsuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()

def validacion_datos():

    while True:
        
        with conexion.fcursor() as cursor:
            consulta1 = ("Select usuario,pass from Ingreso where usuario='"+nombreUsuario_verify.get()+"' and pass='"+contrasenaUsuario_verify.get()+"'")
            #fcursor.execute(consulta1, (nombreUsuario_verify.get(), contrasenaUsuario_verify.get()))

            resultado = cursor.fetchall()

        if resultado:
            for i in resultado:
                messagebox.showinfo(title="Inicio Correcto"+i[0])
            break
        else:
            messagebox.showinfo(title="Inicio Incorrecto")
            break

        conexion.close()
        
menu_pantalla()