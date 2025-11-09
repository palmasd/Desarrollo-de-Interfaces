from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout,  QGridLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class PanelIzquierdo(QVBoxLayout):
    def __init__(self):
        super().__init__()

        layout_horizontal = QHBoxLayout()

        etiqueta = QLabel("<h1>El MEMORY</h1>")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addWidget(etiqueta)

        layout_cuadricual = QGridLayout()
        layout_cuadricual.setSpacing(10)
        layout_cuadricual.setContentsMargins(10, 10, 10, 10)

        cartas = [
            "img/spiderman.jpg", "img/dragonBall.jpg", "img/Fortnite.jpg", "img/borderlands3lanseres_2801823.jpg", "img/crash_bandicoot_.jpg", "img/GOW.jpg",
            "img/spiderman.jpg", "img/dragonBall.jpg", "img/Fortnite.jpg", "img/borderlands3lanseres_2801823.jpg", "img/crash_bandicoot_.jpg", "img/GOW.jpg"
            ]
        for indice, carta in enumerate(cartas):
            columna = indice % 4
            fila = indice // 4
            juego = QLabel()
            pixmap = QPixmap(carta)
            juego.setPixmap(pixmap)
            juego.setScaledContents(True)
            juego.setFixedSize(50, 50)        # Ajusta al tamaño que quieras
            layout_cuadricual.addWidget(juego, fila, columna)
        
        self.addLayout(layout_cuadricual)

        nivel = QLabel("Nivel: ")
        nivel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addWidget(nivel)
        layout_horizontal.addWidget(nivel)

        facil = QPushButton("Fácil")
        medio = QPushButton("Medio")
        dificil = QPushButton("Difícil")

        layout_horizontal.addWidget(facil)
        layout_horizontal.addWidget(medio)
        layout_horizontal.addWidget(dificil)

        self.addLayout(layout_horizontal)


