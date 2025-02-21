#Ejercicio 1
#Escribir un programa que pida al usuario dos números y muestre por pantalla el mayor de ellos. Si los números son iguales, indicarlo también.
def FuncionMax():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    
    if n1 > n2:
        print("El número mayor es:", n1)
    else:
        print("El número mayor es:", n2)
FuncionMax()

#Ejercicio 2
#Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.
def FuncionMaxdeTres():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    n3 = int(input("Ingrese el tercer número: "))
    
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print("Los 3 números son iguales")
FuncionMaxdeTres()

#Ejercicio 3
#Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o no.
def Vocal():
    letra = input("Ingrese una letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Es una vocal")
    else:
        print("No es una vocal")
Vocal()

#Ejercicio 4
def SumayMultiplicacion():
    lista_numeros = [1,2,3,4]
    suma = 0
    multiplicacion = 1
    for i in range(len(lista_numeros)):
        suma += lista_numeros[i]
        multiplicacion *= lista_numeros[i]
    print(suma)
    print(multiplicacion)
SumayMultiplicacion()

#Ejercicio 5
#Escribir una funcion que reciba una cadena y devuelva su inversa.
def Inversa():
    palabra = input("Ingrese una palabra: ")
    print(palabra[::-1])
Inversa()

#Ejercicio 6
#Escribir una funcion que reciba una cadena y devuelva un diccionario con cada palabra que contiene y su longitud.
def Palabras():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    print(diccionario)
Palabras()