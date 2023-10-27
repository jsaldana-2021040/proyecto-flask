numeros = [1,2,3,2,1]

def trineo():
    previo = numeros[0]
    subida = True
    estado = True
    for i in range(1, len(numeros)):
        if not len(numeros) < 3 :
            if numeros[i] > previo and subida == True: 
                previo = numeros[i]
            else:
                subida = False
            if numeros[i] < previo and subida == False:
                previo = numeros[i]
            else:
                estado = False
                
            return estado
        else:
            return False
    
print(trineo())