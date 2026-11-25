import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
        valore = self._view.importo_medio_minimo.value
        if valore is None or valore.strip() == "":
            self._view.show_alert("Inserire un valore numerico come soglia.")
            return
        try:
            soglia = float(valore.strip())
        except ValueError:
            self._view.show_alert("Valore non valido: inserire un numero.")
            return
        if soglia < 0:
            self._view.show_alert("Inserire un importo maggiore o uguale a zero.")
            return
        self._model.costruisci_grafo(soglia)
        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()
        edges = self._model.get_all_edges()
        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Filiali: {num_nodi}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Collegamenti: {num_archi}")
        )
        for i, (u, v, attr) in enumerate(edges, start=1):
            peso = attr["weight"]
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"{i}) [{u} -> {v}] -- Importo medio per bonifico: € {peso:.2f}")
            )
        self._view.update()
