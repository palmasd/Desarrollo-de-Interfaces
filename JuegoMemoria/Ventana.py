from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow,QSpinBox, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import *
from panelIzq import PanelIzquierdo
from panelDerech import PanelDerecho



class Ventana(QMainWindow):
        def __init__(self):

            # constructor de la clase Window
            # llamada al constructor de la superclase
            super().__init__()
            # establecemos el título de la ventana
            self.setGeometry(400, 400, 800, 600)
            self.setWindowTitle("Juego de la memoria")
            
            #Crear widget central y layout
            widgetCentral = QWidget()
            layout_Principal = QHBoxLayout()

            #llamamos a las clase donde estan cada uno con su panel
            Panel_izq = PanelIzquierdo()
            Panel_derech = PanelDerecho()
    
            #layout principales en horizontal donde vamos ir agregando los elementos de los demas
            layout_Principal.addLayout(Panel_izq)
            layout_Principal.addLayout(Panel_derech)

            layout_Principal.setStretch(0, 1)
            layout_Principal.setStretch(1, 1)


            widgetCentral.setLayout(layout_Principal)

            self.setCentralWidget(widgetCentral)
            
