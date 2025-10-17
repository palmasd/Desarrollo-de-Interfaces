from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QCheckBox
from PySide6.QtCore import Qt

def create( parent=None):
    box= QGroupBox("Mi label")
    layout = QVBoxLayout(box)

    label = QLabel("hola, este es mi Qlabel")
    label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
    
    info_label = QLabel("Señales: -Ninguna | Metodos: setTex(str), setAlignment(...)")
    info_label.setStyleSheet("color: gray; font-size: 10pt;")

    layout.addWidget(label)
    layout.addWidget(info_label)

    return box

