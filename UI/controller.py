import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        threshold = self._view._txtIn.value

        try:
            float(threshold)
        except ValueError:
            self._view._txtResult.controls.clear()
            self._view._txtResult.controls.append(ft.Text("AGGIUNGI IL TUO OUTPUT"))
            self._view.update_page()
            return

        self._model.buildGraph(float(threshold))
        self._view._txtResult.controls.clear()
        self._view._txtResult.controls.append(ft.Text("GRAFICO CREATO"))
        self._view._txtResult.controls.append(ft.Text("Num of nodes:" + str(self._model.getNumNodes())))
        self._view._txtResult.controls.append(ft.Text("Num of nodes:" + str(self._model.getNumEdges())))
        allEdges = self._model.getAllEdges()
        for edge in allEdges:
            self._view._txtResult.controls.append(
                ft.Text(f"\"\nA1: {edge[0]} \nA2: ->{edge[1]} \nAvgDist: {self._model.getAvgDist(edge[0], edge[1])}\n"))

        self._view.update_page()
