#Llamamos a la variable conexión
from conexion import conexion

try:
    #registrarse
    print("\nIngrese un usuario y contraseña para registrarse \n")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    print("Su usuario es: ", usuario)
    print("Su contraseña es: ", password)

    with conexion.cursor() as cursor:
        consulta = "insert into Ingresar (usuario, pass) values (?,?);"
        cursor.execute(consulta,(usuario, password))
    
    while True:
        print("\nIngrese su usuario y contraseña\n")
        usuarioL = input("Ingrese su Usuario: ")
        passwordL = input("Ingrese su Contraseña: ")

        with conexion.cursor() as cursor:
            consulta2 = ("Select usuario,pass from Ingresar where usuario=? and pass=?")
            cursor.execute(consulta2, (usuarioL, passwordL))

            resultado = cursor.fetchall()

        if resultado:
            for i in resultado:
                print("\nBienvenido "+i[0])
            break
        else:
            print("\nEl usuario o el password es incorrecto")
            intentarOtraVez = input("Quieres intentar otra vez s/n: ")
            if intentarOtraVez.lower() =="n":
                print("Adios gracias")
                break
except Exception as e:
    print("Ocurrio un error:", e)
finally:
    conexion.close()