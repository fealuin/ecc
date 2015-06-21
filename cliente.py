import socket
import sys
import ecc

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=raw_input("Escriba host del servidor:")
try:
    sock.connect((host,8888))
except:
    print("host no encontrado")
    exit()
print("Se ha establecido conexion con el servidor, para salir ingrese un mensaje vacio")

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
print "Esperando a Servidor"
sock.sendall('10')

while True:
    if sock.recv(1024)=='10':
        break
print "Intercambiando Clave Publica"

sock.sendall(str(clavePublica))

clave=tuple(sock.recv(1024))

print "Se ha recibido Clave %s"%str(clave)


while(True):
    msg=raw_input("Escriba su mensaje:\n")
    if len(msg)%2: msg=msg+' '
    if not msg: 
        break
    iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
    k=(raw_input("Escriba clave:\n")+" "*16)[:16]
    log.logreset()
    sock.sendall(str(len(msg)))
    cfb.enviocfb(msg,k,iv,sock)
    
sock.sendall('0')
print "Saliendo"
sock.close()