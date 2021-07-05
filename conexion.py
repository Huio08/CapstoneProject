#importamos la libreria
import pyodbc

#Datos del servidor
server = 'LAPTOP-T49VU3LR'
database = 'TicketBD'
usuarioBD = 'sa'
passwordDB = '1234'

try:
    #String de conexión
    conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+database+';UID='+usuarioBD+';PWD='+passwordDB)

except Exception as e:
    print("Ocurrio un error al conectar SQL Server", e)