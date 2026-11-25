from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        self.G.clear()
        if self._nodes is None:
            self._nodes = DAO.read_all_filiali()
        if self._edges is None:
            self._edges = DAO.read_all_collegamenti()
        self.G.add_nodes_from(self._nodes)
        id_map = {}
        for f in self._nodes:
            id_map[f.id] = f
        for c in self._edges:
            if c.importo_medio >= threshold:
                u = id_map[c.id_filiale_1]
                v = id_map[c.id_filiale_2]
                self.G.add_edge(u, v, weight=c.importo_medio)

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return list(self.G.edges(data=True))
