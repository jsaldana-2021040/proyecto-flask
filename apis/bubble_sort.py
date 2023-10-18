import random

print('--------------------------------------------------------')
tipo = int(input('| que tipo de lista va a ordenar: \n| 1.Propia \n| 2.Autogenerada\n|\n|>> '))
print('--------------------------------------------------------')
    
if tipo == 1:
    print('--------------------------------------------------------')
    entrada = input('| ingrese los numeros separados por comas:\n|>> ')
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    opcion = int(input('| de que manera quiere ordenarlos:\n| 1.asc\n| 2.desc\n|>> '))
    print('--------------------------------------------------------')
    numeros = entrada.split(',')

    for num in range(len(numeros) - 1):
        if opcion == 1:
            for index in range(len(numeros) - (num + 1)):

                if numeros[index] > numeros[index + 1]:
                    
                    numActual = numeros[index + 1]

                    numeros[index + 1] = numeros[index]

                    numeros[index] = numActual

        if opcion == 2:
            for index in range(len(numeros) - (num + 1)):

                if numeros[index] < numeros[index + 1]:
                    
                    numActual = numeros[index + 1]

                    numeros[index + 1] = numeros[index]

                    numeros[index] = numActual
    
    print('--------------------------------------------------------')
    print('| ',  end='')
    print(*numeros, sep=", ")
    print('--------------------------------------------------------')


if tipo == 2:
    print('--------------------------------------------------------')
    cantidad = int(input('| Cuantos elementos quiere en el arreglo:\n|>> '))
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    opcion = int(input('| de que manera quiere ordenarlos:\n| 1.asc\n| 2.desc\n|>> '))
    print('--------------------------------------------------------')

    numeros = []
    i=0

    while i < cantidad:
        numeros.append(random.randint(1,99))
        i+=1

    for num in range(len(numeros) - 1):
        if opcion == 1:
            for index in range(len(numeros) - (num + 1)):

                if numeros[index] > numeros[index + 1]:
                
                    numActual = numeros[index + 1]

                    numeros[index + 1] = numeros[index]

                    numeros[index] = numActual

        if opcion == 2:
            for index in range(len(numeros) - (num + 1)):

                if numeros[index] < numeros[index + 1]:
                
                    numActual = numeros[index + 1]

                    numeros[index + 1] = numeros[index]

                    numeros[index] = numActual

    print('--------------------------------------------------------')
    print('| ',  end='')
    print(*numeros, sep=", ")
    print('--------------------------------------------------------')

if tipo > 2 :
    print('seleccione una opcion valida')