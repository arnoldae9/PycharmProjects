import numpy as np
data = open('pr76.tsp','r')  # abre el archivo
datos = data.read().split("\n") # lee los elementos del archivo
lista = []
nombre = datos[0]
dimension = datos[3].split( )
dim = int(dimension[2])
print(nombre)
print(dim)
#crear una lista con los subconjuntos
subconjuntos = []
A = []
stop = ['E0F']
for item in datos:
    if datos.index(item) >= 6 and datos.index(item) < dim +6 :
        A.append(item.split( ))


#convertir a enteros
for b in A:
    for a in b:
        b[b.index(a)] = float(a)
A = np.array(A)
# print(A)

visitados = []
# función de disancia
def distancia(  a, b):
    return ((a[1]-b[1])**(2)+(a[2]-b[2])**(2))**0.5

lista = []
matriz = []
for i in range(len(A)):
    for j in range(len(A)):
        # print(distancia(A[i],A[j]))
        lista.append(distancia(A[i],A[j]))
    matriz.append(lista)
    lista = []
matriz = np.array(matriz)
print(matriz)

# print(len(A))
# print(matriz2)
# print(matriz)

# Hay dos entradas repetidas....
# función mínimo de una lista
def menor(lista):
    min = lista[0]
    for x in lista:
            if x < min:
                min = x
    return min
limite=[]
for k in range(dim):
    limite.append(k)

nodoi = 0
while len(visitados) <=dim:
    if nodoi not in visitados:
        visitados.append(nodoi)
    else:
        break
    min = np.amax(matriz[nodoi])
    print(min)
    novisitados = set(limite) - set(visitados)
    print(novisitados)
    for i in novisitados:
        print(i)
        item = matriz[nodoi][i]
        if item < min:
            min = item
    resultado = np.where(matriz[nodoi] == min)
    for item in resultado[0]:
        item = int(item)
        if item in novisitados:
            nodoi = item
    print(nodoi)
    print("el minimo es:")
    print(min)

    #print(nodoi)

    # for item in range(280):
    #     if item not in visitados:
    #         print(item)

    print(visitados)
    print(len(visitados))

    with open('resultados.txt','w') as f:
        f.write("%s \n" %nombre)
        for item in visitados:
            item2= item+1
            f.write("%s \n" % item2)

    # x=
    # for item in range(130):
    #     if item not in x:
    #         print(item)
    # set(visitados) != set(limite)

distancia2 = 0
for i in visitados:
    for j in visitados:
        if visitados.index(i) != visitados.index(j):
            if visitados.index(i) - visitados.index(j) ==1:
                distancia2 = distancia2 + matriz[i][j]
distanciatotal = distancia2 + matriz[visitados[-1]][visitados[0]]
print(distanciatotal)
#
# data = open('tsp225.opt.tour','r')  # abre el archivo
# datos = data.read().split("\n") # lee los elementos del archivo
# lista = []
# #crear una lista con los subconjuntos
# subconjuntos = []
# A = []
# stop = ['E0F']
# for item in datos:
#     if datos.index(item) >= 6 and datos.index(item) < 231:
#         A.extend(item.split( ))
# # print(A)
# nombre = datos[0]
# print(nombre)
# #convertir a enteros
# B=[]
# for b in A:
#     B.append(int(b))
# print(B)
#
#
# distancia2 = 0
# for i in B:
#     for j in B:
#         if i != j:
#             if i - j ==1:
#                 distancia2 = distancia2 + matriz[i][j]
# print(distancia2)