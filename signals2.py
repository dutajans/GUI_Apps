# Bir pencere oluşturun. Bir buton widget'ı ekleyin.
# Butona her tıklandığında butonun ismi bir listeden rastgele bir ifade ile değiştirilsin.
import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication

from random import choice

button_labels = [
    "Ankara",
    "İstanbul",
    "İzmir",
    "Samsun"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Application")

        self.button = QPushButton("Press Me")

        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        button_label = choice(button_labels)
        self.button.setText(button_label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()