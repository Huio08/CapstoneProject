import smtplib

sContenido="Contenido"
sCorreo="jhoaquinf.6@gmail.com"

#El correo debe acceder al siguiente enlace y acpetar 
#https://www.google.com/settings/security/lesssecureapps

from_addr = 'contactosistematickets@gmail.com'

sNombre="Ferdinan"
sApellido="Mamani Alfaro"
sContenido="Contenido"
iCategoria="Categoria"
sAsunto="Asunto"
iIdTicket = 0

remitente = sNombre +" " + sApellido + " " + "<contactosistematickets@gmail.com"


destinatario = 'Administrador <jhoaquinf.6@gmail.com>'
asunto = sAsunto

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
""" % (remitente, destinatario, asunto, mensaje)


username = 'contactosistematickets@gmail.com'
password = 'contactoSistematickets123'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(remitente, destinatario, email) 
server.quit()
