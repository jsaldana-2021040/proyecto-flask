import random
import time

strLinea: str = '--------------------------------------------------------'

numeros = []

contador = 0

largoArray: int = 0

def solicitarDatos(msg: str) -> str:
    print(strLinea)
    valor: str = input(msg)
    print(strLinea)
    return valor

def impresionLinea(txt: str):
    print(strLinea)
    print(txt)
    print(strLinea)


salir: bool = False
while not salir:
    tipo = int(solicitarDatos('| que tipo de lista va a ordenar: \n| 1.Propia \n| 2.Autogenerada\n| 3.leer de lista ya generada:\n|\n|>> '))
        
    if tipo == 1: # Lista propia
        entrada = solicitarDatos('| ingrese los numeros separados por comas:\n|>> ')
        numeros = entrada.split(',')
        largoArray = len(numeros)
    elif tipo == 2: # Lista autogenerada
        cantidad = int(solicitarDatos('| Cuantos elementos quiere en el arreglo:\n|>> '))
        f = open("list_numbers.txt", "w")

        i=0
        while i < cantidad:
            if i == cantidad - 1:
                f.write(str(random.randint(1,99)))
            else:
                f.write(str(random.randint(1,99)) + ' ')
            i+=1

        f = open("list_numbers.txt", "r")
        numeros = f.read().split(" ")

    elif tipo == 3:
        f = open("list_numbers.txt", "r")
        numeros = f.read().split(" ")
        largoArray = len(numeros)
    else:
        print('seleccione una opcion valida')
        exit()

    opcion = int(solicitarDatos('| de que manera quiere ordenarlos:\n| 1.asc\n| 2.desc\n|>> '))

    verPasos = int(solicitarDatos('| Desae ver los pasos?: \n| 1.Si \n| 2.No\n|\n|>> '))

    tiempo = time.time()
    for num in range(largoArray - 1):

        intercambio: bool = False
              
        for index in range(largoArray - (num + 1)):

            if opcion == 1:
                intercambio = numeros[index] > numeros[index + 1]
            elif opcion == 2:
                intercambio = numeros[index] < numeros[index + 1]

            if intercambio:
                    
                    numActual = numeros[index + 1]

                    numeros[index + 1] = numeros[index]

                    numeros[index] = numActual

            if verPasos == 1:
                contador+=1
                print('paso', contador,':', numeros)


        for index in range(largoArray - (num + 1)):
            
            if opcion == 1:
                intercambio = numeros[largoArray-(index+1)] < numeros[largoArray-(index+2)]
            elif opcion == 2:
                intercambio = numeros[largoArray-(index+1)] > numeros[largoArray-(index+2)]
                
            if intercambio:
                
                numActual = numeros[largoArray-(index+1)]

                numeros[largoArray-(index+1)] = numeros[largoArray-(index+2)]

                numeros[largoArray-(index+2)] = numActual
        
            if verPasos == 1:
                contador+=1
                print('paso inverso', contador,':', numeros)

    tiempoFinal = time.time()

    impresionLinea('| RESULTADO: ' + str(numeros))
    impresionLinea('| Tiempo total: ' + str(tiempoFinal - tiempo))

    opSalir = int(solicitarDatos('| Desea realizar un nuevo ordenamiento (1=Si, 2=No, Salir):\n|>> '))
    salir = True if opSalir == 2 else False