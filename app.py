# pip install PyQt6
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton


# MainWindow sınıfı oluşturun.
class MainWindow(QMainWindow):
    # Constructor metodu oluşturun.
    def __init__(self):
        super().__init__()    # QMainWindow sınıfının constructor'ını çağır

        # Pencere başlığını ayarlayın
        self.setWindowTitle("My App")

        # Bir buton oluşturun ve bu butonun üzerindeki yazıyı ayarlayın
        button = QPushButton("Click Me")

        # Pencerenin minimum boyutunu ayarlayın (genişlik, yükseklik)
        self.setMinimumSize(QSize(100, 50))

        # Pencerenin maximum boyutunu ayarlayın
        self.setMaximumSize(QSize(900, 700))

        # Oluşturulan butonu pencerenin merkezi widget'ı olarak ayarla
        self.setCentralWidget(button)

# Uygulama için bir QApplication örneği oluşturun. sys.argv, komut satırı argümanlarını içerir
app = QApplication(sys.argv)

# Bir MainWindow örneği oluşturun.
window = MainWindow()

# Pencereyi görünür yap
window.show()

# Uygulamanın event loop'u başlat. Bu uygulamanın açık kalmasını sağlar
app.exec()