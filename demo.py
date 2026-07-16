import sys
import platform
from PyQt6.QtWidgets import QApplication
from SamplePopupWnd import SamplePopupWnd

mainwnd = None


def main():
    global mainwnd
    if platform.system() != "Darwin":
        print("This program requires macOS.")
        sys.exit(1)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    mainwnd = SamplePopupWnd()

    sys.exit(app.exec())


main()
