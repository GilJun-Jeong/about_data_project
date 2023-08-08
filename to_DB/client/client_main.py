import sys
from socket import *
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox
from client_operation import ClientOp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./font/subway.ttf')
    app.setFont(QFont('subway'))
    window_show = ClientOp()
    window_show.exec()
    sys.exit(app.exec())
