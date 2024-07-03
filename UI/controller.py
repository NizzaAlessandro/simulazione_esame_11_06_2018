import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno = None
        self.stato = None



    def handleAvvistamenti(self, e):
        if self.anno is None:
            self._view.create_alert("Anno non selezionato")
            return
        self._model.buildGraph(int(self.anno))
        n,e = self._model.graphDetails()
        self._view.txtGrafo.clean()
        self._view.txtGrafo.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self.fillDDStato(list(self._model.graph.nodes))
        self._view.update_page()


    def handleAnalizza(self, e):
        if self.stato is None:
            self._view.create_alert("Stato non selezionato")
            return
        uscenti, entranti, raggiungibili = self._model.analizza(self.stato)
        self._view.txtAnalizza.clean()
        self._view.txtAnalizza.controls.append(ft.Text(f"Successori"))
        for u in uscenti:
            self._view.txtAnalizza.controls.append(ft.Text(f"{u[1]}"))
        self._view.txtAnalizza.controls.append(ft.Text(f"Precedenti"))
        for e in entranti:
            self._view.txtAnalizza.controls.append(ft.Text(f"{e[0]}"))
        self._view.txtAnalizza.controls.append(ft.Text(f"Raggiungibili"))
        for r in raggiungibili:
            self._view.txtAnalizza.controls.append(ft.Text(f"{r}"))
        self._view.update_page()


    def handleSequenza(self, e):
        if self.stato is None:
            self._view.create_alert("Stato non selezionato")
            return
        solBest = self._model.calcola_percorso(self.stato)
        self._view.txtSequenza.clean()
        for i in solBest:
            self._view.txtSequenza.controls.append(ft.Text(f"{i}"))
        self._view.update_page()

    def fillDDAnno(self):
        anni = self._model.fillDDAnno()
        anniDD = list(map(lambda x: ft.dropdown.Option(key=x[0], text=x[0] + "-" + x[1], on_click=self.getAnno), anni))
        self._view.ddanno.options = anniDD


    def fillDDStato(self, stati):
        statiDD = list(map(lambda x: ft.dropdown.Option(key = x.id, text=x, on_click=self.getStato), stati))
        self._view.ddstato.options = statiDD
        self._view.update_page()


    def getAnno(self, e):
        if e.control.key is None:
            pass
        else:
            self.anno = e.control.key

    def getStato(self, e):
        if e.control.key is None:
            pass
        else:
            self.stato = e.control.key

           