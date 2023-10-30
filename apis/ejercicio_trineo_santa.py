numeros = [1,2,3,2,1]

def trineo():
    previo = numeros[0]
    subida = 0
    bajada = 0

    for i in range(1, len(numeros)):
        if numeros[i] > previo:
            subida += 1
        elif numeros[i] < previo:
            bajada += 1

        previo = numeros[i]

    return subida == bajada

print(trineo())