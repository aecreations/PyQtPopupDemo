import sys
from PySide6.QtWidgets import QApplication
from SamplePopupWnd import SamplePopupWnd

mainwnd = None


def main():
    global mainwnd

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    mainwnd = SamplePopupWnd()

    sys.exit(app.exec())


main()
