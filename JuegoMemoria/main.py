# importamos las clases QApplication, QLabel y Qwidget # del modulo
#QTWidgets del paquete Pyside6
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from Ventana import Ventana


if __name__ == "__main__":
    # cada aplicación tendrá una sola instancia de QApplication
    app = QApplication([])
    # Creamos un objeto ventana
    ventana1 = Ventana()
    # Mostramos la ventana
    ventana1.show()
    # iniciamos el bucle de eventos
    app.exec()
