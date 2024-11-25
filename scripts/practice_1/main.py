import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from main_window import MainWindow


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()