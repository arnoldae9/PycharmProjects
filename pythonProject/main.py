data = open('a280.tsp','r')  # abre el archivo
datos = data.read().split("\n") # lee los elementos del archivo
lista = []
#crear una lista con los subconjuntos
subconjuntos = []
A = []
stop = ['E0F']
for item in datos:
    if datos.index(item) >= 6 and datos.index(item) < 286:
        A.append(item.split( ))
# print(A)

#convertir a enteros
for b in A:
    for a in b:
        b[b.index(a)] = int(a)
print(A)