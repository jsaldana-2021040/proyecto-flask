import random

strLinea: str = '--------------------------------------------------------'

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
    tipo = int(solicitarDatos('| que tipo de lista va a ordenar: \n| 1.Propia \n| 2.Autogenerada\n|\n|>> '))
    numeros = []
        
    if tipo == 1: # Lista propia
        entrada = solicitarDatos('| ingrese los numeros separados por comas:\n|>> ')
        numeros = entrada.split(',')
    elif tipo == 2: # Lista autogenerada
        cantidad = int(solicitarDatos('| Cuantos elementos quiere en el arreglo:\n|>> '))
        i=0
        while i < cantidad:
            numeros.append(random.randint(1,99))
            i+=1
    else:
        print('seleccione una opcion valida')
        exit()

    opcion = int(solicitarDatos('| de que manera quiere ordenarlos:\n| 1.asc\n| 2.desc\n|>> '))

    # ordenamiento
    for num in range(len(numeros) - 1):
        for index in range(len(numeros) - (num + 1)):

            intercambio: bool = False
            if opcion == 1:
                intercambio = numeros[index] > numeros[index + 1]
            elif opcion == 2:
                intercambio = numeros[index] < numeros[index + 1]
                
            if intercambio:
                numActual = numeros[index + 1]
                numeros[index + 1] = numeros[index]
                numeros[index] = numActual

    impresionLinea('| RESULTADO: ' + str(numeros))

    salir = bool(solicitarDatos('| Desea realizar un nuevo ordenamiento (0=Si, 1=Salir):\n|>> '))