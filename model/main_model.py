from database.DAO import DAO

import networkx as nx


class Model:

    def __init__(self):
        self._edges = None
        self._nodes = None
        self._grafo = nx.Graph()
        self._mappaNodixID = {}

    def buildGraph(self,threshold):
        self._grafo.clear()
        self._nodes = DAO.getAllAirports()
        self.fillMappaNodixID()
        self._grafo.add_nodes_from(self._nodes)
        self._edges = DAO.getAllRotteV2()

        for rotta in self._edges:
            peso = rotta.avgDistance
            a1Object = self._mappaNodixID[rotta.a1]
            a2Object = self._mappaNodixID[rotta.a2]

            if peso > threshold:
                self._grafo.add_edge(a1Object, a2Object, weight = peso)
                print(f"ARCO AGGIUNTO -> {rotta}")

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getAllEdges(self):
        return self._grafo.edges

    def fillMappaNodixID(self):
        for nodo in self._nodes:
            self._mappaNodixID[nodo.ID] = nodo


    def getAvgDist(self, v1, v2):
        data =  self._grafo.get_edge_data(v1, v2)
        return data["weight"]


if __name__ == "__main__":
    m = Model()
    m.buildGraph(1000)  # Costruisci il grafo con soglia 1000 miglia

    print(m.getNumNodes())
    print(m.getNumEdges())
    for arco in m.getAllEdges():
        print(arco, m.getAvgDist(arco[0],arco[1]))

    # Ordina gli archi per distanza media crescente
    for a1, a2 in sorted(m.getAllEdges(), key=lambda arco: m.getAvgDist(arco[0], arco[1])):
        print(f"({a1.AIRPORT}, {a2.AIRPORT}) {m.getAvgDist(a1, a2):.1f}")



