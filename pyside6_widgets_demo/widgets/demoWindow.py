'''
Ventan principal de la aplicación que compone todos los widgets disponibles desde mídulos separados. 
Cada módulo expone create(parent=None) que devuelve un QGroupBox y un diccionario (exposed_dict) de widgets
expuestos

'''
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import widgets.label as label


class DemoWindow(QMainWindow): # mi Clase DemoWindow hereca de QmainWindow

    def __init__(self):    #constructor de la clase DemoWindow

        self.main_layout: QVBoxLayout #
        self.refs: dict                #diccionario para almacenar referencias a widgets expuetos
        self.central_widget: QWidget   #declaracion de variable con anotacio de tipo => variable: tipo 


        super().__init__() #Llamada al constructor de la clase base QMainWindow


        # Configuramos el titulo de la ventana
        self.setWindowTitle("PySide6 Widgets Demo")

        # Le damos tamaño inicial a la ventan
        self.resize(800, 600)

        #Creamos el widget central de la ventana
        self.central_widget = QWidget(self)
        self.setCentralWidget(central_widget) # ejecutamos el metodo setCentralWidget heredado  de           QMainWindow. Este método recibe un Qwidget que se establece como widget central de la ventana.

        #definimos el layout del widget central 
        self.main_layout = QVBoxLayout(central_widget)

        self.refs = {} # inicializamos el diccionario desde los míduloes en el layout principal

        # ---Metodos de composición de la ventana principal (uno por widget)---

        #declaramos el método add_label que añade el widget label al layout principal 
        self.add_label(self)

        def add_label(self):
            box, exposed = label.create(self.central_widget)
            
            # Lo agregamos al layout principal
            self.main_layout.addWidget(box)

            # Guardamos referencias de widgets expuestos
            self.refs.update(exposed)