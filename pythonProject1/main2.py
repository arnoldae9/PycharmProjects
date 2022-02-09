data = open('scp61.txt','r')  # abre el archivo
datos = data.read().split("\n") # lee los elementos del archivo
#print(datos)
#obtener numero de regiones y centros:
nm = datos[0].split()
for item in nm:
    nm[nm.index(item)] = int(item)
centros = nm[1]
regiones = nm[0]
print(centros,regiones)

#obtener los costos ij
    # obtenemos los indices de los costos nota: el indice 0 esta reservado para n,m
indicescostos = []
i=0
for line in datos:
    indicescostos.append(i)
    if len(line.split( )) == 1:
        break
    i += 1
#print(indicescostos)
costos =[]
A=[]
lista=[]
for i in range(len(indicescostos)-1):
    if i != 0:
        for j in range(indicescostos[i],indicescostos[i+1]):
            A.append(datos[j].split( ))
            costos = costos + A
            A=[]
for item in costos:
    lista = lista + item
costos = lista

for item in costos:
    costos[costos.index(item)] = int(item)
#print(costos)

#obtener los indices de las lineas con un solo número
indices = []
i=0
for line in datos:
    if len(line.split( )) == 1:
        indices.append(i)
    i += 1

#crear una lista con los subconjuntos
subconjuntos = []
A = []
for i in range(len(indices)-1):
    for j in range(indices[i],indices[i+1]):
        A.append(datos[j].split( ))
    subconjuntos.append(A)
    A=[]

#convertir a enteros
for b in subconjuntos:
    for a in b:
        for i in a:
            a[a.index(i)] = int(i)
#print(subconjuntos[0])

#juntar listas
lista = []
subconjuntos2 = []
j=-1
for i in range(len(subconjuntos)):
    j= j + 1
    for b in subconjuntos:
        if subconjuntos.index(b) == subconjuntos.index(subconjuntos[j]):
            for i in b:
                lista = lista + i
            subconjuntos2.append(lista)
            lista = []

#inicio del ciclo---------------------------------------------------------------
solucion = []
iterador = 0
while subconjuntos2 != []:
    #seleccionar el elemento que se repite mas quitando el primer elemento ya que es el indicador del centro
    contador = 0
    lista2 = []
    for i in range(centros):
        i+=1
        for item in subconjuntos2:
            for subitem in item:
                if item.index(subitem) != 0:
                    if i == subitem:
                        contador += 1
        lista2.append(contador)
        contador = 0
        #print(i)
    #print(lista2)
    #print(lista2.index(max(lista2))+1)
    maximo = lista2.index(max(lista2))+1
    solucion.append(maximo)
    if maximo == 1:
        break
    print(maximo)
    #print(len(lista2))

    #remover listas
        #-----hacemos una lista con los indices de las listas que queremos eliminar
    remover = []
    for item2 in subconjuntos2:
        if maximo in item2:
            remover.append(subconjuntos2.index(item2))
    #print(remover)
        #elimina las listas dependiendo de la lista remover
    subconjuntos2 = [palabra for index, palabra in enumerate(subconjuntos2) if(index not in remover)]
    #print(subconjuntos2)
#print(solucion)

#funcion para ordenar las listas por subconjunto de menor a mayor
def ordenarPorPosicionSubLista(subconjuntos2: list, posicionOrdenar: int) -> list:
    return(sorted(subconjuntos2, key = lambda elemento: elemento[posicionOrdenar-1]))
Z=0

for i in solucion:
    i -= 1
    Z += costos[i]*1

#escribir en un txt los subconjuntos este solo fue de prueba...
i=0
with open('archivo.txt', 'w') as temp_file:
    temp_file.write("Cantidad de Regiones: %i \n" %regiones)
    temp_file.write("Cantidad de Centros: %i \n" %centros)
    temp_file.write("Los centros seleccionados son: \n")
    for item in solucion:
        temp_file.write("     %i \n" %item)
    temp_file.write("Con un costo total de: %i \n" %Z)
file = open('archivo.txt', 'r')
#print(file.read())
"""la lista subconjuntos2 es la lista donde cada elemento es una lista del subconjunto"""