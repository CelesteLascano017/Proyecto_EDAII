from grafo import Grafo
from utils import cargar_nodos, cargar_aristas


class CampusEPN:

    def __init__(self):

        ruta_nodos = "gephi/nodos_grafo_campus_epn_gephi.csv"
        ruta_aristas = "gephi/edged_grafo_campus_epn_gephi.csv"

        self.graph = Grafo()
        self.id_a_nombre = cargar_nodos(ruta_nodos)
        aristas = cargar_aristas(ruta_aristas)

        for id_nodo in self.id_a_nombre.keys():
            self.graph.agregar_nodo(id_nodo)

        for source, target in aristas:
            self.graph.agregar_arista(source, target)

    def obtener_nombre_nodo(self, id_nodo):
        return self.id_a_nombre.get(id_nodo, None)
