# Projekt: Piłka
# Autor: Oliwier Chudzicki
# Data: 29.05.2024 r.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class OknoGry(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Projekt pilka - poziom 1') # Ustawia tytuł okna
        self.resize(750, 500)   # Ustawia początkowy rozmiar okna
        self.setMinimumSize(650, 400)  # Ustawia minimalny rozmiar okna

        self.poziom = [ # Definiuje tablicę z elementami poziomu
            [0, 2, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 2, 3, 3, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 2, 2, 2, 1],
            [2, 2, 2, 2, 2, 2, 2, 3, 2, 0]
        ]

        self.uklad_poziomu = QGridLayout()  # Tworzy układ siatki dla poziomu gry
        self.uklad_poziomu.setContentsMargins(10, 10, 10, 10)  # Ustawia marginesy ukladu
        self.uklad_poziomu.setSpacing(0)  # Ustawia odstęp między widgetami
        self.stworz_widgety_poziomu()   # Wywołuje metodę tworzącą widgety poziomu

        main_layout = QVBoxLayout()     # Tworzy główny układ pionowy
        main_layout.addLayout(self.uklad_poziomu)   # Dodaje układ poziomu do głównego układu
        main_layout.setContentsMargins(10, 10, 10, 10)  # Ustawia marginesy dla głównego układu

        self.setLayout(main_layout) # Ustawia główny układ jako układ okna

    def stworz_widgety_poziomu(self):
        # Tworzy widgety poziomu na podstawie tablicy self.poziom
        for i, row in enumerate(self.poziom):
            # Zwraca zarówno i i wartość row dla każdego wiersza w self.poziom
            for j, cell in enumerate(row):
                if cell == 0:       # Jeśli komórka ma wartość 0, to tworzy piłkę lub bramke
                    widget = QLabel('⚽️', self) if (i == 0 and j == 0) else QLabel('🥅', self) # Dla pierwszego 0 ustawia piłkę, dla innego bramkę
                elif cell == 1:     # Jeśli komórka ma wartość 1, to tworzy ścieżkę
                    widget = QLabel('🟫', self)
                elif cell == 2:     # Jeśli komórka ma wartość 2, to tworzy pobocze
                    widget = QLabel('🪨', self)
                elif cell == 3:     # Jeśli komórka ma wartość 1, to tworzy trawę
                    widget = QLabel('🌿', self)
                widget.setAlignment(Qt.AlignCenter) # Ustawia wyrównanie do środka
                self.uklad_poziomu.addWidget(widget, i, j)  # Dodaje każdego kolejnego labela do układu siatki na pozycji (i, j)

# Drugie okno do sterowania piłką
class OknoSterowania(QWidget):
    def __init__(self, okno_gry):
        super().__init__()
        self.okno_gry = okno_gry # Przekazuje referencję, aby móc sterować piłką

        self.setWindowTitle('Sterowanie piłką') # Ustawia tytuł drugiego okna
        self.resize(200, 100) # Zmienia początkową wielkość drugiego okna

        # Tworzy przyciski sterowania
        self.przycisk_gora = QPushButton('⬆️', self)
        self.przycisk_dol = QPushButton('⬇️', self)
        self.przycisk_lewo = QPushButton('⬅️', self)
        self.przycisk_prawo = QPushButton('➡️', self)

        # Łączy przyciski z metodami obsługującymi ruch piłki
        self.przycisk_gora.clicked.connect(self.ruch_gora)
        self.przycisk_dol.clicked.connect(self.ruch_dol)
        self.przycisk_lewo.clicked.connect(self.ruch_lewo)
        self.przycisk_prawo.clicked.connect(self.ruch_prawo)

        layout = QGridLayout()  # Tworzy układ siatki dla przycisków
        layout.addWidget(self.przycisk_gora, 0, 1)
        layout.addWidget(self.przycisk_lewo, 1, 0)
        layout.addWidget(self.przycisk_dol, 1, 1)
        layout.addWidget(self.przycisk_prawo, 1, 2)

        self.setLayout(layout)  # Ustawia układ siatki jako układ drugiego okna

    def ruch_gora(self):
        # Implementacja ruchu piłki w górę
        pass

    def ruch_dol(self):
        # Implementacja ruchu piłki w dół
        pass

    def ruch_lewo(self):
        # Implementacja ruchu piłki w lewo
        pass

    def ruch_prawo(self):
        # Implementacja ruchu piłki w prawo
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gra = OknoGry()
    gra.show()

    sterowanie = OknoSterowania(gra)
    sterowanie.show()

    sys.exit(app.exec_())
