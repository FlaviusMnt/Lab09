import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "LAB09"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txtIn = None
        self._btnAnalizza = None
        self._txtResult = None

    def load_interface(self):
        # title
        self._title = ft.Text("Flights Manager", color="blue", size=24)
        self._page.controls.append(self._title)

        #RIGA 1
        self._txtIn = ft.TextField(label = "DISTANZA MINIMA")
        self._btnAnalizza = ft.ElevatedButton(text="Analizza Aeroporti",
                                              on_click=self._controller.handleAnalizza)

        row1 = ft.Row([self._txtIn, self._btnAnalizza],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #TXT RESULT

        self._txtResult = ft.ListView(expand=1, spacing=10, padding=10, auto_scroll=False)
        self._txtResult.controls.append(ft.Text("AGGIUNGI IL TUO OUTPUT QUI!"))
        self._page.controls.append(self._txtResult)

        #FINALE
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
