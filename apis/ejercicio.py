Lista = [4, 6, 1, 8, 2, 1, 5, 9, 8, 3, 2, 6, 6, 2]

resultados = []

def buscarPareja(list, target, current=[], index=0):
    if target == 0:
        current.sort()
        if current not in resultados:
            resultados.append(current)
    for i in range(index, len(list)):
        buscarPareja(list, target - list[i], current + [list[i]], i + 1)

target = 10
buscarPareja(Lista, target)
print(resultados)
print(len(resultados))