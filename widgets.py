import sys

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QWidget, QApplication, QDateTimeEdit, \
    QDateEdit, QLineEdit, QDial, QDoubleSpinBox, QFontComboBox, QHBoxLayout, QLCDNumber, QLabel, QProgressBar, \
    QPushButton, QTimeEdit, QRadioButton, QSlider, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Widgets App')

        # Dikey düzenleyici (layout) oluştur
        layout = QVBoxLayout()

        widgets = [
            QCheckBox,     # A box hat can be checked or unchecked
            QComboBox,     # A dropdown list that lets you to choose one of several options
            QDateEdit,     # A widget edits dates
            QDateTimeEdit, # A widget edits dates with time
            QDial,         # A circular dial like a knob
            QDoubleSpinBox,# A box for number input with decimal points
            QFontComboBox, # A dropdown list to select font styles
            QLCDNumber,    # A display widget to show numbers in LCD-like style
            QLabel,        # A text or image display
            QLineEdit,     # A one-line text field for input
            QProgressBar,  # A bar that shows progress of a task
            QPushButton,   # A button that can be clicked
            QRadioButton,  # A button used for making selections, often within a group
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for widget in widgets:
            layout.addWidget(widget())

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()