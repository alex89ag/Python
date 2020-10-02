#Numero de Ramujan - taxicab(2)
import msvcrt,os

#FUNCION
def taxicab2(h):
	import collections
	h=h+1
	lista=[]
	resultados=[]
	repetidos=[]
	cuenta=[]
	listaDef=[]
#Crea lista inicial y la de resultados
	for x in range(0,h):
			numero1=x
			for	y in range (0,h):
				numero2=y
				resultado=(numero1**3)+(numero2**3)
				lista.append([numero1,numero2,resultado])
				resultados.append(resultado)
#Busca valores repetidos en a lista de resultados
	repetidos = [x for x, y in collections.Counter(resultados).items() if y > 1]
#Compara si el resultado guardado en la linsta inicial es igual a uno de los resultados repetidos.
#Crea una lista con los 2 numeros que elevados al cubo dan un resultado repetido, ademas guarda el resultado. 
	for x in lista:
		if x[2] in repetidos:
			cuenta.append(x)
#Ordena la lista de menor a mayor teniendo en cuenta solo el resultado
	cuenta.sort(key=lambda x:x[2])
#Cuenta la cantidad de componentes en la lista
	cant1=len(cuenta)
#Busca las cuenta que de el mismo resultado pero que no sean los mismos numeros inveridos. Ej 1^3 + 2^3 = 2^3 + 1^3
	for x in range(1,cant1,1):
		if cuenta[x][0]!=cuenta[x-1][1] and cuenta[x-1][0] != cuenta[x][1] and cuenta[x-1][2] == cuenta[x][2]:
			listaDef.append([cuenta[x-1][0],cuenta[x-1][1],cuenta[x][0],cuenta[x][1],cuenta[x][2]])
#Cuenta cuantos componentes tiene la lista y pregunta si esta vacia o no. Si no esta vacia procede, caso contrario devuelve un mensaje.			
	cant2=len(listaDef)
	if cant2 > 0:
#Imprime un solo resultado(si se imprime la listaDef tal cual sin saltear un resultado repitiria lo mismo 2 veces pero invertido).
#Ordena el resultado
		for x in range(0,cant2,2):
			print (str(listaDef[x][0])+chr(252)+" + "+str(listaDef[x][1])+chr(252)+" =",str(listaDef[x][2])+chr(252)+" + "+str(listaDef[x][3])+chr(252)+" =",(listaDef[x][4]))
	else:
		print("No se encuentra ningun numero taxicab(2)")	
	print (f"\nCantidad de numeros encontrados: {(len(listaDef)/2)}")
	print (f"Combinaciones probadas: {len(lista)}")
#PROGRAMA PRINCIPAL		
print ("BIENVENIDO AL PROGRAMA TAXICAB(2)\n\n(Presione cualquier tecla para comenzar)")		
#Pausa para leer bienvenida
msvcrt.getch()
#Se asigna un valor a key para que inicie el while
key="C"
#Se usa upper() para que sin importar si usa mayuscula o minuscula entre al while.
while key.upper() == "C":
	os.system("cls")	
#Pide hasta que rango se desea buscar el valor
	num = int(input("Ingrese hasta que numero usar para las combinaciones: "))
	taxicab2(num)
#Se consulta si quiere hacer una nueva busqueda. 
#Si se preciona "c" o "C" va a volver a consultar el rango, caso contrario finaliza el programa.	
	print("")
	print("Desea realizar una nueva busqueda????\n(precionar C para continuar o cualquier tecla para salir)")
	key=msvcrt.getch()
print("Fin del programa")
