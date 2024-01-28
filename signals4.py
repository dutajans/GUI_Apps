# Bir pencere oluşturun. Bir buton widget'ı ekleyin.
# Butona her tıklandığında butonun ismi bir listeden rastgele bir ifade ile değiştirilsin.
import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        self.label = QLabel()

        self.input = QLineEdit()

        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()

        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()