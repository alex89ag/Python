import os

# Funcion que solicita el posicion en donde se corta la sucesión
def solicitarNum():
    numero = int(input("Ingrese la posición donde quiere cortar la sucesión: "))
    while numero <= 0:
        print ("Debe ingresar un numero mayor a 0")
        numero=int(input("Ingrese nuevamente: "))
    return numero

#Crea la funcion hasta la funcion ingresada
def creaFibonachi(h,cont,lista):
    if cont < h: #Se ejecuta hasta que el contador sea igual hasta el numero ingresado
        if len(lista) == 0: # Si la lista esta vacia se agrega el 0 a la lista
            lista.append(0)
            cont += 1
        elif len(lista) == 1: #Si la lista tiene 1 numero cargado se agrega el 1
            lista.append(1)
            cont += 1
        else: #Se continua la lista realizando la suma del ultimo numero con el anterior
            num2=lista[-1]
            num1=lista[-2]
            resultado=num2+num1
            lista.append(resultado)
            cont += 1
        creaFibonachi(h, lista, cont) #Se realiza la recursión para que siga agregando resultados a la lista
    return lista #Se retorna la lista

#Funcion que muestra la serie
def mostrarFibonachi(h,lista):
    sucesion = ""  
    for z in lista:
        sucesion = sucesion + str(z) + "; "
    print(f"\nLa sucesion Fibonachi desde 0 hasta {str(h)} es:\n\n" + "{" + sucesion[0:-2] + "}")

#Funcion que realiza todos los pasos para mostrar la serie
def fibonachi():
    lista = []
    cont = 0 
    num =  solicitarNum()
    lista = creaFibonachi(num,lista,cont)
    mostrarFibonachi(num,lista)

os.system("cls")
print("Bienvenido\n\n")
fibonachi()