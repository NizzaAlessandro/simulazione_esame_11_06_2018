import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model

    def fillDDanni(self):
        elementiDD= self.model.getAnni()
        for e in elementiDD:
            #chiamo l'elemnto della view, poi chiamo append e gli inserisco le cose col metodo
            self.view.ddanno.options.append(ft.dropdown.Option(key=e[0], text=f"{e[0]} {e[1]}"))

        self.view.update_page()

    def clickAvvistamenti(self,e):
        self.model.creaGrafo(self.view.ddanno.value)
        self.fillDDStati(self.model.grafo.nodes)



    def fillDDStati(self,stati):
        for e in stati:
            self.view.ddstato.options.append(ft.dropdown.Option(key=e, text=f"{e}"))

        self.view.update_page()

    def clickAnalizza(self,e):
        listaPred= self.model.precessori(self.view.ddstato.value)
        listaSucc= self.model.successivi(self.view.ddstato.value)
        self.view.txtAnalizza.controls.append(ft.Text(f"Stati Immediatamente precedenti: "))

        for i in listaPred:
               self.view.txtAnalizza.controls.append(ft.Text(f"{i}"))
        self.view.txtAnalizza.controls.append(ft.Text(f"Stati Immediatamente successivi: "))

        for e in listaSucc:
            self.view.txtAnalizza.controls.append(ft.Text(f"{e}"))

        self.view.update_page()

#        for i in LISTADASTAMPARE:
#           self.view.LISTWVIEW.controls.append(ft.Text(f"TESTOCHE VUOISCRIVERE/{i}"))
        #self.view.update_page()
        #NEL CONTROLLER