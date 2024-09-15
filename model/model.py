import copy
import random

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
      pass
    def getAnni(self):
        return DAO().getAnniDAO()

    def creaGrafo(self,anno):
        self.grafo = nx.DiGraph()
        nodi = DAO().getNodiDAO(anno)
        self.grafo.add_nodes_from(nodi)
        archi = DAO().getArchiDAO(anno)
        self.grafo.add_edges_from(archi)

    def precessori(self,nodo):
        pred = list(nx.predecessor(self.grafo, nodo))
        return pred

    def successivi(self,nodo):
        pred = list(self.grafo.successors(nodo))
        return pred

    """def cammino(self,nodo):
        nodi=nx"""
