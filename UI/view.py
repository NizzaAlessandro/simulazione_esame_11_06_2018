import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):
        # title
        self._title = ft.Text("simulazione esame 24/01/2024", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1
        self.ddanno = ft.Dropdown(label="Anno")
        self.btnAvvistamenti = ft.ElevatedButton(text="Avvistamenti",on_click=self._controller.clickAvvistamenti)
        row1 = ft.Row([ft.Container(self.ddanno, width=300),
                       ft.Container(self.btnAvvistamenti, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        #row 2
        self.ddstato = ft.Dropdown(label="Stato")
        self.btnAnalizza = ft.ElevatedButton(text="Analizza",on_click=self._controller.clickAnalizza)
        self.btnSequenza = ft.ElevatedButton(text="Calcola sequenza")
        row2 = ft.Row([ft.Container(self.ddstato, width=300),
                       ft.Container(self.btnAnalizza, width=300),
                       ft.Container(self.btnSequenza, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self.txtGrafo = ft.ListView()
        self.txtAnalizza = ft.ListView(expand=1)
        self.txtSequenza = ft.ListView(expand=1)

        self._page.add(self.txtGrafo)
        self._page.add(self.txtAnalizza)
        self._page.add(self.txtSequenza)

        #non serve chiamarla perche chiamata in un altra funzione
        #self._controller.fillDDStati()
        self._controller.fillDDanni()
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
