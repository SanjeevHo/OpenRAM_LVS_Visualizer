# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import json, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog,QMessageBox,QDesktopWidget

from json_parser import json_parser
from search_extfile_coordinates import magic

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 582)
        MainWindow.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        self.label.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"border-radius:10px;\n"
"font-weight:bold;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setStyleSheet("text-align:center;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_3.setStyleSheet("text-align:center;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_4.setStyleSheet("text-align:center;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_5.setStyleSheet("text-align:center;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_6.setStyleSheet("text-align:center;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_10.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"border-radius:10px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_6.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(143, 240, 164);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_8.addWidget(self.pushButton_6)
        self.verticalLayout.addWidget(self.frame_10)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(153, 193, 241);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"font-weight:bold;\n"
"border-radius:10px;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_8.hide()
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_10.addWidget(self.pushButton_7)
        self.pushButton_7.hide()
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(222, 221, 218);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_3)
        self.treeWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.treeWidget.setObjectName("treeWidget")
        
        
        self.verticalLayout_11.addWidget(self.treeWidget)
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

 
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Input Tab"))
        self.label_2.setText(_translate("MainWindow", "Schematic Netlist"))
        self.pushButton.setText(_translate("MainWindow", "Browse File"))
        self.label_3.setText(_translate("MainWindow", "Layout Netlist"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse File"))
        self.label_4.setText(_translate("MainWindow", "JSON Output file"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse File"))
        self.label_5.setText(_translate("MainWindow", "Magic (*.mag) file"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse File"))
        self.label_6.setText(_translate("MainWindow", "Ext (*.ext) File"))
        self.pushButton_5.setText(_translate("MainWindow", "Browse File"))
        self.pushButton_6.setText(_translate("MainWindow", "Start >>"))
        self.label_7.setText(_translate("MainWindow", "Views Tab"))
        self.pushButton_8.setText(_translate("MainWindow", "Schematic"))
        self.pushButton_7.setText(_translate("MainWindow", "Netlist"))
        self.pushButton_9.setText(_translate("MainWindow", "Cross Reference"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Keys"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Layout"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Schematic"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        # self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "pins"))
        # self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "A(3)"))
        # self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "A(3)"))
        # self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("MainWindow", "A"))
        # self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "sky130"))
        # self.treeWidget.topLevelItem(0).child(0).child(0).setText(1, _translate("MainWindow", "sky130"))
        # self.treeWidget.topLevelItem(0).child(0).child(0).setText(2, _translate("MainWindow", "sky130"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

class MainApp(QMainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

        # Set up the user interface from Design
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButton.clicked.connect(self.browseFile)
        self.browse_connect()
        self.ui.pushButton_6.clicked.connect(self.START_PROCESSING)
        self.colors = [
        QtCore.Qt.black,      # Color for root items
        QtCore.Qt.blue,       # Color for first-level child items
        QtCore.Qt.green,      # Color for second-level child items
        QtCore.Qt.magenta,    # Color for third-level child items
        QtCore.Qt.darkBlue,   # Color for fourth-level child items
        QtCore.Qt.darkGreen,  # ... and so on
        QtCore.Qt.darkMagenta,
        QtCore.Qt.darkRed,
        QtCore.Qt.darkGray,
        QtCore.Qt.darkCyan,
        # ... Add more colors if needed ...
        ]


    def recursive_parse(self, mark , d, parent_item=None):
        for key, value in d.items():
            current_item = self.funcKey(mark, key, parent_item)
            
            if len(value) == 3:
                self.func0(value[0], current_item)
                self.func1(value[1], current_item)
                if isinstance(value[2], dict):
                    self.recursive_parse(mark,value[2], current_item)
            elif len(value) == 2:
                self.func0(value[0], current_item)
                self.func1(value[1], current_item)

    def func0(self, val, item):
        item.setText(1, val)
        self.set_color_based_on_depth(item, 1)


    def func1(self, val, item):
        item.setText(2, val)
        self.set_color_based_on_depth(item, 2)

    def set_color_based_on_depth(self, item, column):
        # Determine depth
        depth = 0
        temp_item = item
        while temp_item.parent() is not None:
                temp_item = temp_item.parent()
                depth += 1

        # Set color based on depth
        color = self.colors[depth % len(self.colors)]  # Use modulo in case depth exceeds number of colors
        item.setForeground(column, QtGui.QBrush(color))



    def funcKey(self, mark, key, parent_item=None):
        item = QtWidgets.QTreeWidgetItem(parent_item)
        item.setData(0, QtCore.Qt.UserRole, mark)
        item.setText(0, key)
        self.set_color_based_on_depth(item, 0)
        return item

    def json_bana_di(self, jsonfile):

        f = open(jsonfile)
        d = json.load(f)
        f.close()

        # current_item.setData(0, QtCore.Qt.UserRole, "child")

        for root_key, root_value in d.items():
            root_item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
            root_item.setText(0, root_key)
            if root_key in ["nets", "pins"]:
                self.recursive_parse("pin_data", root_value, root_item)
            elif root_key in ["pin_connections"]:
                self.recursive_parse("pin_connection", root_value, root_item)
            else:
                self.recursive_parse("dev_data", root_value, root_item)

        self.ui.treeWidget.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_double_clicked(self, item):
        # Assuming only 2 depths are there (device and pins)
        if item.data(0, QtCore.Qt.UserRole) == "pin_data":
            if item.parent().parent() is None:
                a1=magic(self.ext_file ,self.magic_file, f'"{item.text(0)}"', "pin")
                if a1!="":
                    self.displayalert(a1)
                print(f"'{item.text(0)}' is a pin.")
            elif item.parent().parent().parent() is None:
                a1=magic(self.ext_file ,self.magic_file, item.text(0), "device")
                if a1!="":
                    self.displayalert(a1)
                print(f"'{item.text(0)}' is a device.")
            else:
                a1=magic(self.ext_file ,self.magic_file, f'"{item.text(0)}"', "pin")
                if a1!="":
                    self.displayalert(a1)
                print(f"'{item.text(0)}' is a pin.")
        elif item.data(0, QtCore.Qt.UserRole) == "dev_data":
            if item.parent() is None or item.parent().parent() is None:
                a1=magic(self.ext_file ,self.magic_file, item.text(0), "device")
                if a1!="":
                    self.displayalert(a1)
                print(f"'{item.text(0)}' is a device.")
            else:
                a1=magic(self.ext_file ,self.magic_file,f'"{item.text(0)}"', "pin")
                if a1!="":
                    self.displayalert(a1)
                print(f"'{item.text(0)}' is a pin.")
        elif item.data(0, QtCore.Qt.UserRole) == "pin_connection":
            a1=magic(self.ext_file ,self.magic_file, f'"{item.text(1)}"', "pin")
            if a1!="":
                    self.displayalert(a1)
            print(f"{item.text(1)} is a pin.")
    def displayalert(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)  # You can set this to be Warning, Critical, Information, etc.
        msg.setText(message)
        msg.setWindowTitle("Alert")
        qtRectangle = msg.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        msg.move(qtRectangle.topLeft())
        msg.exec_()


    def START_PROCESSING(self):
        json_parser(self.schematic_netlist, self.layout_netlist, self.json_file)
        self.json_bana_di("combined.json")
    
    
    def browse_connect(self):
        self.ui.pushButton.clicked.connect(self.browse_file_schematic)
        self.ui.pushButton_2.clicked.connect(self.browse_file_layout)
        self.ui.pushButton_3.clicked.connect(self.browse_file_json)
        self.ui.pushButton_4.clicked.connect(self.browse_file_magic)
        self.ui.pushButton_5.clicked.connect(self.browse_file_ext)

    def browse_file_schematic(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Browse File", "", "All Files (*)", options=options)
        if filePath:
            print(filePath)
            self.schematic_netlist = filePath
            self.ui.pushButton.setText(os.path.basename(filePath))


    def browse_file_layout(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Browse File", "", "All Files (*)", options=options)
        if filePath:
            print(filePath)
            self.layout_netlist = filePath
            self.ui.pushButton_2.setText(os.path.basename(filePath))

    def browse_file_json(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Browse File", "", "All Files (*)", options=options)
        if filePath:
            print(filePath)
            self.json_file = filePath
            self.ui.pushButton_3.setText(os.path.basename(filePath))

    def browse_file_magic(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Browse File", "", "All Files (*)", options=options)
        if filePath:
            print(filePath)
            self.magic_file = filePath
            self.ui.pushButton_4.setText(os.path.basename(filePath))

    def browse_file_ext(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Browse File", "", "All Files (*)", options=options)
        if filePath:
            print(filePath)
            self.ext_file = filePath
            self.ui.pushButton_5.setText(os.path.basename(filePath))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
    # JSONFILE = "combined.json"
    window = MainApp()
#     window.show()
    window.showMaximized()
#     ui.setupUi(MainWindow, JSONFILE)
#     MainWindow.show()
#     MainWindow.showMaximized()
    sys.exit(app.exec_())
