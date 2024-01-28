# Bir pencere oluşturun. Bir buton widget'ı ekleyin.
# Butona her tıklandığında butonun ismi bir listeden rastgele bir ifade ile değiştirilsin.
import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Application")

        self.button = QPushButton("Press Me")

        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        button_label = "You clicked the button"
        self.button.setText(button_label)

        self.button.setEnabled(False)

        self.setWindowTitle("My OneShot Application")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()