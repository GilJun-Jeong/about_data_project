# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sw_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.sw_main.setGeometry(QtCore.QRect(0, 100, 800, 500))
        self.sw_main.setObjectName("sw_main")
        self.pg_data_page = QtWidgets.QWidget()
        self.pg_data_page.setObjectName("pg_data_page")
        self.widget_3 = QtWidgets.QWidget(self.pg_data_page)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget_3.setObjectName("widget_3")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget_5.setStyleSheet("background-color : #009223")
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.widget_6.setStyleSheet("background-color : #ffce32;")
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setGeometry(QtCore.QRect(300, 35, 200, 40))
        self.widget_7.setStyleSheet("background-color : #ffce32")
        self.widget_7.setObjectName("widget_7")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setGeometry(QtCore.QRect(0, 5, 200, 30))
        self.label_5.setStyleSheet("background-color : #009223;\n"
"color : #ffce32;\n"
"font-size : 12;\n"
"font-weight : bold;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.wg_data_map = QtWebEngineWidgets.QWebEngineView(self.widget_5)
        self.wg_data_map.setGeometry(QtCore.QRect(10, 90, 400, 400))
        self.wg_data_map.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wg_data_map.setObjectName("wg_data_map")
        self.widget_9 = QtWidgets.QWidget(self.widget_5)
        self.widget_9.setGeometry(QtCore.QRect(450, 90, 340, 400))
        self.widget_9.setObjectName("widget_9")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setGeometry(QtCore.QRect(0, 0, 340, 50))
        self.widget_10.setObjectName("widget_10")
        self.cb_district_data = QtWidgets.QComboBox(self.widget_10)
        self.cb_district_data.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self.cb_district_data.setStyleSheet("background-color : white;")
        self.cb_district_data.setFrame(True)
        self.cb_district_data.setObjectName("cb_district_data")
        self.cb_local_data = QtWidgets.QComboBox(self.widget_10)
        self.cb_local_data.setGeometry(QtCore.QRect(90, 10, 70, 30))
        self.cb_local_data.setStyleSheet("background-color : white;")
        self.cb_local_data.setObjectName("cb_local_data")
        self.cb_data_type = QtWidgets.QComboBox(self.widget_10)
        self.cb_data_type.setGeometry(QtCore.QRect(170, 10, 70, 30))
        self.cb_data_type.setStyleSheet("background-color : white;")
        self.cb_data_type.setObjectName("cb_data_type")
        self.pb_data_scan_button = QtWidgets.QPushButton(self.widget_10)
        self.pb_data_scan_button.setGeometry(QtCore.QRect(260, 10, 60, 30))
        self.pb_data_scan_button.setStyleSheet("QPushButton{\n"
"background-color : #ffce32;\n"
"color : #009223;\n"
"font : 12px;\n"
"font-weight : bold;\n"
"border : 0px, solid;\n"
"border-radius : 10%;\n"
"}")
        self.pb_data_scan_button.setObjectName("pb_data_scan_button")
        self.li_data = QtWidgets.QListWidget(self.widget_9)
        self.li_data.setGeometry(QtCore.QRect(10, 60, 320, 330))
        self.li_data.setStyleSheet("background-color : white;\n"
"")
        self.li_data.setObjectName("li_data")
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        self.label_16.setGeometry(QtCore.QRect(130, 190, 81, 31))
        self.label_16.setObjectName("label_16")
        self.lb_next = QtWidgets.QLabel(self.widget_5)
        self.lb_next.setGeometry(QtCore.QRect(740, 30, 50, 50))
        self.lb_next.setText("")
        self.lb_next.setPixmap(QtGui.QPixmap("./img/right.png"))
        self.lb_next.setScaledContents(True)
        self.lb_next.setObjectName("lb_next")
        self.sw_main.addWidget(self.pg_data_page)
        self.pg_analysis_page = QtWidgets.QWidget()
        self.pg_analysis_page.setObjectName("pg_analysis_page")
        self.widget_11 = QtWidgets.QWidget(self.pg_analysis_page)
        self.widget_11.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget_11.setStyleSheet("background-color : #009223")
        self.widget_11.setObjectName("widget_11")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        self.widget_12.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.widget_12.setStyleSheet("background-color : #ffce32;")
        self.widget_12.setObjectName("widget_12")
        self.sw_result = QtWidgets.QStackedWidget(self.widget_11)
        self.sw_result.setGeometry(QtCore.QRect(10, 90, 780, 400))
        self.sw_result.setObjectName("sw_result")
        self.pg_main_scan = QtWidgets.QWidget()
        self.pg_main_scan.setObjectName("pg_main_scan")
        self.widget_14 = QtWidgets.QWidget(self.pg_main_scan)
        self.widget_14.setGeometry(QtCore.QRect(20, 30, 740, 360))
        self.widget_14.setStyleSheet("")
        self.widget_14.setObjectName("widget_14")
        self.sw_condition = QtWidgets.QStackedWidget(self.widget_14)
        self.sw_condition.setGeometry(QtCore.QRect(0, 0, 740, 360))
        self.sw_condition.setObjectName("sw_condition")
        self.pg_scan = QtWidgets.QWidget()
        self.pg_scan.setObjectName("pg_scan")
        self.widget_16 = QtWidgets.QWidget(self.pg_scan)
        self.widget_16.setGeometry(QtCore.QRect(0, 0, 360, 340))
        self.widget_16.setStyleSheet("background-color : #ffce32")
        self.widget_16.setObjectName("widget_16")
        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        self.widget_17.setGeometry(QtCore.QRect(0, 10, 360, 320))
        self.widget_17.setStyleSheet("background-color : #009223")
        self.widget_17.setObjectName("widget_17")
        self.pb_all = QtWidgets.QPushButton(self.widget_17)
        self.pb_all.setGeometry(QtCore.QRect(30, 30, 300, 50))
        self.pb_all.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_all.setObjectName("pb_all")
        self.pb_money = QtWidgets.QPushButton(self.widget_17)
        self.pb_money.setGeometry(QtCore.QRect(30, 130, 300, 50))
        self.pb_money.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_money.setObjectName("pb_money")
        self.pb_location = QtWidgets.QPushButton(self.widget_17)
        self.pb_location.setGeometry(QtCore.QRect(30, 230, 300, 50))
        self.pb_location.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_location.setObjectName("pb_location")
        self.sw_scan = QtWidgets.QStackedWidget(self.pg_scan)
        self.sw_scan.setGeometry(QtCore.QRect(370, 20, 360, 300))
        self.sw_scan.setObjectName("sw_scan")
        self.pg_all = QtWidgets.QWidget()
        self.pg_all.setObjectName("pg_all")
        self.cb_district_all = QtWidgets.QComboBox(self.pg_all)
        self.cb_district_all.setGeometry(QtCore.QRect(50, 80, 200, 30))
        self.cb_district_all.setStyleSheet("background-color : white\n"
"")
        self.cb_district_all.setObjectName("cb_district_all")
        self.cb_local_all = QtWidgets.QComboBox(self.pg_all)
        self.cb_local_all.setGeometry(QtCore.QRect(50, 140, 200, 30))
        self.cb_local_all.setStyleSheet("background-color : white\n"
"")
        self.cb_local_all.setObjectName("cb_local_all")
        self.pb_scan_all = QtWidgets.QPushButton(self.pg_all)
        self.pb_scan_all.setGeometry(QtCore.QRect(50, 200, 200, 30))
        self.pb_scan_all.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_scan_all.setObjectName("pb_scan_all")
        self.label_13 = QtWidgets.QLabel(self.pg_all)
        self.label_13.setGeometry(QtCore.QRect(50, 40, 200, 30))
        self.label_13.setStyleSheet("color : #ffce32;\n"
"font-weight : bold;\n"
"\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_19 = QtWidgets.QLabel(self.pg_all)
        self.label_19.setGeometry(QtCore.QRect(270, 160, 70, 70))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("./img/cado.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.sw_scan.addWidget(self.pg_all)
        self.pg_money = QtWidgets.QWidget()
        self.pg_money.setObjectName("pg_money")
        self.le_money = QtWidgets.QLineEdit(self.pg_money)
        self.le_money.setGeometry(QtCore.QRect(50, 70, 200, 30))
        self.le_money.setStyleSheet("background-color : white;")
        self.le_money.setObjectName("le_money")
        self.label_11 = QtWidgets.QLabel(self.pg_money)
        self.label_11.setGeometry(QtCore.QRect(50, 30, 200, 30))
        self.label_11.setStyleSheet("color : #ffce32;\n"
"font-weight : bold;\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.cb_district_money = QtWidgets.QComboBox(self.pg_money)
        self.cb_district_money.setGeometry(QtCore.QRect(50, 120, 200, 30))
        self.cb_district_money.setStyleSheet("background-color : white\n"
"")
        self.cb_district_money.setObjectName("cb_district_money")
        self.cb_local_money = QtWidgets.QComboBox(self.pg_money)
        self.cb_local_money.setGeometry(QtCore.QRect(50, 170, 200, 30))
        self.cb_local_money.setStyleSheet("background-color : white\n"
"")
        self.cb_local_money.setObjectName("cb_local_money")
        self.pb_scan_money = QtWidgets.QPushButton(self.pg_money)
        self.pb_scan_money.setGeometry(QtCore.QRect(50, 220, 200, 30))
        self.pb_scan_money.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_scan_money.setObjectName("pb_scan_money")
        self.label_17 = QtWidgets.QLabel(self.pg_money)
        self.label_17.setGeometry(QtCore.QRect(270, 180, 70, 70))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("./img/cado.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.sw_scan.addWidget(self.pg_money)
        self.pg_location = QtWidgets.QWidget()
        self.pg_location.setObjectName("pg_location")
        self.le_location = QtWidgets.QLineEdit(self.pg_location)
        self.le_location.setGeometry(QtCore.QRect(50, 90, 200, 30))
        self.le_location.setStyleSheet("background-color : white;")
        self.le_location.setObjectName("le_location")
        self.label_12 = QtWidgets.QLabel(self.pg_location)
        self.label_12.setGeometry(QtCore.QRect(50, 50, 200, 30))
        self.label_12.setStyleSheet("color : #ffce32;\n"
"font-weight : bold;\n"
"\n"
"")
        self.label_12.setObjectName("label_12")
        self.pb_scan_location = QtWidgets.QPushButton(self.pg_location)
        self.pb_scan_location.setGeometry(QtCore.QRect(50, 140, 200, 30))
        self.pb_scan_location.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_scan_location.setObjectName("pb_scan_location")
        self.label_18 = QtWidgets.QLabel(self.pg_location)
        self.label_18.setGeometry(QtCore.QRect(270, 90, 70, 70))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("./img/cado.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.sw_scan.addWidget(self.pg_location)
        self.sw_condition.addWidget(self.pg_scan)
        self.pg_realestate = QtWidgets.QWidget()
        self.pg_realestate.setObjectName("pg_realestate")
        self.tw_realestate = QtWidgets.QTableWidget(self.pg_realestate)
        self.tw_realestate.setGeometry(QtCore.QRect(0, 30, 360, 270))
        self.tw_realestate.setStyleSheet("background-color : white;")
        self.tw_realestate.setObjectName("tw_realestate")
        self.tw_realestate.setColumnCount(3)
        self.tw_realestate.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_realestate.setHorizontalHeaderItem(2, item)
        self.pb_result_realestate = QtWidgets.QPushButton(self.pg_realestate)
        self.pb_result_realestate.setGeometry(QtCore.QRect(70, 320, 200, 30))
        self.pb_result_realestate.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_result_realestate.setObjectName("pb_result_realestate")
        self.label_25 = QtWidgets.QLabel(self.pg_realestate)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 200, 30))
        self.label_25.setStyleSheet("color : #ffce32;\n"
"font-weight : bold;\n"
"\n"
"")
        self.label_25.setObjectName("label_25")
        self.wg_scan_map = QtWebEngineWidgets.QWebEngineView(self.pg_realestate)
        self.wg_scan_map.setGeometry(QtCore.QRect(380, 0, 360, 360))
        self.wg_scan_map.setStyleSheet("background-color : white;")
        self.wg_scan_map.setObjectName("wg_scan_map")
        self.sw_condition.addWidget(self.pg_realestate)
        self.sw_result.addWidget(self.pg_main_scan)
        self.pg_result = QtWidgets.QWidget()
        self.pg_result.setObjectName("pg_result")
        self.widget_19 = QtWidgets.QWidget(self.pg_result)
        self.widget_19.setGeometry(QtCore.QRect(20, 10, 200, 40))
        self.widget_19.setStyleSheet("background-color : #ffce32")
        self.widget_19.setObjectName("widget_19")
        self.label_20 = QtWidgets.QLabel(self.widget_19)
        self.label_20.setGeometry(QtCore.QRect(0, 5, 200, 30))
        self.label_20.setStyleSheet("background-color : #009223;\n"
"color : #ffce32;\n"
"font-size : 12;\n"
"font-weight : bold;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.sw_analysis_result = QtWidgets.QStackedWidget(self.pg_result)
        self.sw_analysis_result.setGeometry(QtCore.QRect(20, 70, 740, 320))
        self.sw_analysis_result.setObjectName("sw_analysis_result")
        self.pg_result_data = QtWidgets.QWidget()
        self.pg_result_data.setObjectName("pg_result_data")
        self.result = QtWidgets.QWidget(self.pg_result_data)
        self.result.setGeometry(QtCore.QRect(0, 10, 350, 310))
        self.result.setStyleSheet("background-color : white;")
        self.result.setObjectName("result")
        self.label_21 = QtWidgets.QLabel(self.result)
        self.label_21.setGeometry(QtCore.QRect(120, 90, 101, 31))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.result)
        self.label_22.setGeometry(QtCore.QRect(120, 140, 56, 12))
        self.label_22.setObjectName("label_22")
        self.graph = QtWidgets.QWidget(self.pg_result_data)
        self.graph.setGeometry(QtCore.QRect(380, 10, 350, 310))
        self.graph.setStyleSheet("background-color : white;")
        self.graph.setObjectName("graph")
        self.label_23 = QtWidgets.QLabel(self.graph)
        self.label_23.setGeometry(QtCore.QRect(130, 130, 81, 41))
        self.label_23.setObjectName("label_23")
        self.sw_analysis_result.addWidget(self.pg_result_data)
        self.pg_result_map = QtWidgets.QWidget()
        self.pg_result_map.setObjectName("pg_result_map")
        self.wg_map_result = QtWebEngineWidgets.QWebEngineView(self.pg_result_map)
        self.wg_map_result.setGeometry(QtCore.QRect(0, 0, 740, 320))
        self.wg_map_result.setStyleSheet("background-color : white;")
        self.wg_map_result.setObjectName("wg_map_result")
        self.sw_analysis_result.addWidget(self.pg_result_map)
        self.pb_show_data = QtWidgets.QPushButton(self.pg_result)
        self.pb_show_data.setGeometry(QtCore.QRect(250, 20, 80, 30))
        self.pb_show_data.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_show_data.setObjectName("pb_show_data")
        self.pb_show_map = QtWidgets.QPushButton(self.pg_result)
        self.pb_show_map.setGeometry(QtCore.QRect(350, 20, 80, 30))
        self.pb_show_map.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_show_map.setObjectName("pb_show_map")
        self.pb_start_page = QtWidgets.QPushButton(self.pg_result)
        self.pb_start_page.setGeometry(QtCore.QRect(660, 20, 80, 30))
        self.pb_start_page.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_start_page.setObjectName("pb_start_page")
        self.label_6 = QtWidgets.QLabel(self.pg_result)
        self.label_6.setGeometry(QtCore.QRect(570, 5, 60, 60))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("./img/sad.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pb_return = QtWidgets.QPushButton(self.pg_result)
        self.pb_return.setGeometry(QtCore.QRect(450, 20, 80, 30))
        self.pb_return.setStyleSheet("background-color : #ffce32;\n"
"border : 0px;\n"
"border-radius : 10%;\n"
"font-weight : bold;\n"
"color : #009223;\n"
"")
        self.pb_return.setObjectName("pb_return")
        self.sw_result.addWidget(self.pg_result)
        self.lb_previous = QtWidgets.QLabel(self.widget_11)
        self.lb_previous.setGeometry(QtCore.QRect(10, 30, 50, 50))
        self.lb_previous.setText("")
        self.lb_previous.setPixmap(QtGui.QPixmap("./img/left.png"))
        self.lb_previous.setScaledContents(True)
        self.lb_previous.setObjectName("lb_previous")
        self.widget_13 = QtWidgets.QWidget(self.widget_11)
        self.widget_13.setGeometry(QtCore.QRect(300, 35, 200, 40))
        self.widget_13.setStyleSheet("background-color : #ffce32")
        self.widget_13.setObjectName("widget_13")
        self.label_10 = QtWidgets.QLabel(self.widget_13)
        self.label_10.setGeometry(QtCore.QRect(0, 5, 200, 30))
        self.label_10.setStyleSheet("background-color : #009223;\n"
"color : #ffce32;\n"
"font-size : 12;\n"
"font-weight : bold;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.sw_main.addWidget(self.pg_analysis_page)
        self.pg_open_page = QtWidgets.QWidget()
        self.pg_open_page.setObjectName("pg_open_page")
        self.widget = QtWidgets.QWidget(self.pg_open_page)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget.setStyleSheet("background-color: #ffce32;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 500, 500))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./img/20603_23733_4810.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pb_start = QtWidgets.QPushButton(self.widget)
        self.pb_start.setGeometry(QtCore.QRect(665, 400, 120, 80))
        self.pb_start.setStyleSheet("QPushButton{\n"
"color : #009223;\n"
"font-size : 14pt;\n"
"font-weight : bold;\n"
"border : 7px solid;\n"
"border-color : #009223;\n"
"background-color : #ffce32 ;\n"
"border-radius : 20%;\n"
"}\n"
"")
        self.pb_start.setFlat(True)
        self.pb_start.setObjectName("pb_start")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(670, 300, 100, 100))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./img/hello.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.sw_main.addWidget(self.pg_open_page)
        self.sw_logo = QtWidgets.QStackedWidget(self.centralwidget)
        self.sw_logo.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.sw_logo.setObjectName("sw_logo")
        self.pg_logo_open = QtWidgets.QWidget()
        self.pg_logo_open.setObjectName("pg_logo_open")
        self.widget_2 = QtWidgets.QWidget(self.pg_logo_open)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.widget_2.setStyleSheet("background-color : #ffce32")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(150, 0, 500, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./img/logo-crop.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.sw_logo.addWidget(self.pg_logo_open)
        self.pg_logo_menu = QtWidgets.QWidget()
        self.pg_logo_menu.setObjectName("pg_logo_menu")
        self.widget_4 = QtWidgets.QWidget(self.pg_logo_menu)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.widget_4.setStyleSheet("background-color : #009223")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(150, 0, 500, 100))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./img/logo_crop_color.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.sw_logo.addWidget(self.pg_logo_menu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sw_main.setCurrentIndex(2)
        self.sw_result.setCurrentIndex(0)
        self.sw_condition.setCurrentIndex(0)
        self.sw_scan.setCurrentIndex(0)
        self.sw_analysis_result.setCurrentIndex(0)
        self.sw_logo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "상권 및 유동인구 데이터"))
        self.pb_data_scan_button.setText(_translate("MainWindow", "검색"))
        self.label_16.setText(_translate("MainWindow", "데이터 리스트"))
        self.pb_all.setText(_translate("MainWindow", "전체"))
        self.pb_money.setText(_translate("MainWindow", "금액 조건"))
        self.pb_location.setText(_translate("MainWindow", "위치 조건"))
        self.pb_scan_all.setText(_translate("MainWindow", "분석 결과 보기"))
        self.label_13.setText(_translate("MainWindow", "원하는 구와 동 선택"))
        self.le_money.setPlaceholderText(_translate("MainWindow", "금액 입력 단위 : 만 원"))
        self.label_11.setText(_translate("MainWindow", "최대 투자 금액 입력"))
        self.pb_scan_money.setText(_translate("MainWindow", "검색"))
        self.label_12.setText(_translate("MainWindow", "분석을 보고 싶은 주소를 입력"))
        self.pb_scan_location.setText(_translate("MainWindow", "분석 결과 보기"))
        item = self.tw_realestate.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tw_realestate.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tw_realestate.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tw_realestate.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tw_realestate.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tw_realestate.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tw_realestate.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        self.pb_result_realestate.setText(_translate("MainWindow", "분석 결과 보기"))
        self.label_25.setText(_translate("MainWindow", "부동산 매물 선택"))
        self.label_20.setText(_translate("MainWindow", "분석 결과"))
        self.label_21.setText(_translate("MainWindow", "분석결과"))
        self.label_22.setText(_translate("MainWindow", "주소 등등"))
        self.label_23.setText(_translate("MainWindow", "그래프 출력"))
        self.pb_show_data.setText(_translate("MainWindow", "데이터 보기"))
        self.pb_show_map.setText(_translate("MainWindow", "지도 보기"))
        self.pb_start_page.setText(_translate("MainWindow", "처음으로"))
        self.pb_return.setText(_translate("MainWindow", "돌아가기"))
        self.label_10.setText(_translate("MainWindow", "입지조건 및 매물 분석"))
        self.pb_start.setText(_translate("MainWindow", "입지분석 \n"
"시작하기"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
