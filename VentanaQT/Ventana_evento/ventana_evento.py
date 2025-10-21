from PySide6.QtWidgets import QApplication, QLabel, QWidget


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.mensaje_cambiado = False #controla si el mensaje ha cmabiado 

        self.setWindowTitle("Mi primera ventana")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Haz clic cualquier parte de la ventana", self)
        self.label.move(50, 130)

        #self.label.actionEvent = self.cambiar_mensaje

        def mousePressEvent(self, event):
            if not self.mensaje_cambiado:
                self.label.setText("Has hecho clic en la ventana!")
                self.mensaje_cambiado = True
            else:
                self.label.setText("Haz clic de vuelta")
                self.mensaje_cambiado = False


        self.show