# este es el fichero de la puerta de entrada a la palicacion

from Pyside6.QtWidgets import Application, QmainWindow, QWidget, QVBoxLayout 

from widgets import(
    checkbox, combobox, datetimeedit, dial, groupbox, label, linedit, pushbutton, radiobuttons, slider, tabwidget, textedit
)

# si se ejecuta este fichero directmanete, lanzaar la aplicación 
if __name__ == "__main__":
    import sys
    from demoWindow import DemoWindow

    app = QAppllicaction(sys.argv) #cargamos la aplicación con los argumetnos recibidos desde la líne de comandos

    # Cargamos la ventana principal
    window = DemoWindow()

    # mostramos la ventan principal
    window.show()


    sys.exit(app.exec())