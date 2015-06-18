import math
def validaCoeficientes(a,b):
	if 4*pow(a,3)+27*pow(b,2)==0:
		return False
	return True


def sumaPuntos(p,q,P,a): #Suma puntos de la curva eliptica

	if(p==q):
		for i in range (1,2000):
			x=(P*i+1.0)/(2*p[1])
			if x-int(x) == 0:
				s=(3*pow(p[0],2)+a)*int(x)%P
				break
		rx=pow(s,2)-2*p[0]
		ry=s*(p[0]-rx)-p[1]
		print "%s + %s = %s"%(str(p),str(q),tuple((rx%P,ry%P)))
		return tuple((rx%P,ry%P))
	else:
		if(p[0]==q[0]):
			print "IGUALESS %s + %s = %s"%(str(p),str(q),str(q))
			return q
		#print "sumando puntos distintos %s %s"%(str(p),str(q))
		for i in range (1,1000):
			x=(P*i+1.0)/(p[0]-q[0])
			#print x
			if x-int(x) == 0:
				s=(p[1]-q[1])*int(x)%P
				break
		rx=pow(s,2)-p[0]-q[0]
		ry=s*(p[0]-rx)-p[1]
		print "%s + %s = %s"%(str(p),str(q),tuple((rx%P,ry%P)))
		return tuple((rx%P,ry%P))

def restaPuntos(p,q,P,a): #Suma el inverso aditivo de q a p
	return sumaPuntos(p,tuple((q[0],-q[1])),P,a)

def multiplicaPunto(n,p,P,a): #multiplica puntos
	for i in range(n):
		if i==0:
			a=p
		a=sumaPuntos(a,p,P,a)
	return a

	#if n==1:
	#	return p
	#else:
	#	return sumaPuntos(multiplicaPunto(n-1,p,P,a),p,P,a)

def puntoEnCurva(p,P,a,b): #Retorna True si el punto pertenece a la curva
	z=(pow(p[0],3)+a*p[0]+b)%P
	if pow(p[1],2)%P==z or pow(p[1],2)%P==-z:
		return True
	return False

def puntosEnCurva(P,a,b): #busca los puntos y los deja en una lista
	conj=[]
	for i in range(P):
		for j in range(P):
			if(puntoEnCurva((i,j),P,a,b)):
				conj.append((i,j))
				print ((i,j))
	return conj
def esPrimo(n):
	if n%2==0 and n>2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def validaGenerador(g,P,a,b):
	if puntoEnCurva(g,P,a,b):
		i=2
		punto=g
		while True:
			punto=sumaPuntos(punto,g,P,a)
			i=i+1
			if punto[0]==g[0]: 
				if esPrimo(i):
					print i
					return True
	return False

print validaGenerador((6, 9),23,3,8)
#print puntoEnCurva((1,22),23,3,8)
#puntosEnCurva(23,3,8)
#print sumaPuntos((2,7),(2,7),11,1)
#print multiplicaPunto(7,(2,7),11,1)
#print sumaPuntos((10,-2),(8,3),11)