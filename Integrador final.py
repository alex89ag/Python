#LIBRERIAS
import msvcrt, os

#FUNCIONES

#Funcion del menu de opciones
def menu():
	print "Elija una opcion: \n 1.- Agregar producto \n 2.- Borrar producto \n 3.- Editar producto \n 4.- Buscar producto \n 5.- Movimientos realizados\n 6.- Fin\n"
	key = msvcrt.getch() #Espera a que se ingrese una tecla para continuar y guarda la tecla ingresada en la variable.
	return key
#Funcion de la opcion agregar producto
def agregar(x):
	cont = 0
	lista=[]
	listaNom=[]
	while cont < x:
		cont = cont+1
		os.system("cls")
		ident=input("Ingrese el codigo del producto: ")
		os.system("cls")
		nom=raw_input("Ingrese el nombre del producto: ")
		os.system("cls")
		prec=input("Ingrese el precio del producto: ")
		os.system("cls")
		stock=input("Ingrese el stock: ")
		lista.append([ident,nom,prec,stock])
		listaNom.append(nom)
	os.system("cls")
	if x == 0:
		print "Ultimo movimiento: No se agrego ningun producto"
		movimientos.append("No se agrego ningun producto")		
	elif x == 1:
		print "Ultimo movimiento: Se agrego el producto: "+nom			
		movimientos.append("Se agrego el producto: "+nom)		
	else:
		mensaje= "Ultimo movimiento: Se agregaron los productos: "
		mensaje2=""
		cantL=0
		for x in listaNom:
			mensaje=mensaje + x +", "  
			cantL=len(x)
			mensaje2=x
		cantL=cantL+4
		print mensaje[0:-cantL]+" y "+mensaje2
		movimientos.append(mensaje[0:-cantL]+" y "+mensaje2)
	return lista	
#Funcion para borrar un producto
def borrar(x,y):
	listaN=[]
	nombre=""
	for producto in x:
		if y == str(producto[0]) or y == producto[1]:
			nombre=producto[1]
			os.system("cls")
			print "Ultimo movimiento: Producto",nombre,"borrado!"
			movimientos.append("Se borro el producto: "+nombre)			
		else:
			listaN.append(producto)
	return listaN
#Funcion para editar o cambiar un producto
def editar(x,y):
	listaN=[]
	ident=0
	nombre=""
	for producto in x:
		if y == str(producto[0]) or y == producto[1]:
			ident=producto[0]
			nombre=producto[1]
			os.system("cls")
			nom=raw_input("Ingrese el nombre del producto: ")
			os.system("cls")
			prec=input("Ingrese el precio del producto: ")
			os.system("cls")
			stock=input("Ingrese el stock: ")
			if nombre == nom:
				os.system("cls")
				print "Ultimo movimiento: Producto",nombre,"editado!"
				movimientos.append("Se edito el producto: "+nombre)
			else:
				os.system("cls")
				print "Ultimo movimiento: Producto",nombre,"fue cambiado por",nom
				movimientos.append("Se cambio el producto "+nombre+" por "+nom)			
			listaN.append([ident,nom,prec,stock])
		else:
			listaN.append(producto)
	return listaN
#Funcion para buscar un producto o mostrar la lista de productos
def buscar(x,y):
	mensaje=""
	encontro="no"
	bajoStock=[]
	stockBajo=""
	suma=0
	cont=0
	promedio=0
	mov=""
	cantL=0
	mov2=""
	if y == "todos":
		movimientos.append("Se buscaron todos los productos")
		os.system("cls")
		for datos in x:
			mensaje=mensaje + "id: "+str(datos[0])+"\nNombre: "+datos[1]+"\nPrecio: "+str(datos[2])+"\nStock: "+str(datos[3])+"\n\n"
			suma=suma+(datos[2]*datos[3])
			cont=cont+datos[3]
			if datos[3] < 5:
				bajoStock.append(datos)
		promedio=suma/len(x)
		if len(bajoStock) == 0:
			stockBajo="No hay stock bajo"
			movimientos.append("No hay stock bajo")
		else:
			for datos in bajoStock:
				stockBajo=stockBajo + "\nid: "+str(datos[0])+"\nNombre: "+datos[1]+"\nPrecio: "+str(datos[2])+"\nStock: "+str(datos[3])+"\n"
				mov= mov + datos[1] + ", "  
				cantL=len(datos[1])
				mov2=datos[1]
		cantL=cantL+4
		movimientos.append("Los productos con bajo stock son: "+mov[0:-cantL]+" y "+mov2)
		promedio=float(suma)/float(cont)		
		mensaje=mensaje + "\nPromedio de precios: " + str(promedio) + "\nProductos con Stock bajo (menos de 5): " + stockBajo
	else:
		movimientos.append("Se busco el producto: " + y)
		for producto in x:
			if y == str(producto[0]) or y == producto[1]:
				os.system("cls")		
				mensaje="id: "+str(producto[0])+"\nNombre: "+producto[1]+"\nPrecio: "+str(producto[2])+"\nStock: "+str(producto[3]) 	
				encontro="si"
		if encontro =="no":
				os.system("cls")
				movimientos.append("Se busco el producto: " + y + " pero no se encontro")
				mensaje="No se encontro el producto buscado"
	return mensaje

#PROGRAMA PRINCIPAL
#Bienvenida, la cual desaparece una vez que se ingresa a cualquier menu.
print "BIENVENIDO\nSISTEMA DE GESTION PARA PRODUCTOS\n\n"
print "que desea hacer?\n"

#Variables
key=menu()
lista=[]
movimientos=[]

#Se agrega a la lista el primer movimiento que es el inicio del programa.
movimientos.append("se inicio el programa")

#Codigo principal del programa
while key != "6":
	if key == "1": #Codigo para agregar un producto
		movimientos.append("Se eligio la opcion: Agregar producto")
		os.system("cls")  #Limpia pantalla
		cantP=input("Cuantos productos quiere ingresar?? ")
		lista=lista + agregar(cantP)
	elif key == "2": #Codigo para borrar un producto
		movimientos.append("Se eligio la opcion: Borrar producto")
		os.system("cls")
		if len(lista) != 0:
			opB=raw_input("Ingrese el codigo o nombre del producto que desea borrar: ") 			
			if buscar(lista,opB)=="No se encontro el producto buscado":
				print "No se encontro el producto buscado\n0k?\nPresionar cualquier tecla para continuar"
				seguir=msvcrt.getch()
				os.system("Cls")
				print "No se borro nada porque no se encontro lo que se queria borrar"
				movimientos.append("No se borro nada porque no se encontro lo que se queria borrar")
			else:
				print buscar(lista,opB)
				print("\nEsta seguro de querer borrar?\nS=SI\nCualquier tecla=NO")
				opcion=msvcrt.getch()
				if opcion.upper() == "S":
					lista=borrar(lista,opB)
				else:
					os.system("cls")
					print "Ultimo movimiento: No se borro nada\n"
					movimientos.append("No se borro nada")
		else:
			os.system("cls")
			movimientos.append("Lista vacia")
			print "Lista vacia\n"
	elif key == "3": #Codigo para editar un producto
		movimientos.append("Se eligio la opcion: Editar producto")
		os.system("cls")
		if len(lista) != 0:
			opE=raw_input("Ingrese el codigo o nombre del producto que desea editar: ")
			if buscar(lista,opE)=="No se encontro el producto buscado":
				print "No se encontro el producto buscado\n0k?\nPresionar cualquier tecla para continuar"
				seguir=msvcrt.getch()
				os.system("Cls")
				print "No se edito nada porque no se encontro lo que se queria editar"
				movimientos.append("No se edito nada porque no se encontro lo que se queria editar")
			else:
				print buscar(lista,opE)
				print("\nEsta seguro de querer editar?\nS=SI\nCualquier tecla=NO")
				opcion=msvcrt.getch()
				if opcion.upper() == "S":
					lista=editar(lista,opE)
				else:
					os.system("cls")
					print "Ultimo movimiento: No se edito nada\n"
					movimientos.append("No se edito nada")
		else:
			os.system("cls")
			movimientos.append("Lista vacia")
			print "Lista vacia\n"
	elif key == "4": #Codigo para buscar un producto
		if len(lista) != 0:
			seguir = "s"
			while seguir == "s":
				os.system("cls")
				movimientos.append("Se elijio la opcion: Buscar producto")
				print "Si desea ver la lista completa escriba en minuscula: todos"
				bus=raw_input("Cual producto busca?(codigo o nombre) ")
				print buscar(lista,bus)		
				print "\nDesea realizar otra busqueda? (s=si // cualquier tecla=no)"
				seguir=msvcrt.getch()
				os.system("Cls")
				print "Ultimo movimiento: Se realizo una busqueda"
		else: 
			os.system("cls")
			movimientos.append("Lista vacia")
			print "Lista vacia\n"
	elif key == "5": #Codigo para mostrar los movimientos realizados
			movimientos.append("Se revisaron los movimientos")
			os.system("cls")
			for movimiento in movimientos:
				print movimiento
			print "\nContinuar??? (presionar cualquier tecla para volver al menu)"
			msvcrt.getch()
			os.system("cls")
			print "Ultimo movimiento: Se revisaron los movimientos"		
	else:
		os.system("cls")
		movimientos.append("Se ingreso una opcion invalida")
		print "Opcion invalida\n"
	movimientos.append("Se volvio al menu")		
	key=menu()
os.system("cls")
movimientos.append("Se cerro el programa")		
#Mensaje final
print "Fin del programa, gracias por usarlo\nPresione una tecla para finalizar."
