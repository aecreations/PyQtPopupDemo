from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

class SampleMainWnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SampleMainWnd")
        self.setGeometry(64, 128, 200, 48)

        # Make this dummy window invisible.
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
