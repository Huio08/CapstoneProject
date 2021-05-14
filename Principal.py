from email import message
import tkinter 
from tkinter import*
from tkinter import messagebox, Tk, Label, Button, Entry
from conexion import conexion
import pyodbc
from tkinter import ttk

import smtplib
from decouple import config

#import Login

def formulario(usuarioTipo):
    
    global pantalla2
    
    pantalla2 = Tk()
    pantalla2.geometry("450x500")
    pantalla2.title("Sistema gestion de tickets ("+usuarioTipo+")")
    pantalla2.iconbitmap("imagenes/imagen6.ico")
    pantalla2.resizable(width=0, height=0)
    
    Label(pantalla2, text="BIENVENIDO AL SISTEMA DE TICKETS", bg="green", fg="white", width="300", height="3", font=("calibri", 14)).pack()
    #Label(pantalla2, text="").pack()

    #global nombreUsuario

    lbl1 = Label(pantalla2, text="Nombres:", bg="white", font=("verdana",9))
    lbl1.place(x=20, y=100, width=65, height=26 )
    nombreUser = Entry(pantalla2)
    nombreUser.place(x=90, y=103, width=100, height=20)
    #nombreUser.pack()
    
    lbl2 = Label(pantalla2, text="Apellidos:", bg="white", font=("verdana",9))
    lbl2.place(x=20, y=150, width=65, height=26 )
    apellidoUser = Entry(pantalla2)
    apellidoUser.place(x=90, y=153, width=100, height=20)

    global correo_ing
    correo_ing=StringVar()

    lbl3 = Label(pantalla2, text="Correo:", bg="white", font=("verdana",9))
    lbl3.place(x=210, y=100, width=65, height=26 )
    correoUser = Entry(pantalla2, textvariable=correo_ing)
    correoUser.place(x=280, y=103, width=155, height=20)
   
    global contenido
    contenido = Text(pantalla2)
    contenido.pack()
    contenido.place(x=20, y=200, width=410, height=185)
    
    botonGenerarTicket= Button(text="Generar\n Ticket", height="3", width="10", command=enviarTicket)
    botonGenerarTicket.place(x=20, y=400)

    botonRegistrar= Button(text="Registrar", height="3", width="10", command=registro)
    botonRegistrar.place(x=110, y=400)

    #ayuda a correr solo esta ventana, comentarlo para correr todo el programa
    #pantalla2.mainloop()

def registro():

    #pantalla2.destroy()

    global pantalla3
    pantalla3 = Tk()
    #pantalla1 = Toplevel(pantalla)
    pantalla3.geometry("400x250")
    pantalla3.title("Registro de usuarios")
    pantalla3.iconbitmap("imagenes/imagen6.ico")
     
    Label(pantalla3, text="Por favor ingrese los datos del nuevo usuario", bg="green", fg="white", width="300", height="3", font=("calibri", 14)).pack()
    Label(pantalla3, text="").pack()

    Button(pantalla3, text="Agregar", height="2", width="15").pack()

def enviarTicket():
    
    result = contenido.get("1.0","end")
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config('my_email'), config('my_password'))

    server.sendmail(config('my_email'), correo_ing.get(), result)
    #server.sendmail(config('my_email'),'hugio1989@gmail.com', result)

    server.quit()

    messagebox.showinfo(message="Mensaje enviado",title="Notificación")
    
#formulario()