import random
import getpass
import openpyxl

def validar(minimo,maximo):
    opcion = 0
    while opcion < minimo or opcion > maximo:
        opcion = int(input('Escribe una opcion entre ' + str(minimo) + ' y ' + str(maximo) + ':'))
        if opcion < minimo or opcion > maximo:
            print('**Valor Erroneo, recuerda que tu numero debe estar entre ' + str(minimo) + ' y ' + str(maximo))
            print()
    return opcion
    
def validaroculto(minimo,maximo):
    opcion = 0
    while opcion < minimo or opcion > maximo:
        opcion = int(getpass.getpass('Escribe un número entre ' + str(minimo) + ' y ' + str(maximo) + ':'))
        if opcion < minimo or opcion > maximo:
            print('**Valor Erroneo, recuerda que tu numero debe estar entre ' + str(minimo) + ' y ' + str(maximo))
            print()
    return opcion

def nombre():
    print()
    print('Ahora por favor dame tu nombre para registrar tus datos')
    print()
    nomb=input('Nombre:')
    print()
    print('--Perfecto ' + str(nomb) + ' tus datos se han guardado correctamente!')
    print()
    return nomb
    

def juego(vidas,numeroadivinar):
    numeroadivinado=-1
    intentos=0
    while  intentos<vidas and numeroadivinado!=numeroadivinar:
        numeroadivinado=int(input('Trata de adivinar el número:'))
        print()
        if numeroadivinado<numeroadivinar:
            print('-NOO, el numero que buscas es mayor!')
            intentos= intentos+1
            print()
            print('(Recuerda que te quedan ' + str(vidas-intentos)+ ' vidas)')
        if numeroadivinado>numeroadivinar:
            print('-No, el numero que buscas es menor!')
            intentos= intentos+1
            print()
            print('(Recuerda que te quedan ' + str(vidas-intentos)+ ' vidas)')
        if numeroadivinado==numeroadivinar:
            
            print('************************************************************')
            print('          SIIII!!!!, acertaste el numero era ' + str(numeroadivinado))
            print('************************************************************')
            nomb=nombre()
            resultado= 'Gano'            
        if intentos>=vidas:
            
            print('************************************************************')
            print('          NOOOO!!!!, PERDISTE, el número era ' + str(numeroadivinado))
            print('************************************************************')
            nomb=nombre()
            resultado= 'Perdio'
    return resultado, intentos, nomb
            
def exportardatos(nomb,intentos,resultado):
    
    documentoexcel= openpyxl.load_workbook('C:/EjerciciosPython/datosjugadores.xlsx')
    Hoja = documentoexcel['Hoja 1']
    Hoja.append([nomb, intentos+1, resultado])
    documentoexcel.save('C:/EjerciciosPython/datosjugadores.xlsx')
    print('Gracias por Jugar!!')
    print()
    print('------------------------------------------------------------------')
    print()

def estadist():
    print()
    print('------------------------------------------------------------------')
    print()
    print('A continuación te muestro una tabla con los datos de los jugadores:')
    print()
    documentoexcel= openpyxl.load_workbook('C:/EjerciciosPython/datosjugadores.xlsx')
    Hoja = documentoexcel['Hoja 1']
    dimensiones = Hoja.calculate_dimension()
    rangoceldas = Hoja[dimensiones]
    for linea in rangoceldas:
        for celda in linea:
            print(str(celda.value) + " | ", end="")
        print()
    print()
    print('------------------------------------------------------------------')
    print()