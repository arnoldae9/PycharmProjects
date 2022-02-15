import numpy as np
data = open('tsp225.tsp','r')  # abre el archivo
datos = data.read().split("\n") # lee los elementos del archivo
lista = []
#crear una lista con los subconjuntos
subconjuntos = []
A = []
stop = ['E0F']
for item in datos:
    if datos.index(item) >= 6 and datos.index(item) < 231:
        A.append(item.split( ))
# print(A)
nombre = datos[0]
print(nombre)
#convertir a enteros
for b in A:
    for a in b:
        b[b.index(a)] = float(a)


visitados = []
# función de disancia
def distancia(  a, b):
    return ((a[1]-b[1])**(2)+(a[2]-b[2])**(2))**0.5


matriz = []
for item in A:
    for i in range(len(A)):
        for j in range(len(A)):
            lista.append(distancia(A[i],A[j]))
        matriz.append(lista)
        lista = []


# print(len(A))
# print(matriz[171])
# Hay dos entradas repetidas....
# función mínimo de una lista
def menor(lista):
    min = lista[0]
    for x in lista:
            if x < min:
                min = x
    return min
limite=[]
for k in range(225):
    limite.append(k)

nodoi = 1
while set(visitados) != set(limite) :
    min = max(matriz[nodoi])
    # print(min)
    for item in matriz[nodoi]:
        if item != matriz[nodoi][nodoi]:
            if matriz[nodoi].index(item) not in visitados:
                if item < min:
                    min = item
    # print(min)
    nodoi=matriz[nodoi].index(min)
    # print(nodoi)
    if nodoi not in visitados:
        visitados.append(nodoi)
    else:
        break
    # for item in range(280):
    #     if item not in visitados:
    #         print(item)

    # print(visitados)
    print(len(visitados))

    with open('resultados.txt','w') as f:
        f.write("%s \n" %nombre)
        for item in visitados:
            f.write("%s \n" % item)

    # x=
    # for item in range(130):
    #     if item not in x:
    #         print(item)
    # set(visitados) != set(limite)

distancia2 = 0
for i in visitados:
    for j in visitados:
        if i != j:
            if i - j ==1:
                distancia2 = distancia2 + matriz[i][j]
print(distancia2)
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