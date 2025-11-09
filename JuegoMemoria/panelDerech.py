# panel_derecho.py
from PySide6.QtWidgets import QVBoxLayout, QLabel, QSpinBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class PanelDerecho(QVBoxLayout):
    def __init__(self):
        super().__init__()

        intentos = QLabel("Intentos")
        intentos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addWidget(intentos)

        numero_vidas = QSpinBox()
        numero_vidas.setRange(0, 3)
        numero_vidas.setValue(3)
        numero_vidas.setReadOnly(True)
        self.addWidget(numero_vidas)

        imagen_vidas = ["img/spiderman.jpg", "img/dragonBall.jpg", "img/Fortnite.jpg"]
        for img_path in imagen_vidas:
            vidas = QLabel()
            pixmap = QPixmap(img_path)
            vidas.setPixmap(pixmap)
            vidas.setScaledContents(True)
            vidas.setFixedSize(75, 75)
            self.addWidget(vidas)
