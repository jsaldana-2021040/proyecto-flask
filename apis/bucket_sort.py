import random
import time

strLinea: str = '--------------------------------------------------------'
contador = 0

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

    tipo = int(solicitarDatos('| que tipo de lista va a ordenar: \n| 1.Autogenerada \n| 2.leer de lista ya generada:\n|\n|>> '))
    numeros = []
        
    if tipo == 1: # Lista propia
        cantidad = int(solicitarDatos('| Cuantos elementos quiere en el arreglo:\n|>> '))
        f = open("list_numbers.txt", "w")

        i = 0
        while i < cantidad:
            if i == cantidad - 1:
                f.write(str(random.randint(1,49)))
            else:
                f.write(str(random.randint(1,49)) + ' ')
            i+=1

        f = open("list_numbers.txt", "r")
        numeros = f.read().split(" ")
    elif tipo == 2:
        f = open("list_numbers.txt", "r")
        numeros = f.read().split(" ")  

    opcion = int(solicitarDatos('| de que manera quiere ordenarlos:\n| 1.asc\n| 2.desc\n|>> '))

    verPasos = int(solicitarDatos('| Desae ver los pasos?: \n| 1.Si \n| 2.No\n|\n|>> '))

    casilleros = [[],[],[],[],[]]
    limite1: int = 0
    limite2: int = 9
    
    numCasillero: int = 0
    
    tiempo = time.time()
    for index in range(len(numeros)):
        for num in numeros:
            if (int(num) >= limite1  and int(num) <= limite2):
                casilleros[numCasillero].append(num)
                
        numCasillero+=1
        limite1+=10
        limite2+=10

    if verPasos == 1:
        print(numeros)
        print('Paso bucket', ':', casilleros)
    
    for data in casilleros:
        for index in range(len(data) - 1):
            intercambio: bool = False
            if opcion == 1:
                intercambio = data[index] > data[index + 1]
            elif opcion == 2:
                intercambio = data[index] < data[index + 1]
                
            if intercambio:
                numActual = data[index + 1]
                data[index + 1] = data[index]
                data[index] = numActual

            if verPasos == 1:
                contador+=1
                print('paso', contador,':', casilleros)

    tiempoFinal = time.time()

    casilleros = casilleros[0] + casilleros[1] + casilleros[2] + casilleros[3] + casilleros[4]
    impresionLinea('| RESULTADO: ' + str(casilleros))
    impresionLinea('| Tiempo total: ' + str(tiempoFinal - tiempo))

    opSalir = int(solicitarDatos('| Desea realizar un nuevo ordenamiento (1=Si, 2=No, Salir):\n|>> '))
    salir = True if opSalir == 2 else False