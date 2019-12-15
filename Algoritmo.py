from Grafo import G
from Node import Node
from Coordenadas import Cordenadas
from Estaciones import Estacion
import geopy.distance

# Algoritmo A*
def astar(start, end):
    
    # Lineas
    lineas = []
    # Se inicializa el mapa
    cordenadas = Cordenadas()
    cordenadas.añadir()
   
    # Crea los nodos start y end
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Inicializa la lista abierta y la lista cerrada
    open_list = []
    closed_list = []

    # Añade el nodo start a la lista abierta
    open_list.append(start_node)

    # Itera hasta que llega al final
    while len(open_list) > 0:

        # Almacena el nodo actual
        current_node_ = open_list[0]
        # Ordena la lista         
        open_list.sort()
        # Coge el nodo mas pequeño 
        current_node = open_list[0]
        # Saca el nodo actual de la lista abierta y lo añade a la cerrada
        open_list.pop(0)
        # Metemos el nodo en la lista cerrada
        closed_list.append(current_node)
        
        # Calculamos las Lineas
        lineas = compLineas(cordenadas, current_node_.name, current_node.name)
        
        # Llega al final
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.name)
                current = current.parent
            return path[::-1] # Devuelve el camino al reves

        # Genera los hijos 
        children = []

        # Creamos una lista con los hijos
        hijos = cordenadas.getEstaciones()[current_node.name].getParadas()

        # Iteramos entre los hijos
        for new_station in hijos:

            # Crea un nodo
            new_node = Node(current_node, new_station)
            # Lo añade a la lista
            children.append(new_node)

        # Itera en la lista de hijos
        for child in children:

            # Si el hijo esta en la lista cerrada 
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Get lineas
            #Lineas__ = compLineas(cordenadas, current_node.name, child.name)
            # Crea los valores F, H y G
            transbordo = getTransbordo(lineas, compLineas(cordenadas, current_node.name, child.name))
            child.g = current_node.g + distanciaG(current_node.name, child.name) + transbordo
            child.h = distanciaH(cordenadas , child.name, end_node.name)
            child.f = child.g + child.h
                        
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Añade el hijo a la lista abierta
            open_list.append(child)


# Calcula la distancia G
def distanciaG(origen, destino):
    return G.get_edge_data(origen, destino)['weight']

# Calcula la distancia H
def distanciaH(cordenadas, origen, destino):
    cord1 = cordenadas.getEstaciones()[origen].getCordenada()
    cord2 = cordenadas.getEstaciones()[destino].getCordenada()
    return geopy.distance.distance(cord1, cord2).km 

def compLineas(cordenadas, origen, destino):
    lista = []
    linea1 = cordenadas.getLinea(origen)
    linea2 = cordenadas.getLinea(destino)
    for element in linea1:
        if element in linea2:
            lista.append(element)
    return lista

def getTransbordo(linea1, linea2):
    if len(linea1) == 0:
        return 0
    for element in linea1:
        if element in linea2:
            return 0
    return 1.5

