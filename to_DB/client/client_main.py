import sys
from socket import *
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox
from client_operation import ClientOp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_show = ClientOp()
    window_show.show()
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./font/Pretendard-Regular.ttf')
    app.setFont(QFont('Pretendard'))
    sys.exit(app.exec())
