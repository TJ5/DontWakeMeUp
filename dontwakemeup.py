# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dont wake me up.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(550, 30, 201, 218))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout.addWidget(self.doubleSpinBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout.addWidget(self.doubleSpinBox_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 30, 481, 371))
        self.graphicsView.setObjectName("graphicsView")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(570, 260, 61, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 320, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 320, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(670, 260, 61, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 340, 181, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 370, 101, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_2.setText(_translate("MainWindow", "Set X Threshold"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Alarm"))
        self.label.setText(_translate("MainWindow", "Set Y Threshold"))
        self.pushButton.setText(_translate("MainWindow", "Set Alarm"))
        self.label_3.setText(_translate("MainWindow", "Set Z Threshold"))
        self.pushButton_3.setText(_translate("MainWindow", "Set Alarm"))
        self.label_4.setText(_translate("MainWindow", "Temperature"))
        self.label_5.setText(_translate("MainWindow", "Humidity"))
        self.label_6.setText(_translate("MainWindow", "Current Time & Day: 4:11 pm 2/5/22"))
        self.pushButton_4.setText(_translate("MainWindow", "Manual Capture"))
