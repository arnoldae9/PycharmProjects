import numpy as np
import random
import os
#TODO Como proyecto personal, utilizar funciones y clases para recortar el código

#TODO Selección de los archivos:
direccion = '/home/arnold/PycharmProjects/pythonProject'
contenido = os.listdir(direccion)
contenido
tsp = []
for item in contenido:
    if os.path.isfile(os.path.join(direccion, item)) and item.endswith('.tsp'):
        tsp.append(item)
print(tsp) #TODO el orden de los archivos es: ['tsp225.tsp', 'a280.tsp', 'ch130.tsp', 'pr76.tsp', 'lin105.tsp']
#TODO la lista tsp2 es por si alguna de las instancias falla
tsp2= [tsp[4]]
for archivo in tsp:
    itersinmejora = 0
    xasterisco = 99999999999
    while (itersinmejora < 3):
        print("Iteración: ",itersinmejora+1)
        data = open(archivo, 'r')  # abre el archivo
        datos = data.read().split("\n")  # lee los elementos del archivo
        lista = []
        nombre = datos[0]
        dimension = datos[3].split()
        dim = int(dimension[2])
        print(nombre)
        print(dim)
        #TODO crea una lista con los subconjuntos
        subconjuntos = []
        A = []
        stop = ['E0F']
        for item in datos:
            if datos.index(item) >= 6 and datos.index(item) < dim + 6:
                A.append(item.split())


        #TODO convertir a enteros
        for b in A:
            for a in b:
                b[b.index(a)] = float(a)
        A = np.array(A)
        # print(A)

        # función de distancia
        def distancia(a, b):
            return ((a[1]-b[1])**(2)+(a[2]-b[2])**(2))**0.5

        #TODO matriz de distancias
        lista = []
        matriz = []
        for i in range(len(A)):
            for j in range(len(A)):
                # print(distancia(A[i],A[j]))
                lista.append(distancia(A[i], A[j]))
            matriz.append(lista)
            lista = []
        matriz = np.array(matriz)
        # print(matriz)

        # print(len(A))
        # print(matriz2)
        # print(matriz)

        # Hay dos entradas repetidas....
        # función mínimo de una lista
        #TODO definición de una función que encuentra el menor de una lista (no se usa)
        def menor(lista):
            min = lista[0]
            for x in lista:
                if x < min:
                    min = x
            return min

        #TODO limite de nodos
        limite = []
        for k in range(dim):
            limite.append(k)

        # print("¿Con que nodo deseas empezar? \n")
        nodoi = random.randint(0,dim-1)
        nodoinicial = nodoi
        print("El nodo inicial es: ",nodoi)
        visitados = []
        alfa = 0.1
        # alfa = random.random()
        # print("alfa = " , alfa)
        # print(alfa)
        #TODO inicio del ciclo constructivo
        while len(visitados) <= 280:
            if nodoi not in visitados:
                visitados.append(nodoi)
            else:
                break
            novisitados = set(limite) - set(visitados)
            listcostdisp = []
            for i in novisitados:
                # costosdisponibles = costdisp
                costdisp = matriz[nodoi][i]
                listcostdisp.append(costdisp)
                # print(listcostdisp)
            if len(listcostdisp) >= 2: 
                max = np.max(listcostdisp)
                # print(max)
                min = np.min(listcostdisp)
                # print(min)
                rango = max - min
                cijmin = min+min*alfa
                aleatorios = []
                for item in listcostdisp:
                    if item <= cijmin:
                        aleatorios.append(item)
                aleatorios2 = np.where(matriz[nodoi] == item )
                aleatorios2 = np.array(aleatorios2).ravel().tolist()
                seleccionables = []
                for item in aleatorios2:
                    if item not in visitados and item not in seleccionables:
                        seleccionables.append(item)        
                nodoi = np.random.choice(seleccionables)
                if len(seleccionables) == 1:
                    nodoi = seleccionables[0]
                # print(nodoi)
                # print(nodoi)
            else:
                for item in range(dim):
                    if item not in visitados:
                        x = item
                        visitados.append(x)
                break
            # print(nodoi)
        # print(visitados)
        # print(len(visitados))
        for item in range(dim):
                if item not in visitados:
                    print(item)
        distancia2 = 0
        for i in visitados:
            for j in visitados:
                if visitados.index(i) != visitados.index(j):
                    if visitados.index(i) - visitados.index(j) == 1:
                        distancia2 = distancia2 + matriz[i][j]
        distanciatotal = distancia2 + matriz[visitados[-1]][visitados[0]]
        print(distanciatotal)
        if distanciatotal < xasterisco:
            xasterisco = distanciatotal
            visitadosasterisco = visitados
        else:
            itersinmejora = itersinmejora + 1
        #TODO crea la escritura en un archivo txt
        distancia2 = 0
        for i in visitados:
            for j in visitados:
                if visitados.index(i) != visitados.index(j):
                    if visitados.index(i) - visitados.index(j) == 1:
                        distancia2 = distancia2 + matriz[i][j]
        distanciatotal = distancia2 + matriz[visitados[-1]][visitados[0]]
        print("Distancia: ", distanciatotal)
        with open('resultadositeraciones.txt', 'a') as f:
            f.write("%s \n" % nombre)
            f.write("nodo de inicio: %i \n" %nodoinicial)
            f.write("alfa = %f \n" % alfa)
            f.write("Distancia después de la construcción: %f \n" % distanciatotal)
            f.write("Ruta: \n")
            for item in visitados:
                f.write(" %i " % item)
            f.write("\n")
    else:
        print("terminado")
        print("mejor resultado obtenido: " ,xasterisco)

    #TODO inicio de la busqueda local
        iter = visitadosasterisco
        print(iter)
        nodosintercambiables = []
        for inicio in iter:
            for final in iter:
                if inicio != final and inicio != iter[0] and final != iter[0]:
                    nodosintercambiables.append([inicio, final])
        res = list(set(tuple(sorted(sub)) for sub in nodosintercambiables))

        print(res)
        for item in res:
            nodo1 = item[0]
            nodo2 = item[1]
            print(nodo1, nodo2)
            i = iter.index(nodo1)
            j = iter.index(nodo2)
            if i > j:
                i = iter.index(nodo2)
                j = iter.index(nodo1)
            print(i, j)
            if j - i == 1 or j - i == -1:
                if i == dim - 1:
                    y = 0
                else:
                    y = i + 1
                if j == dim - 1:
                    x = 0
                else:
                    x = j + 1
                costoactual = matriz[iter[i-1]][iter[i]] + \
                    matriz[iter[i]][iter[j]] + matriz[iter[j]][iter[x]]
                # print(matriz[iter[i-1]][iter[i]],matriz[iter[i]][iter[j]], matriz[iter[j]][iter[x]])
                print(costoactual)
                # print("aqui")
                costonuevo = matriz[iter[i-1]][iter[j]] + \
                    matriz[iter[j]][iter[i]] + matriz[iter[i]][iter[x]]
                # print(matriz[iter[i-1]][iter[j]] , matriz[iter[j]][iter[i]] , matriz[iter[i]][iter[x]])
                print(costonuevo)
                delta = costoactual - costonuevo
                if delta >= 0:
                    iter[i], iter[j] = iter[j], iter[i]
                    print("si se cambio")
                    visitadosasterisco = iter
                    print("los visitadosasterisco son: ", visitadosasterisco)
                    distancia2 = 0
                    for i in visitadosasterisco:
                        for j in visitadosasterisco:
                            if visitadosasterisco.index(i) != visitadosasterisco.index(j):
                                if visitadosasterisco.index(i) - visitadosasterisco.index(j) == 1:
                                    distancia2 = distancia2 + matriz[i][j]
                    distanciatotal = distancia2 + matriz[visitadosasterisco[-1]][visitadosasterisco[0]]
                    print("El total de la solucion es: ", distanciatotal)
                else:
                    print("no se cambio")
            else:
                if i == dim - 1:
                    y = 0
                else:
                    y = i + 1
                if j == dim - 1:
                    x = 0
                else:
                    x = j + 1
                costoactual = matriz[iter[i-1]][iter[i]] + matriz[iter[i]][iter[y]
                                                                        ] + matriz[iter[j-1]][iter[j]] + matriz[iter[j]][iter[x]]
                print(costoactual)
                # print(matriz[iter[i-1]][iter[i]] , matriz[iter[i]][iter[y]] , matriz[iter[j-1]][iter[j]] , matriz[iter[j]][iter[x]])
                costonuevo = matriz[iter[i-1]][iter[j]] + matriz[iter[j]][iter[y]
                                                                        ] + matriz[iter[i]][iter[j-1]] + matriz[iter[i]][iter[x]]
                # print(matriz[iter[i-1]][iter[j]] , matriz[iter[j]][iter[y]] , matriz[iter[i]][iter[j-1]] ,matriz[iter[i]][iter[x]])
                print(costonuevo)
                delta = costoactual - costonuevo
                if delta >= 0:
                    iter[i], iter[j] = iter[j], iter[i]
                    print("si se cambio")
                    visitadosasterisco = iter
                    distancia2 = 0
                    for i in visitadosasterisco:
                        for j in visitadosasterisco:
                            if visitadosasterisco.index(i) != visitadosasterisco.index(j):
                                if visitadosasterisco.index(i) - visitadosasterisco.index(j) == 1:
                                    distancia2 = distancia2 + matriz[i][j]
                    distanciatotal = distancia2 + matriz[visitadosasterisco[-1]][visitadosasterisco[0]]
                    print("El total de la solucion es: ", distanciatotal)
                else:
                    print("no se cambio")
            print(iter)
        #TODO crea la escritura en un archivo txt
        visitadosasterisco = iter
        distancia2 = 0
        for i in visitadosasterisco:
            for j in visitadosasterisco:
                if visitadosasterisco.index(i) != visitadosasterisco.index(j):
                    if visitadosasterisco.index(i) - visitadosasterisco.index(j) == 1:
                        distancia2 = distancia2 + matriz[i][j]
        distanciatotal = distancia2 + matriz[visitadosasterisco[-1]][visitadosasterisco[0]]
        print("Distancia después de la búsqueda local: ", distanciatotal)
        with open('resultadositeraciones.txt', 'a') as f:
            f.write("---------------------------------------------------------------------------------------------- \n")
            f.write("%s \n" % nombre)
            f.write("nodo de inicio: %i \n" %nodoinicial)
            f.write("alfa = %f \n" % alfa)
            f.write("Distancia después de la búsqueda local: %f \n" % distanciatotal)
            f.write("Ruta: \n")
            for item in visitadosasterisco:
                f.write(" %i " % item)
            f.write("\n")
            f.write("El mejor resultado obtenido en las iteraciones %f \n" %xasterisco)
            f.write("---------------------------------------------------------------------------------------------- \n")

