import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle('My Application')

        self.button = QPushButton('Click Me')

        self.button.setCheckable(True)

        # Butonun tıklama, kontrol değişimi, serbest bırakılma (released) durumları için ilgili slot fonksiyonlarına bağla
        # self.button.released.connect(self.button_released)
        # self.button.clicked.connect(self.button_clicked)
        self.button.toggled.connect(self.button_toggled)

        # Butonun kontrol durumunu başlangıçta ayarla
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def button_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def button_clicked(self):
        print("Button clicked!")

    def button_toggled(self, checked: bool):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()