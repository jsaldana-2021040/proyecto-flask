numeros = [5,4,3,2,1]

contador = 0

largoArray = len(numeros)

for num in range(largoArray - 1):

    for index in range(largoArray - (num + 1)):

        if numeros[index] > numeros[index + 1]:
            
            numActual = numeros[index + 1]

            numeros[index + 1] = numeros[index]

            numeros[index] = numActual
        
        contador+=1
        print('paso', contador,':', numeros)

    for index in range(largoArray - (num + 1)):
        
        if numeros[largoArray-(index+1)] < numeros[largoArray-(index+2)]:
            
            numActual = numeros[largoArray-(index+1)]

            numeros[largoArray-(index+1)] = numeros[largoArray-(index+2)]

            numeros[largoArray-(index+2)] = numActual

            contador+=1
            print('paso al revez', contador,':', numeros)

print(numeros)