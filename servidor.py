import socket
import sys
import ecc

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (('', 8888))
print 'Iniciando servidor %s en puerto %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'Esperando por una conexion'
    connection, client_address = sock.accept()
    print "Se ha recibido una conexion desde la direccion:",client_address[0],":",client_address[1]
    break
    
while True:
    try:
        P=int(raw_input("Ingrese modulo:"))
        a=int(raw_input("Ingrese coeficiente a:"))
        b=int(raw_input("Ingrese coeficiente b:"))
        if not ecc.validaCoeficientes(a,b):
            print "Coeficientes a y b invalidos"
        elif P < 3:
            print "El Modulo debe ser mayor que 3"
        elif not ecc.esPrimo(P):
            print "El Modulo debe ser primo"
        else:
            break
    except ValueError:
        print("Por favor ingrese valores enteros")

while True:
    try:
        print("A continuacion se presentan los posibles puntos generadores, por favor seleccionar uno: ")
        ecc.puntosGeneradores(P,a,b)
        Gx=int(raw_input("Ingrese la coordenada en el eje X del punto generador: "))
        Gy=int(raw_input("Ingrese la coordenada en el eje y del punto generador: "))
        G=tuple((Gx,Gy))
        orden=ecc.validaGenerador(G,P,a,b)
        if orden==0:
            print("Numero generador invalido, favor seleccionar nuevamente")
        else:
            break
    except ValueError:
        print("Por favor ingrese valores enteros")

while True:
    try:
        n=int(raw_input("Ingrese su Clave Privada:"))
        if(n>orden and n<2):
            print("La clave debe ser mayor que 1 y menor que %d"%orden)
        else:
            break
    except ValueError:
        print("Por favor ingrese valores enteros")

clavePublica=ecc.multiplicaPunto(n,G,P,a)
print "Su clave publica es: %s"%str(clavePublica)
print "Esperando a Cliente"
while True:
    if connection.recv(1024)=='10':
        break
print "Intercambiando Clave Publica"

connection.sendall(str(clavePublica))

clave=connection.recv(1024)

print "Se ha recibido Clave %s"%str(clave)

#while(True):
#    inicio=int(connection.recv(1024))
#    if inicio>0: #Inicia la conversacion con en largo del mensaje, si es 0 se sale
#        print("Se esta recibiendo un mensaje\n")
#        iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
#        k=(raw_input("Escriba clave:\n")+" "*16)[:16]
#        cfb.reccfb(k,iv,connection,inicio)
#    else:
#        break
#    if(inicio==0):break
                
print("El cliente se ha desconectado, saliendo..")
connection.close()
