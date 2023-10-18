numeros = [5,4,3,2,1]

contador = 0

for num in range(len(numeros) - 1):

    for index in range(len(numeros) - (num + 1)):

        if numeros[index] > numeros[index + 1]:
            
            numActual = numeros[index + 1]

            numeros[index + 1] = numeros[index]

            numeros[index] = numActual
        
        contador+=1
        print('paso', contador,':', numeros)

    for index in range(len(numeros) - (num + 1)):
        
        if numeros[len(numeros)-(index+1)] < numeros[len(numeros)-(index+2)]:
            
            numActual = numeros[len(numeros)-(index+1)]

            numeros[len(numeros)-(index+1)] = numeros[len(numeros)-(index+2)]

            numeros[len(numeros)-(index+2)] = numActual

            contador+=1
            print('paso al revez', contador,':', numeros)

print(numeros)