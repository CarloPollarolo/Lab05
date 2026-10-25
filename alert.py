import flet as ft

class AlertManager:
    def __init__(self, page: ft.Page):
        self._page = page
        self._alert_dialog = ft.AlertDialog( #creazione oggetto finestra di dialogo
            title=ft.Text(""),
            actions=[ft.TextButton("OK", on_click=self.close)] #richiamo del metodo self.close per chiudere la finestra
        )

    def show_alert(self, message: str):
        self._alert_dialog.title.value = message #aggiorno il meesaggio da "" a un messaggio di errore
        if self._alert_dialog not in self._page.overlay:
            self._page.overlay.append(self._alert_dialog)
        self._alert_dialog.open = True #impostato valore della finestra di dialogo su aperto(open=True)
        self._page.update()
        #l'overlay è lo strato trasparente con il messaggio di allerta che sta sopra alla page

    def close(self, e):
        self._alert_dialog.open = False #cambia lo stato della finestra in chiusa(open=False), si attiva quando clicchi il TextButton
        self._page.update() #si aggiorna l'interfaccia per far scomaprire la finestra di dialogo e
                             #rendere visualizzabile la page prima coperta

#self._alert_dialog.title.value: prima accedo alla proprietà Title dell 'attributo self._alert_dialog e poi
#al suo valore, quindi alla stringa messa come argomento del ft.Txt che Title rappresenta