# Projekt: Piłka
# Autor: Oliwier Chudzicki
# Data: 30.05.2024 r.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class OknoGry(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Projekt pilka - poziom 1')  # Ustawia tytuł okna
        self.resize(750, 500)  # Ustawia początkowy rozmiar okna
        self.setMinimumSize(650, 400)  # Ustawia minimalny rozmiar okna

        # Definiuje tablicę z elementami poziomu
        self.poziom = [
            ['P', 2, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 2, 3, 3, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 2, 2, 2, 1],
            [2, 2, 2, 2, 2, 2, 2, 3, 2, 'B']
        ]

        # Pobiera startową pozycję piłki z tablicy poziomu
        self.pilka_startowa_pozycja = self.znajdz_pilke()
        self.pilka_pozycja = self.pilka_startowa_pozycja  # Ustawia aktualną pozycję piłki na startową

        self.uklad_poziomu = QGridLayout()  # Tworzy układ siatki dla poziomu gry
        self.uklad_poziomu.setContentsMargins(10, 10, 10, 10)  # Ustawia marginesy ukladu
        self.uklad_poziomu.setSpacing(0)  # Ustawia odstęp między widgetami
        self.stworz_widgety_poziomu()  # Wywołuje metodę tworzącą widgety poziomu

        main_layout = QVBoxLayout()  # Tworzy główny układ pionowy
        main_layout.addLayout(self.uklad_poziomu)  # Dodaje układ poziomu do głównego układu
        main_layout.setContentsMargins(10, 10, 10, 10)  # Ustawia marginesy dla głównego układu

        self.setLayout(main_layout)  # Ustawia główny układ jako układ okna

    def znajdz_pilke(self):
        # Znajduje pozycję startową piłki 'P' w tablicy poziomu
        for i, wiersz in enumerate(self.poziom):
            for j, komorka in enumerate(wiersz):
                if komorka == 'P':
                    return (i, j)
        return (0, 0)  # Domyślna wartość, jeśli piłka nie zostanie znaleziona

    def stworz_widgety_poziomu(self):
        # Tworzy widgety poziomu na podstawie tablicy self.poziom
        for i, wiersz in enumerate(self.poziom):
            for j, komorka in enumerate(wiersz):
                if komorka == 'P':  # Jeśli komórka ma wartość 'P', to tworzy piłkę
                    widget = QLabel('⚽️', self)
                elif komorka == 'B':  # Jeśli komórka ma wartość 'B', to tworzy bramkę
                    widget = QLabel('🥅', self)
                elif komorka == 1:  # Jeśli komórka ma wartość 1, to tworzy ścieżkę
                    widget = QLabel('🟫', self)
                elif komorka == 2:  # Jeśli komórka ma wartość 2, to tworzy pobocze
                    widget = QLabel('🪨', self)
                elif komorka == 3:  # Jeśli komórka ma wartość 3, to tworzy trawę
                    widget = QLabel('🌿', self)
                widget.setAlignment(Qt.AlignCenter) # Ustawia wyrównanie do środka
                self.uklad_poziomu.addWidget(widget, i, j) # Dodaje widget do układu siatki na pozycji (i, j)

    def ruch_pilki(self, nowa_pozycja):
        stara_pozycja = self.pilka_pozycja
        i, j = nowa_pozycja

        if i < 0 or i >= len(self.poziom) or j < 0 or j >= len(self.poziom[0]) or self.poziom[i][j] == 2:
            print(f"Piłka weszła na krawędź na pozycji ({stara_pozycja[1]}, {stara_pozycja[0]}), powrót na start")
            self.poziom[stara_pozycja[0]][stara_pozycja[1]] = 1  # Ustawienie ścieżki w starej pozycji
            self.pilka_pozycja = self.pilka_startowa_pozycja  # Powrót na start
            self.poziom[self.pilka_startowa_pozycja[0]][self.pilka_startowa_pozycja[1]] = 'P'
            self.odswiez_uklad()
        elif self.poziom[i][j] == 'B':
            print(f"Piłka weszła do bramki na pozycji ({j}, {i})")
            self.poziom[stara_pozycja[0]][stara_pozycja[1]] = 1  # Ustawienie ścieżki w starej pozycji
            self.poziom[i][j] = 'P'  # Ustawienie piłki w nowej pozycji
            self.pilka_pozycja = (i, j)
            self.odswiez_uklad()
            self.wyswietl_wiadomosc_wygranej()
        else:
            print(f"Ruch piłki na pozycję ({j}, {i})")
            self.poziom[stara_pozycja[0]][stara_pozycja[1]] = 1  # Ustawienie ścieżki w starej pozycji
            self.poziom[i][j] = 'P'  # Ustawienie piłki w nowej pozycji
            self.pilka_pozycja = (i, j)
            self.odswiez_uklad()

    def odswiez_uklad(self):
        # Usuwa wszystkie widgety z aktualnego układu
        for i in range(self.uklad_poziomu.rowCount()):
            for j in range(self.uklad_poziomu.columnCount()):
                widget = self.uklad_poziomu.itemAtPosition(i, j).widget()
                if widget:
                    self.uklad_poziomu.removeWidget(widget)
                    widget.deleteLater()
        # Tworzy nowe widgety na podstawie bieżącej konfiguracji planszy
        self.stworz_widgety_poziomu()

    def wyswietl_wiadomosc_wygranej(self):
        msg_box = QMessageBox() # Tworzy okno komunikatu
        msg_box.setWindowTitle("Wygrana!")
        msg_box.setText("Gratulacje! Ukończyłeś poziom.")
        msg_box.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)   # Dodaje przyciski "Od nowa" i "Zamknij"
        next_level_button = msg_box.addButton("Następny poziom", QMessageBox.AcceptRole)    # Dodaje przycisk "Następny poziom"
        next_level_button.setDisabled(True)
        next_level_button.setToolTip("Kiedyś")
        # Zmienia etykiety przycisków "Od nowa" i "Zamknij"
        msg_box.button(QMessageBox.Retry).setText("Od nowa")
        msg_box.button(QMessageBox.Close).setText("Zamknij")
        result = msg_box.exec_()    # Wyświetla okno komunikatu i oczekuje na jego zamknięcie

        # Jeśli użytkownik wybrał "Od nowa", resetuje poziom
        if result == QMessageBox.Retry:
            self.reset_poziom()
        # Jeśli użytkownik wybrał "Zamknij", zamyka aplikację
        elif result == QMessageBox.Close:
            QApplication.instance().quit()

    def reset_poziom(self):
        self.poziom = [  # Resetuje tablicę z elementami poziomu
            ['P', 2, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 2, 3, 3, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 2, 2, 2, 1],
            [2, 2, 2, 2, 2, 2, 2, 3, 2, 'B']
        ]
        self.pilka_pozycja = self.pilka_startowa_pozycja  # Resetuje pozycję piłki
        self.odswiez_uklad()

class OknoSterowania(QWidget):
    def __init__(self, okno_gry):
        super().__init__()
        self.okno_gry = okno_gry  # Przekazuje referencję, aby móc sterować piłką

        self.setWindowTitle('Sterowanie piłką')  # Ustawia tytuł drugiego okna
        self.resize(200, 100)  # Zmienia początkową wielkość drugiego okna

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
        x, y = self.okno_gry.pilka_pozycja
        self.okno_gry.ruch_pilki((x - 1, y))

    def ruch_dol(self):
        x, y = self.okno_gry.pilka_pozycja
        self.okno_gry.ruch_pilki((x + 1, y))

    def ruch_lewo(self):
        x, y = self.okno_gry.pilka_pozycja
        self.okno_gry.ruch_pilki((x, y - 1))

    def ruch_prawo(self):
        x, y = self.okno_gry.pilka_pozycja
        self.okno_gry.ruch_pilki((x, y + 1))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gra = OknoGry()
    gra.show()

    sterowanie = OknoSterowania(gra)
    sterowanie.show()

    sys.exit(app.exec_())
