# Projekt: Piłka
# Autor: Oliwier Chudzicki
# Data: 29.05.2024 r.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout
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
            # zwraca zarówno i i wartość row dla każdego wiersza w self.poziom
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = OknoGry()
    okno.show()
    sys.exit(app.exec_())
