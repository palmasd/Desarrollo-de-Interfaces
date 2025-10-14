from PySide6.QtWidgets import QApplication, QLabel, QWidget


class Ventana(QWidget):
    # constructor de la clase Window
    def __init__(self):
        # llamada al constructor de la superclase
        super().__init__()

        # Asignamos el título de la ventana
        self.setWindowTitle("Mi primera ventana")
        # Creamos una etiqueta con la ventana como elemento principal
        self.etiqueta = QLabel("Hola Mundo", self)
