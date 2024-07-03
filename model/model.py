import copy
import random

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.idMap = {}


    def buildGraph(self, anno):
        self.graph.clear()
        self.idMap = {}
        nodi = DAO.getNodi(anno)
        for n in nodi:
            self.graph.add_node(n)
            self.idMap[n.id] = n
        archi = DAO.getArchi(anno)
        for a in archi:
            self.graph.add_edge(self.idMap[a[0]], self.idMap[a[1]])


    def analizza(self, stato):
        start = self.idMap[stato]
        usc = list(self.graph.out_edges(start))
        entr = list(self.graph.in_edges(start))
        compConn = list(nx.dfs_successors(self.graph, source=start))
        raggiungibili = []
        for i in compConn:
            if i != start and (start, i) not in usc or (i, start) not in entr:
                raggiungibili.append(i)
        return usc, entr, raggiungibili

    def calcola_percorso(self, s):
        stato = self.idMap[s]
        self.solBest  = []
        parziale = [stato]
        self.ricorsione(parziale)
        return self.solBest


    def ricorsione(self, parziale):
        vicini = list(self.graph.neighbors(parziale[-1]))
        viciniAmmissibili = self.getAmmissibili(parziale, vicini)
        if len(viciniAmmissibili) == 0 and len(parziale) > len(self.solBest):
            self.solBest = copy.deepcopy(parziale)
        else:
            for v in viciniAmmissibili:
                parziale.append(v)
                self.ricorsione(parziale)
                parziale.pop()



    def getAmmissibili(self, parziale, vicini):
        ammissibili = []
        if len(parziale) == 1:
            ammissibili = copy.deepcopy(vicini)
            return ammissibili
        for v in vicini:
            if v not in parziale:
                ammissibili.append(v)
        return ammissibili






    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)


    def fillDDAnno(self):
        anni = DAO.getAnni()
        return anni