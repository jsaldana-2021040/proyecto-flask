lista = input('ingrese los nombres de los archivos separados por comas\n')

files = lista.split(", ")

# file, video, file, video, file, video, file, video

result = []

def archivosRepetidos(files):
    repetidos = 0
    for i in range(len(files)):
        if files[i] in result:
            repetidos+=1
            valor = files[i] + '(' + str(repetidos) + ')'
            if valor in result:
                valor = files[i] + '(' + str(repetidos + 1) + ')'
            else:
                repetidos-=1
            result.append(valor)
        else:
            result.append(files[i])
    
    result.sort()
    print(result)


archivosRepetidos(files)