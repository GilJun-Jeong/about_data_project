import sys
from socket import *
import threading
import ui.mainUi
import json
import time
from temp_data import Temp
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMainWindow


class ClientOp(QMainWindow, ui.mainUi.Ui_MainWindow, Temp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connection()
        self.init_signal()

    def init_signal(self):
        self.pb_start.clicked.connect(self.start)
        self.lb_next.mousePressEvent = self.next_page
        self.lb_previous.mousePressEvent = self.previous_page
        self.pb_all.clicked.connect(self.all_page)
        self.pb_money.clicked.connect(self.money_page)
        self.pb_location.clicked.connect(self.location_page)
        self.pb_show_data.clicked.connect(self.show_result_data)
        self.pb_show_map.clicked.connect(self.show_result_map)
        self.pb_start_page.clicked.connect(self.start_page)
        self.pb_data_scan_button.clicked.connect(self.data_scan)
        self.pb_scan_all.clicked.connect(self.analysis_all)
        self.pb_scan_money.clicked.connect(self.analysis_money)
        self.pb_scan_location.clicked.connect(self.analysis_location)
        self.pb_result_realestate.clicked.connect(self.analysis_real_estate)
        self.pb_return.clicked.connect(self.return_previous)


    def connection(self):
        server_ip = '10.10.20.101'
        server_port = 9999

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        try:
            self.client_socket.connect((server_ip, server_port))
            self.listening_thread = threading.Thread(target=self.check_server_response, daemon=True)
            self.listening_thread.start()
            self.connected = True
            self.information['socket'] = [self.client_socket]
            self.information['connect'] = [True]
        except:
            self.connected = False
            print('해제')

    def closeEvent(self, e):
        self.close()
        self._send_packet(f'disconnect{self.header_split}')

    def _send_packet(self, p):
        packet_length = 1024
        if self._connected:
            if len(p.encode()) < packet_length:
                filled_packet = p.ljust(packet_length)
            else:
                filled_packet = p[:packet_length]
            self.client_socket.send(filled_packet.encode('UTF-8'))
        else:
            pass

    def check_server_response(self):
        while self.connected:
            try:
                response = self.client_socket.recv(int(self.file_size))
                self._parse_packet(response)

            except Exception as e:
                pass

    def _parse_packet(self, p):

        packet = p.decode('UTF-8').strip()
        parsed = packet.split(self.header_split)
        command = parsed[0].strip()
        try:
            if command == 'size':
                self.file_size = packet.split(self.header_split)[1].strip()

            elif command == 'disconnect':
                self.client_socket.close()
                self.client_socket = None
                self.information['connect'] = False

            elif command == 'error':
                pass
            elif command == 'update':
                self.classcenterframe.theSignal.emit(' '.join(parsed[1:]).strip(), False)
        except:
            self.file_receive(p)

    def file_receive(self, byte):
        path = './temp_img/' + self.name
        with open(path,'wb') as file:
            try:
                file.write(byte)
                file.close()
                self.file_size = 1024
            except Exception as e:
                print(e)

    def start(self):
        self.sw_main.setCurrentWidget(self.pg_data_page)
        self.sw_logo.setCurrentWidget(self.pg_logo_menu)

    def next_page(self, event):
        self.sw_main.setCurrentWidget(self.pg_analysis_page)

    def previous_page(self, event):
        self.sw_main.setCurrentWidget(self.pg_data_page)

    def all_page(self):
        self.sw_scan.setCurrentWidget(self.pg_all)

    def money_page(self):
        self.sw_scan.setCurrentWidget(self.pg_money)

    def location_page(self):
        self.sw_scan.setCurrentWidget(self.pg_location)

    def show_result_data(self):
        self.sw_analysis_result.setCurrentWidget(self.pg_result_data)
        self.pb_show_data.setEnabled(False)
        self.pb_show_map.setEnabled(True)

    def show_result_map(self):
        self.sw_analysis_result.setCurrentWidget(self.pg_result_map)
        self.pb_show_map.setEnabled(False)
        self.pb_show_data.setEnabled(True)

    def data_scan(self):
        district = self.cb_district_data.currentText()
        local = self.cb_local_data.currentText()
        data_type = self.cb_data_type.currentText()

    def analysis_all(self):
        district = self.cb_district_all.currentText()
        local = self.cb_local_all.currentText()
        self.sw_condition.setCurrentWidget(self.pg_realestate)

    def analysis_money(self):
        money = self.le_money.text()
        district = self.cb_district_money.currentText()
        local = self.cb_local_money.currentText()
        self.sw_condition.setCurrentWidget(self.pg_realestate)

    def analysis_location(self):
        location = self.le_location.text()
        self.sw_result.setCurrentWidget(self.pg_result)

    def analysis_real_estate(self):
        self.sw_result.setCurrentWidget(self.pg_result)

    def return_previous(self):
        self.sw_result.setCurrentWidget(self.pg_main_scan)
        self.sw_condition.setCurrentWidget(self.pg_scan)
        self.sw_scan.setCurrentWidget(self.pg_all)

    def start_page(self):
        self.sw_main.setCurrentWidget(self.pg_open_page)
        self.sw_logo.setCurrentWidget(self.pg_logo_open)
        self.sw_result.setCurrentWidget(self.pg_main_scan)
        self.sw_condition.setCurrentWidget(self.pg_scan)
        self.sw_scan.setCurrentWidget(self.pg_all)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = ClientOp()
    myWindow.show()
    app.exec()
