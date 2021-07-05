import tkinter as tk
from tkinter import Tk, Button, Frame, ttk, Label, Entry, messagebox
from tkinter.constants import S
import tkinter.font as font
import tkinter 
from tkinter import*
import pyodbc
import smtplib
from decouple import config
from email import message
from conexion import conexion

class Aplicacion(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.usuario = (args[0])
        
        self.title("Sistema gestion de tickets - Usuario Estandar")
        self.iconbitmap("imagenes/imagen6.ico")
        self.resizable(width=0, height=0)
        self.geometry("450x500")
        Label(self, text="BIENVENIDO AL SISTEMA DE TICKETS", bg="lightgreen", fg="white", width="300", height="3", font=("calibri", 14)).pack()
    
        self.crearWidgets()

    def comboSeleccionado(self,event):
        if(self.opcion.current() == 0):
            global varOp
            varOp=StringVar(self)
            varOp.set("Incidencia")
            opcionesOp=['Hardware','Software','Comunicaciones']
            self.opcionOp=ttk.Combobox(self,state="readonly")
            self.opcionOp["values"] = opcionesOp
            self.opcionOp.set("Hardware")

            self.opcionOp.config(width=20)
            self.opcionOp.place(x=283, y=170, width=100, height=20)
        else:
            self.opcionOp.destroy()
                

    def crearWidgets(self):
        self.lbl1 = Label(self, text="Nombres:", bg="white", font=("verdana",9))
        self.lbl1.place(x=20, y=100, width=65, height=20 )
        
        self.nombreUser = Entry(self)
        self.nombreUser.place(x=90, y=103, width=100, height=20)

        self.lbl2 = Label(self, text="Apellidos:", bg="white", font=("verdana",9))
        self.lbl2.place(x=20, y=140, width=65, height=20 )
        self.apellidoUser = Entry(self)
        self.apellidoUser.place(x=90, y=140, width=100, height=20)


        global var
        var=StringVar(self)
        var.set("Incidencia")
        opciones=['Incidencia','Problema','Proyecto','Informativo']
        self.lblMenu = Label(self, text="Categoria:", bg="white", font=("verdana",9))
        self.lblMenu.place(x=210, y=140, width=65, height=20)
        self.opcion=ttk.Combobox(self,state="readonly")
        self.opcion["values"] = opciones
        self.opcion.set("Incidencia")
        
        
            
        self.opcion.bind("<<ComboboxSelected>>", self.comboSeleccionado)

        self.opcion.config(width=20)
        self.opcion.place(x=283, y=140, width=100, height=20)

        global correo_ing
        correo_ing=StringVar()

        self.lbl3 = Label(self, text="Correo:", bg="white", font=("verdana",9))
        self.lbl3.place(x=210, y=100, width=65, height=20 )
        correoUser = Entry(self, textvariable=correo_ing)
        correoUser.place(x=280, y=103, width=155, height=20)

        global asunto
        asunto=StringVar()

        self.lbl3 = Label(self, text="Asunto:", bg="white", font=("verdana",9))
        self.lbl3.place(x=20, y=175, width=65, height=20)
        AsuntoUser = Entry(self, textvariable=asunto)
        AsuntoUser.place(x=90, y=175, width=155, height=20)
   
        global contenido
        contenido = Text(self)
        contenido.pack()
        contenido.place(x=20, y=200, width=410, height=185)
    
        self.botonGenerarTicket= Button(text="Generar\nTicket", height="3", width="7", command=self.guardarTicket)
        self.botonGenerarTicket.place(x=20, y=400)

        self.botonHistoriaTicket= Button(text="Historial\nde Ticket's", height="3", width="7", command=self.cargaTicket)
        self.botonHistoriaTicket.place(x=90, y=400)

        self.botonUltimoTicket= Button(text="Estado\nUltimo\nTicket'", height="3", width="7", command=self.cargaUltimoTicket)
        self.botonUltimoTicket.place(x=160, y=400)

        self.botonPerfil= Button(text="Editar\nPerfil'", height="3", width="7", command=self.editarPerfil)
        
        self.botonPerfil.place(x=230, y=400)

        fcursor = conexion.cursor()
        sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
        fcursor.execute(sql)
        usuario = fcursor.fetchone()

        self.nombreUser.insert(0,str(usuario[1]))
        self.apellidoUser.insert(0,str(usuario[2]))
        correo_ing.set(usuario[3])

        self.nombreUser.configure(state='readonly')
        self.apellidoUser.configure(state='readonly')
        correoUser.configure(state='readonly')

        
    def editarPerfil(self):
        root=Tk()
        root.title("Editar Perfil de Usuario")
        root.resizable(width=0, height=0)
        root.geometry("350x280")
        
        root.wm_iconbitmap("imagenes/imagen6.ico")

        varOpcion=IntVar()

        miFrame=Frame(root, width=400, height=200)
        miFrame.pack()

        mensaje=Label(miFrame,text="\nDatos del Usuario:\n")
        mensaje.grid(row=0, column=0, columnspan=2)

        cuadroNombre=Entry(miFrame)
        cuadroNombre.grid(row=5, column=1, padx=5, pady=5)
        cuadroNombre2=Entry(miFrame)
        cuadroNombre2.grid(row=2, column=1, padx=5, pady=5)
        cuadroNombre3=Entry(miFrame)
        cuadroNombre3.grid(row=3, column=1, padx=5, pady=5)
        cuadroNombre4=Entry(miFrame)
        cuadroNombre4.grid(row=4, column=1, padx=5, pady=5)
        cuadroNombre5=Entry(miFrame)
        cuadroNombre5.grid(row=1, column=1, padx=5, pady=5)
        cuadroNombre6=Entry(miFrame)
        cuadroNombre6.config(show="*");
        cuadroNombre6.grid(row=6, column=1, padx=5, pady=5)

        nombreLabel=Label(miFrame, text="Nombre: ")
        nombreLabel.grid(row=2, column=0, sticky="n", padx=5, pady=5)
        nombreLabel2=Label(miFrame, text="Apellido: ")
        nombreLabel2.grid(row=3, column=0, sticky="n", padx=5, pady=5)
        nombreLabel3=Label(miFrame, text="Correo: ")
        nombreLabel3.grid(row=5, column=0, sticky="n", padx=5, pady=5)
        nombreLabel4=Label(miFrame, text="DNI: ")
        nombreLabel4.grid(row=4, column=0, sticky="n", padx=5, pady=5)
        nombreLabel5=Label(miFrame, text="Usuario: ")
        nombreLabel5.grid(row=1, column=0, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Contraseña: ")
        nombreLabel6.grid(row=6, column=0, sticky="n", padx=5, pady=5)


        fcursor = conexion.cursor()
        sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
        #print(sql)
        fcursor.execute(sql)
        usuario = fcursor.fetchone()

        
        cuadroNombre.insert(0,str(usuario[1]))
        cuadroNombre2.insert(0,str(usuario[2]))
        cuadroNombre3.insert(0,str(usuario[3]))
        cuadroNombre4.insert(0,str(usuario[4]))
        cuadroNombre5.insert(0,str(usuario[7]))
        cuadroNombre6.insert(0,str(usuario[8]))


     
        if (usuario[9]!="Admin"):
            cuadroNombre.configure(state='readonly')
            cuadroNombre2.configure(state='readonly')
            cuadroNombre3.configure(state='readonly')
            cuadroNombre4.configure(state='readonly')
            cuadroNombre5.configure(state='readonly')
            #cuadroNombre6.configure(state='readonly')





            

        #print(usuario)

        def guardaDatos():
            sNombre = cuadroNombre.get()
            sApellido = cuadroNombre2.get()
            sCorreo = cuadroNombre3.get()
            sDNI = cuadroNombre4.get()
            sUsuario = cuadroNombre5.get()
            sContrasena = cuadroNombre6.get()
            lDatos = [sNombre,sApellido,sCorreo,sDNI,sUsuario,sContrasena]
            if ("" not in lDatos):
                #print(lDatos)
                try:
                    fcursor = conexion.cursor()

                    sql = """UPDATE [dbo].[Usuarios]
       SET [nombres] = '"""+sNombre+"""'
          ,[apellidos] = '"""+sApellido+"""'
          ,[correo] = '"""+sCorreo+"""'
          ,[dni] = '"""+sDNI+"""'
          ,[usuario] = '"""+sUsuario+"""'
          ,[pass] = '"""+sContrasena+"""'
     WHERE [usuario] = '"""+sUsuario+"""'
    """                
                    #print(sql)
                    fcursor.execute(sql)
                    conexion.commit()
                    messagebox.showinfo(message="Datos editados con éxito",title="Notificación")

                except Exception as e:
                     messagebox.showerror(message="Error al actualizar datos" + str(e),title="Notificación")
                    
                
            else:
                messagebox.showerror(message="Complete todos los datos",title="Notificación")
                self.editarPerfil()
                
        def cargaDatosOtro():
            sUsuario = cuadroNombre5.get()
            fcursor = conexion.cursor()
            sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(sUsuario)+"'"
            #print(sql)
            fcursor.execute(sql)
            usuario = fcursor.fetchone()

            if (usuario):
                conexion.commit()
            
                cuadroNombre.delete(0, tk.END)
                cuadroNombre2.delete(0, tk.END)
                cuadroNombre3.delete(0, tk.END)
                cuadroNombre4.delete(0, tk.END)
                cuadroNombre5.delete(0, tk.END)
                cuadroNombre6.delete(0, tk.END)
                
                cuadroNombre.insert(0,str(usuario[1]))
                cuadroNombre2.insert(0,str(usuario[2]))
                cuadroNombre3.insert(0,str(usuario[3]))
                cuadroNombre4.insert(0,str(usuario[4]))
                cuadroNombre5.insert(0,str(usuario[7]))
                cuadroNombre6.insert(0,str(usuario[8]))
            else:
                cuadroNombre.delete(0, tk.END)
                cuadroNombre2.delete(0, tk.END)
                cuadroNombre3.delete(0, tk.END)
                cuadroNombre4.delete(0, tk.END)
                cuadroNombre5.delete(0, tk.END)
                cuadroNombre6.delete(0, tk.END)
                
            

            
        Button(miFrame, text="Editar Datos",width="20", command=guardaDatos).grid(padx=5, pady=5, row=7, column=0, columnspan=2)

        fcursor = conexion.cursor()
        sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
        #print(sql)
        fcursor.execute(sql)
        usuario = fcursor.fetchone()
        if (usuario[9]=="Admin"):
            Button(miFrame, text="Carga",width="10", command=cargaDatosOtro).grid(padx=5, pady=5, row=1, column=2, columnspan=1)

        
        
        root.mainloop()
        
    def cargaPerfil(self):
        root=Tk()
        root.title("Perfil de Usuario")
        root.resizable(width=0, height=0)
        root.geometry("350x250")
        
        root.wm_iconbitmap("imagenes/imagen6.ico")

        varOpcion=IntVar()

        miFrame=Frame(root, width=400, height=200)
        miFrame.pack()

        mensaje=Label(miFrame,text="\nDatos del Usuario:\n")
        mensaje.grid(row=0, column=0, columnspan=2)

        cuadroNombre=Entry(miFrame)
        cuadroNombre.grid(row=1, column=1, padx=5, pady=5)
        cuadroNombre2=Entry(miFrame)
        cuadroNombre2.grid(row=2, column=1, padx=5, pady=5)
        cuadroNombre3=Entry(miFrame)
        cuadroNombre3.grid(row=3, column=1, padx=5, pady=5)
        cuadroNombre4=Entry(miFrame)
        cuadroNombre4.grid(row=4, column=1, padx=5, pady=5)
        cuadroNombre5=Entry(miFrame)
        cuadroNombre5.grid(row=5, column=1, padx=5, pady=5)
        cuadroNombre6=Entry(miFrame)
        cuadroNombre6.grid(row=6, column=1, padx=5, pady=5)
        cuadroNombre6.config(show="*")

        nombreLabel=Label(miFrame, text="Nombre: ")
        nombreLabel.grid(row=1, column=0, sticky="n", padx=5, pady=5)
        nombreLabel2=Label(miFrame, text="Apellido: ")
        nombreLabel2.grid(row=2, column=0, sticky="n", padx=5, pady=5)
        nombreLabel3=Label(miFrame, text="Correo: ")
        nombreLabel3.grid(row=3, column=0, sticky="n", padx=5, pady=5)
        nombreLabel4=Label(miFrame, text="DNI: ")
        nombreLabel4.grid(row=4, column=0, sticky="n", padx=5, pady=5)
        nombreLabel5=Label(miFrame, text="Usuario: ")
        nombreLabel5.grid(row=5, column=0, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Contraseña: ")
        nombreLabel6.grid(row=6, column=0, sticky="n", show="*", padx=5, pady=5)

        fcursor = conexion.cursor()
        sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
        fcursor.execute(sql)
        usuario = fcursor.fetchone()

        cuadroNombre.insert(0,str(usuario[1]))
        cuadroNombre.configure(state='readonly')

        cuadroNombre2.insert(0,str(usuario[2]))
        cuadroNombre2.configure(state='readonly')

        cuadroNombre3.insert(0,str(usuario[3]))
        cuadroNombre3.configure(state='readonly')

        cuadroNombre4.insert(0,str(usuario[4]))
        cuadroNombre4.configure(state='readonly')

        cuadroNombre5.insert(0,str(usuario[7]))
        cuadroNombre5.configure(state='readonly')

        cuadroNombre6.insert(0,str(usuario[8]))
        cuadroNombre6.configure(state='readonly')

        #print(usuario)

        
        root.mainloop()

    def cargaTicket(self):

        root=Tk()
        root.title("Historial de Ticket's")
        root.resizable(width=0, height=0)
        
        root.iconbitmap("imagenes/imagen6.ico")

        varOpcion=IntVar()

        miFrame=Frame(root, width=400, height=250)
        miFrame.pack()

        tv = ttk.Treeview(miFrame)
        tv.grid(column=0, row=0, padx=10, pady=10, columnspan=4)
        def reporte():
            try:
                fcursor = conexion.cursor()
                dFecha = str(fechaEntry.get())
                dFechaFin = str(fechaEntryFin.get())
                #print(dFecha)
                sql="""SELECT *
          FROM [TicketBD].[dbo].[Ticket], [DetalleTicket],[Usuarios],[TipoCategoria] WHERE [Ticket].idTipoCategoria=[TipoCategoria].idTipoCategoria AND [DetalleTicket].idTicket=[Ticket].idTicket AND [Usuarios].id = [DetalleTicket].idUsuario AND fecha >= '""" + dFecha + """' AND fecha <= '"""+dFechaFin+"""'"""
                #print(sql)
                fcursor.execute(sql)
                lResultado = fcursor.fetchall()
                conexion.commit()
                import openpyxl
                wb = openpyxl.Workbook()
                hoja = wb.active
                # Crea la fila del encabezado con los títulos
                hoja.append(('ID', 'ESTADO', 'ASUNTO', 'MENSAJE', 'FECHA', 'CATEGORIA', "NOMBRE", "APELLIDOS", "CORREO","DNI"))

                for lElemento in lResultado:
                    hoja.append(list([lElemento[0],lElemento[1],lElemento[4],lElemento[3],lElemento[5],lElemento[20],lElemento[9],lElemento[10],lElemento[11],lElemento[12]]))
                from datetime import datetime
                dFecha=str(datetime.now())
                dFecha=dFecha.replace(" ","")
                dFecha=dFecha.replace(".","")
                dFecha=dFecha.replace("-","")
                dFecha=dFecha.replace(":","")
                wb.save("reporte"+dFecha+".xlsx")
                #fcursor.close()
                messagebox.showinfo(message="Reporte generado con éxito",title="Notificación")
            except Exception as e:
                messagebox.showerror(message="Error al generar el reporte "+str(e),title="Notificación")

        fcursor = conexion.cursor()
        sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
        fcursor.execute(sql)
        usuario = fcursor.fetchone()
        
        fecha = Label(miFrame, text="Fecha Inicio (01/01/2021)", bg="white")
        fechaFin = Label(miFrame, text="Fecha Fin (31/12/2021)", bg="white")

        
        fecha.grid(column = 0, row = 2,padx=10,pady=5)
        fechaFin.grid(column = 2, row = 2,padx=10,pady=5)

        fechaEntry = ttk.Entry(miFrame, width=10)
        fechaEntryFin = ttk.Entry(miFrame, width=10)

        fechaEntry.delete(0, tk.END)
        fechaEntry.insert(0, "01/01/2021")

        fechaEntryFin.delete(0, tk.END)
        fechaEntryFin.insert(0, "31/12/2021")
    
        fechaEntry.grid(column = 1, row = 2,padx=10,pady=5)
        fechaEntryFin.grid(column = 3, row = 2,padx=10,pady=5)
        
        if (usuario[9]!="Admin"):
            fechaEntry.state(["disabled"])
            fechaEntryFin.state(["disabled"])
        
        bt = ttk.Button(miFrame, text="Generar Reporte", command=reporte)
        bt.grid(column=0, row=3, padx=10,pady=5, sticky='', columnspan=4)
        if (usuario[9]!="Admin"):
            bt.state(["disabled"]) 
            

        tv['columns']=("ID","ESTADO","ASUNTO","MENSAJE","FECHA","CATEGORIA")
        tv.column('#0', width=0, stretch=NO)
        tv.column('ID', anchor=CENTER, width=25)
        tv.column('ESTADO', anchor=CENTER, width=100)
        tv.column('ASUNTO', anchor=CENTER, width=80)
        tv.column('MENSAJE', anchor=CENTER, width=80)
        tv.column('FECHA', anchor=CENTER, width=80)
        tv.column('CATEGORIA', anchor=CENTER, width=80)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('ID', text='ID', anchor=CENTER)
        tv.heading('ESTADO', text='ESTADO', anchor=CENTER)
        tv.heading('ASUNTO', text='ASUNTO', anchor=CENTER)
        tv.heading('MENSAJE', text='MENSAJE', anchor=CENTER)
        tv.heading('FECHA', text='FECHA', anchor=CENTER)
        tv.heading('CATEGORIA', text='CATEGORIA', anchor=CENTER)

    
        fcursor = conexion.cursor()
        
        sql="""SELECT *
  FROM [TicketBD].[dbo].[Ticket], [DetalleTicket],[Usuarios],[TipoCategoria] WHERE [Ticket].idTipoCategoria=[TipoCategoria].idTipoCategoria AND [DetalleTicket].idTicket=[Ticket].idTicket AND [Usuarios].id = [DetalleTicket].idUsuario and [Usuarios].usuario = '"""+self.usuario+"""'"""
        #print(sql)
        fcursor.execute(sql)
        lResultado = fcursor.fetchall()
        
        conexion.commit()
        
        for ele in tv.get_children():
            tv.delete(ele)
            
        if(len(lResultado)>0):
            idValor = 0
            for item in lResultado:
                tv.insert(parent='', index=idValor, iid= idValor, text='', values=(item[0],item[1],item[4],item[3],item[5],item[20]))
                idValor=idValor+1
        #fcursor.close()
            
    def cargaUltimoTicket(self):
        root=Tk()
        root.title("Editar Estado de Ticket de Usuario")
        root.resizable(width=0, height=0)
        root.geometry("450x350")
        
        root.wm_iconbitmap("imagenes/imagen6.ico")

        varOpcion=IntVar()

        miFrame=Frame(root, width=400, height=200)
        miFrame.pack()

        mensaje=Label(miFrame,text="\nDatos del Ticket Generado:\n")
        mensaje.grid(row=0, column=0, columnspan=3)

        #cuadroNombre=Entry(miFrame)
        #cuadroNombre.grid(row=1, column=1, padx=5, pady=5)

        global nId
        nId = tk.StringVar()
        
        cuadroId=ttk.Combobox(miFrame,width=16,textvariable = nId)



        sql = "SELECT [Ticket].[idTicket] FROM [TicketBD].[dbo].[Ticket], [DetalleTicket],[Usuarios],[TipoCategoria] WHERE [Ticket].idTipoCategoria=[TipoCategoria].idTipoCategoria AND [DetalleTicket].idTicket=[Ticket].idTicket AND [Usuarios].id = [DetalleTicket].idUsuario AND [Ticket].estado != 'Cerrado' ORDER BY [Ticket].[idTicket] DESC"
        fcursor = conexion.cursor()
        fcursor.execute(sql)
        lResultado = fcursor.fetchall()
        #print(lResultado)
        conexion.commit()
        lDatos = []
        for ele in lResultado:
            lDatos.append(ele[0])
            
        cuadroId['values']=lDatos
        cuadroId.grid(row=1, column=1, padx=5, pady=5)
        cuadroId.current(0)

        
        cuadroNombre2=Entry(miFrame)
        cuadroNombre2.grid(row=2, column=1, padx=5, pady=5)
        cuadroNombre3=Entry(miFrame)
        cuadroNombre3.grid(row=3, column=1, padx=5, pady=5)
        cuadroNombre4=Entry(miFrame)
        cuadroNombre4.grid(row=4, column=1, padx=5, pady=5)
        cuadroNombre5=Entry(miFrame)
        cuadroNombre5.grid(row=5, column=1, padx=5, pady=5)
        cuadroNombre6=Entry(miFrame)
        cuadroNombre6.grid(row=6, column=1, padx=5, pady=5)
        #cuadroNombre6.config(show="*")
        botonCarga = Button(miFrame)

        

        nombreLabel=Label(miFrame, text="ID Ticket: ")
        nombreLabel.grid(row=1, column=0, sticky="n", padx=5, pady=5)
        nombreLabel2=Label(miFrame, text="Asunto: ")
        nombreLabel2.grid(row=2, column=0, sticky="n", padx=5, pady=5)
        nombreLabel3=Label(miFrame, text="Nombres: ")
        nombreLabel3.grid(row=3, column=0, sticky="n", padx=5, pady=5)
        nombreLabel4=Label(miFrame, text="Apellidos: ")
        nombreLabel4.grid(row=4, column=0, sticky="n", padx=5, pady=5)
        nombreLabel5=Label(miFrame, text="Categoria: ")
        nombreLabel5.grid(row=5, column=0, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Correo: ")
        nombreLabel6.grid(row=6, column=0, sticky="n", padx=5, pady=5)
        nombreLabel7=Label(miFrame, text="Mensaje: ")
        nombreLabel7.grid(row=7, column=0, sticky="n", padx=5, pady=5)


        global n
        n = tk.StringVar()
        
        cuadroTipo=ttk.Combobox(miFrame,state="readonly",width=16,textvariable = n)

        cuadroTipo['values']=('En proceso/Nuevo','En Observación','Atendido','Cerrado')
        cuadroTipo.grid(row=7, column=1, padx=5, pady=5)
        cuadroTipo.current(0)

        def cargaEstado():
            try:
                sId=cuadroId.get()
                sql = "SELECT TOP 1 * FROM [TicketBD].[dbo].[Ticket], [DetalleTicket],[Usuarios],[TipoCategoria] WHERE [Ticket].idTipoCategoria=[TipoCategoria].idTipoCategoria AND [DetalleTicket].idTicket=[Ticket].idTicket AND [Usuarios].id = [DetalleTicket].idUsuario AND [Ticket].[idTicket] = '"+str(sId)+"'"
                fcursor = conexion.cursor()
                fcursor.execute(sql)
                lResultado = fcursor.fetchone()
                #print(lResultado)
                cuadroNombre2.insert(0,str(lResultado[4]))
                cuadroNombre2.configure(state='readonly')

                cuadroNombre3.insert(0,str(lResultado[9]))
                cuadroNombre3.configure(state='readonly')

                cuadroNombre4.insert(0,str(lResultado[10]))
                cuadroNombre4.configure(state='readonly')

                cuadroNombre5.insert(0,str(lResultado[20]))
                cuadroNombre5.configure(state='readonly')

                cuadroNombre6.insert(0,str(lResultado[11]))
                cuadroNombre6.configure(state='readonly')

                cuadroTipo.set(str(lResultado[1]))            
                conexion.commit()
            except:
                messagebox.showerror(message="No se puede cargar el Ticket ID: " + str(sId) ,title="Notificación")
        
        def cambiaEstado():
            try:
                sId = cuadroId.get()
                sOpcion = cuadroTipo.get()

                fcursor = conexion.cursor()
                sql = "UPDATE [dbo].[Ticket] SET [estado] = '" + sOpcion + "' WHERE [idTicket] = '" + sId + "'"
                fcursor.execute(sql)
                conexion.commit()
                messagebox.showinfo(message="Ticket ID: " + str(sId) + " Modificado correctamente" ,title="Notificación")
            except:
                messagebox.showerror(message="No se puede modificar el Ticket ID: " + str(sId) ,title="Notificación")            
            

        Button(miFrame, text="Buscar",width="10", command=cargaEstado).grid(padx=5, pady=5, row=1, column=2, columnspan=1)

        Button(miFrame, text="Cambiar Estado",command=cambiaEstado).grid(padx=5, pady=5, row=9, column=1, columnspan=1)

        #fcursor = conexion.cursor()
        #sql="SELECT TOP 1 * FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
        #fcursor.execute(sql)
        #usuario = fcursor.fetchone()

        #cuadroNombre.insert(0,str(usuario[1]))
        #cuadroNombre.configure(state='readonly')

        

        #print(usuario)

       
        
        root.mainloop()

    
    def enviarTicket(self):
        try:
        #if (True):
            sContenido=str(contenido.get("1.0",'end-1c'))
            sCorreo=correo_ing.get()
            sNombre=self.nombreUser.get()
            sApellido=self.apellidoUser.get()
            sContenido=str(contenido.get("1.0",'end-1c'))
            iCategoria=str(self.opcion.get())
            sAsunto = str(asunto.get())

            sql="(Select count(*) from [dbo].Ticket)"
            fcursor = conexion.cursor()
            fcursor.execute(sql)
            lTicketId = fcursor.fetchone()
            iIdTicket = str((lTicketId[0]))
            conexion.commit()
            

            sql2 = "SELECT [correo] from [dbo].[Usuarios]"           
            fcursor = conexion.cursor()
            fcursor.execute(sql2)
            lResultado = fcursor.fetchall()
            conexion.commit()

            import smtplib


            for elemento in lResultado:
                sDestino = str(elemento[0])
                #El correo debe acceder al siguiente enlace y acpetar 
                #https://www.google.com/settings/security/lesssecureapps
                
                from_addr = 'Ticket.gestionFC@gmail.com'

                remitente = sNombre +" " + sApellido + " " + "<Ticket.gestionFC@gmail>"


                destinatario = 'Administrador <' + sDestino+ '>'
                asuntoFinal = sAsunto

                mensaje = """<b>Sistema de Ticket's</b><br/>
                De: """ + str(sNombre) + """ """ + str(sApellido)+ """<br/>
                Categoria: """ + str(iCategoria) + """<br/>""" + """
                Asunto: """ + str(sAsunto) + """<br/>""" + """
                Contenido: """ + str(sContenido) + """<br/>""" + """
                ID Ticket: """ + str(iIdTicket) + """<br/>""" + """
                <br/><b>Saludos.</b>
                """
                 
                email = """From: %s 
                To: %s 
                MIME-Version: 1.0 
                Content-type: text/html 
                Subject: %s 

                %s
                """ % (remitente, destinatario, asuntoFinal, mensaje)


                username = 'Ticket.gestionFC@gmail.com'
                password = 'Ydaleu08'
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(username, password)
                server.sendmail(remitente, destinatario, email) 
                server.quit()




            messagebox.showinfo(message="Correo enviado",title="Notificación")
        except Exception as e:
        #else:
            messagebox.showerror(message="Correo no enviado " + str(e),title="Notificación")

    def guardarTicket(self):
        try:
        #if (True):
            sNombre=self.nombreUser.get()
            sApellido=self.apellidoUser.get()
            sContenido=str(contenido.get("1.0",'end-1c'))
            sCorreo=correo_ing.get()
            iCategoria=str(self.opcion.current()+1)
            sAsunto=asunto.get()
            datos = [sNombre,sApellido,sContenido,sCorreo,iCategoria,sAsunto]
            
            if("" not in datos):
                fcursor = conexion.cursor()

                idUser = 0
                sql="SELECT TOP 1 [id] FROM [dbo].[Usuarios] WHERE [usuario] = '"+str(self.usuario)+"'"
                fcursor.execute(sql)
                usuario = fcursor.fetchone()
                sql = """INSERT INTO [dbo].[Ticket]
               ([idTicket]
               ,[estado]
               ,[idTipoCategoria]
               ,[areaTexto]
               ,[asunto])
         VALUES
               ((Select count(*) from [dbo].Ticket),
               'True',
               '"""+iCategoria+"""',
               '"""+sContenido+"""',
               '"""+sAsunto+"""')"""
                #print(sql)
                fcursor.execute(sql)            
                conexion.commit()
                sUsuario=str(usuario[0])
                sql2="""INSERT INTO [dbo].[DetalleTicket]
           ([fecha]
           ,[idUsuario]
           ,[idTicket])
     VALUES
           (GETDATE()
           ,"""+sUsuario+"""
           ,(Select top 1 idTicket from [dbo].Ticket order by idTicket DESC))
"""
                
                fcursor.execute(sql2)
                conexion.commit()
                #conexion.close()

                self.enviarTicket()
                
                messagebox.showinfo(message="Ticker Generado con éxito",title="Notificación")
                
                

            else:
                
                #conexion.close()
                messagebox.showerror(message="Tiene que completar todos los datos",title="Notificación")
        #else:
        except Exception as e:
            error=str(e)
            messagebox.showerror(message="Ocurrió un error"+error,title="Notificación")


    def nuevoUsuario(self):
        
        root=Tk()
        root.title("Nuevo Usuario")
        root.resizable(width=0, height=0)
        root.geometry("650x365")
        
        root.wm_iconbitmap("imagenes/imagen6.ico")

        varOpcion=IntVar()

        miFrame=Frame(root, width=350, height=950)
        miFrame.pack()

        mensaje=Label(miFrame,text="Ingrese los datos del nuevo Usuario: ")
        mensaje.grid(row=0, column=0, columnspan=2,padx=10, pady=10)

        cuadroNombre=Entry(miFrame)
        cuadroNombre.grid(row=1, column=1, padx=5, pady=5)
        cuadroNombre2=Entry(miFrame)
        cuadroNombre2.grid(row=2, column=1, padx=5, pady=5)
        cuadroNombre3=Entry(miFrame)
        cuadroNombre3.grid(row=3, column=1, padx=5, pady=5)
        cuadroNombre4=Entry(miFrame)
        cuadroNombre4.grid(row=4, column=1, padx=5, pady=5)
        cuadroNombre5=Entry(miFrame)
        cuadroNombre5.grid(row=5, column=1, padx=5, pady=5)
        cuadroNombre6=Entry(miFrame)
        cuadroNombre6.grid(row=6, column=1, padx=5, pady=5)
        cuadroNombre6.config(show="*")

        cuadroNombre7=Entry(miFrame)
        cuadroNombre7.grid(row=1, column=3, padx=5, pady=5)
        cuadroNombre8=Entry(miFrame)
        cuadroNombre8.grid(row=2, column=3, padx=5, pady=5)
        cuadroNombre9=Entry(miFrame)
        cuadroNombre9.grid(row=3, column=3, padx=5, pady=5)
        cuadroNombre10=Entry(miFrame)
        cuadroNombre10.grid(row=4, column=3, padx=5, pady=5)
        cuadroNombre11=Entry(miFrame)
        cuadroNombre11.grid(row=5, column=3, padx=5, pady=5)
        cuadroNombre12=Entry(miFrame)
        cuadroNombre12.grid(row=6, column=3, padx=5, pady=5)
        cuadroNombre13=Entry(miFrame)
        cuadroNombre13.grid(row=7, column=3, padx=5, pady=5)


        global nTipoPc
        nTipoPc = tk.StringVar()
        
        cuadroPc=ttk.Combobox(miFrame,state="readonly",width=16,textvariable = nTipoPc)

        cuadroPc['values']=('Desktop','Ordenador')
        cuadroPc.grid(row=8, column=3, padx=5, pady=5)

        cuadroPc.current(0)

        global n
        n = tk.StringVar()
        
        cuadroTipo=ttk.Combobox(miFrame,state="readonly",width=16,textvariable = n)

        cuadroTipo['values']=('Admin','Estandar')
        cuadroTipo.grid(row=7, column=1, padx=5, pady=5)

        cuadroTipo.current(0)

        nombreLabel=Label(miFrame, text="Nombre: ")
        nombreLabel.grid(row=1, column=0, sticky="n", padx=5, pady=5)
        nombreLabel2=Label(miFrame, text="Apellido: ")
        nombreLabel2.grid(row=2, column=0, sticky="n", padx=5, pady=5)
        nombreLabel3=Label(miFrame, text="Correo: ")
        nombreLabel3.grid(row=3, column=0, sticky="n", padx=5, pady=5)
        nombreLabel4=Label(miFrame, text="DNI: ")
        nombreLabel4.grid(row=4, column=0, sticky="n", padx=5, pady=5)
        nombreLabel5=Label(miFrame, text="Usuario: ")
        nombreLabel5.grid(row=5, column=0, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Contraseña: ")
        nombreLabel6.grid(row=6, column=0, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Tipo de Usuario: ")
        nombreLabel6.grid(row=7, column=0, sticky="n", padx=5, pady=5)

        mensajePc=Label(miFrame,text="Ingrese los datos de la Computadora: ")
        mensajePc.grid(row=0, column=2, columnspan=2,padx=10, pady=10)
        
        nombreLabel6=Label(miFrame, text="Marca: ")
        nombreLabel6.grid(row=1, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Modelo de Ordenador: ")
        nombreLabel6.grid(row=2, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Memoria Ram: ")
        nombreLabel6.grid(row=3, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Disco Duro: ")
        nombreLabel6.grid(row=4, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="N° de Contrato: ")
        nombreLabel6.grid(row=5, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="N° de Partes: ")
        nombreLabel6.grid(row=6, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="N° de Serie: ")
        nombreLabel6.grid(row=7, column=2, sticky="n", padx=5, pady=5)
        nombreLabel6=Label(miFrame, text="Tipo de Computadora: ")
        nombreLabel6.grid(row=8, column=2, sticky="n", padx=5, pady=5)

        

        #Opciones[id],[marca],[modelo],[ram],[disco],[contrato],[numeroParte],[serie],[idTipoComputadora]

        def guarda():
            try:
                sNombre = cuadroNombre.get()
                sApellido = cuadroNombre2.get() 
                sCorreo = cuadroNombre3.get()
                sDNI = cuadroNombre4.get()
                sUsuario = cuadroNombre5.get()
                sContea  = cuadroNombre6.get()

                sMarca= cuadroNombre7.get()
                sModelo=cuadroNombre8.get()
                sRam=cuadroNombre9.get()
                sDisco=cuadroNombre10.get()
                sContrato=cuadroNombre11.get()
                sParte=cuadroNombre12.get()
                sSerie=cuadroNombre13.get()
                
                lDatos=[sNombre,sApellido,sCorreo,sDNI,sUsuario,sContea,sMarca,sModelo,sRam,sDisco,sContrato,sParte,sSerie]
                
                
                if ("" not in lDatos):
                    
                    #print(sNombre,sApellido,sCorreo,sDNI,sUsuario, sContea)
                    fcursor = conexion.cursor()
                    sTipoPc = str(cuadroTipo.current()+1)
                    sql="""INSERT INTO [dbo].[Computadoras]
           ([id]
           ,[marca]
           ,[modelo]
           ,[ram]
           ,[disco]
           ,[contrato]
           ,[numeroParte]
           ,[serie]
           ,[idTipoComputadora])
     VALUES
           ((SELECT COUNT(*) + 1 FROM Computadoras)
           ,'"""+sMarca+"""'
           ,'"""+sModelo+"""'
           ,'"""+sRam+"""'
           ,'"""+sDisco+"""'
           ,'"""+sContrato+"""'
           ,'"""+sParte+""""'
           ,'"""+sSerie+"""'
           ,"""+sTipoPc+""")
"""
                    #print(sql)
                    sql2 = """INSERT INTO [dbo].[Usuarios]
                   ([id]
                   ,[nombres]
                   ,[apellidos]
                   ,[correo]
                   ,[dni]
                   ,[centroCosto]
                   ,[descripcionCentroCosto]
                   ,[usuario]
                   ,[pass]
                   ,[tipoUsuario]
                   ,[idComputadora])
             VALUES
                   ((select count(*) + 1 from Usuarios)
                   ,'"""+sNombre+"""'
                   ,'"""+sApellido+"""'
                   ,'"""+sCorreo+"""'
                   ,'"""+sDNI+"""'
                   ,'NULL'
                   ,'NULL'
                   ,'"""+sUsuario+"""'
                   ,'"""+sContea+"""'
                   ,'"""+cuadroTipo.get()+"""'
                   ,(select count(*) from Computadoras))"""

                    #print(sql)
                    #print(sql2)
                    fcursor.execute(sql)
                    conexion.commit()
                    
              
                    fcursor.execute(sql2)
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo(message="Usuario Guardado con éxito",title="Notificación")
                else:
                    messagebox.showerror(message="Complete todos los campos",title="Notificación")
                    #self.nuevoUsuario()
                    
            except Exception as e:
                
                messagebox.showerror(message="Error" + str(e),title="Notificación")
            
        Button(miFrame, text="Agregar Usuario/Computadora",width="30", command=guarda).grid(padx=5, pady=5, row=9, column=1, columnspan=2)
        
        root.mainloop()

class FrameAdmin(Aplicacion):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.usuario = (args[0])
        self.title("Sistema gestion de tickets - Usuario Administrador")
        self.crearBotonesAdm()
    
    def crearBotonesAdm(self):
        self.botonStatus= Button(text="Agregar\nUsuario", height="3", width="7", command=self.nuevoUsuario)
        self.botonStatus.place(x=300, y=400)
