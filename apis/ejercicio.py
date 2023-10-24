Lista = [4, 6, 1, 8, 2, 1, 5, 9, 8, 3, 2, 6, 6, 2]

def buscarPareja(data = 1):
    for num in Lista:
        for index in range(1, len(Lista)):
            if (num + Lista[data]) != 6:
                data+=1
                buscarPareja(data)

            elif (num + Lista[index]) == 6 and num != Lista[index] :
                respuesta = [num, Lista[index]]
                print(respuesta)

buscarPareja()