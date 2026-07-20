from PySide6.QtWidgets import QMainWindow

class SampleMainWnd(QMainWindow):
    def __init__(self, /):
        super().__init__()
        self.setWindowTitle("SampleMainWnd")
        self.setGeometry(64, 128, 200, 48)