import sys

from core.app import HuffmanApp

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HuffmanApp()
    window.show()
    sys.exit(app.exec())
