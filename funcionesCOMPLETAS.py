from principal import *
from configuracion import *
from extras import *
import random
import math
#Funciones implementadas por el grupo
def eliminarSalto(cadena): #elimina los saltos de linea("\n") de las palabras en el archivo
    new_cad=""
    for char in cadena:
        if char != "\n":
            new_cad += char
    return new_cad

def esta (cad,letr):  #Si la letra esta en la cadena, devuelve True. Sino esta, devuelve False. Tambien para usarse en listas: def esta(lista,elem).
    for char in cad:
        if char == letr:
            return True
    return False

def cadenaALista(cadena):
    lista_cadena = [] #creo una lista vacia, que va a contener c/u de las letras de la cadena
    for letra in cadena:
        lista_cadena.append(letra)
    return lista_cadena

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):  #esta funcion no retorna una nueva lista, sino que agrega elementos a la lista vacia "diccionario" previamente declarada en el principal
    abrirLemario = open("lemario.txt", "r",encoding="ISO-8859-1") #modificacion en el encoding(ej: por los caracteres ñ")
    lineas = abrirLemario.readlines()

    for linea in lineas:
        diccionario.append(eliminarSalto(linea))

    abrirLemario.close()


#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
    sieteLetras = ""

    consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w']
    vocales = ['a', 'e', 'i', 'o', 'u']
    consDificiles=['k', 'x', 'y', 'z']

    posCons= random.randint(0,16)
    posVoc= random.randint(0,4)
    posConsDif= random.randint(0,3)

    dameVoc = random.randint(2,3)
    dameConsDif = random.randint(0,1)

    i=1
    while i <= dameVoc:
        if esta(sieteLetras,vocales[posVoc]):
            posVoc= random.randint(0,4)
        else:
            sieteLetras += vocales[posVoc]
            i += 1

    if dameConsDif == 1:
        sieteLetras += consDificiles[posConsDif]

    dameCons = 7 - len(sieteLetras)
    i=1
    while i <= dameCons:
        if esta(sieteLetras,consonantes[posCons]):
            posCons= random.randint(0,16)
        else:
            sieteLetras += consonantes[posCons]
            i += 1

    return sieteLetras

def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
    letrasEnPantalla = cadenaALista(letrasEnPantalla) #pasa cada uno de los caracteres de la cadena a una lista

    long_listaLetras = len(letrasEnPantalla)-1 #longitud de la lista que contiene las letras. "-1" porque empieza en posicion 0
    letra = letrasEnPantalla[3] #letra del medio seleccionada
    return letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
        return Puntos(candidata) #devuelve los correspondientes puntos (los acumula)
    else:
        return -1 #resta 1 punto porque la palabra no tiene la letra princ, no esta en el diccionario
                   #o sus letras no aparecen en la pantalla

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    #letraPrincipal es una sola letra
    #letrasEnPantalla es una cadena
    #diccionario es una lista de palabras
    letrasCandidatas = cadenaALista(candidata)

    for letraCandidata in letrasCandidatas:
        if not esta(letrasEnPantalla,letraCandidata): #letraCandidata son cada uno de las letras de la cadena ingresada por el usuario
            return False #alguna de la letra que se ingreso, no aparece en pantalla

    if esta(candidata,letraPrincipal) and esta(diccionario,candidata): #si la letra principal esta en las letras candidatas y
            return True                                                     #la palabra candidata esta en la lista diccionario, candidata es valida.
    return False  #candidata no tiene la letra principal o no esta en el diccionario

#devuelve los puntos
def Puntos(candidata):
    if len(candidata) <= 2: #resta 1 punto si la palabra ingresada fue de 2 o menos caracteres
        return -1
    elif len(candidata) == 3:
        return 1
    elif len(candidata) == 4:
        return 2
    elif len(candidata) == 7: #primero el 7, porque sino nunca va a entrar en esta condicion, debido al >=5
        return 10
    elif len(candidata) >= 5:
        return len(candidata)

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    #letraPrincipal es una sola letra
    #letrasEnPantalla es una cadena
    #diccionario es una lista de palabras
    palabrasCorrectas = []

    for palabra in diccionario:
        if esta(palabra,letraPrincipal): #la palabra contiene la letra principal
            palabraLetras = cadenaALista(palabra)           #c/u de las letras de la palabra de diccionario en una lista
            cadena=""                                       #esta cadena vacia tiene que ser completada con las letras en pantalla
            for letra in palabraLetras:                     #recorro la lista de la letras de la palabra de diccionario
                if esta(letrasEnPantalla,letra):            #si letra esta en la cadena de las 7 letras de la pantalla
                        cadena += letra                     #la agrega a cadena, y va concatenandolas
            if cadena==palabra:        #si la cadena construida previamente es igual
                palabrasCorrectas.append(palabra)

    return palabrasCorrectas