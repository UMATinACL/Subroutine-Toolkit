# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 571, 122))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_for_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_for_select.setObjectName("btn_for_select")
        self.gridLayout.addWidget(self.btn_for_select, 2, 2, 1, 1)
        self.input_for = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_for.setText("")
        self.input_for.setObjectName("input_for")
        self.gridLayout.addWidget(self.input_for, 2, 1, 1, 1)
        self.btn_inp_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_inp_select.setObjectName("btn_inp_select")
        self.gridLayout.addWidget(self.btn_inp_select, 1, 2, 1, 1)
        self.label_for = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_for.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for.setObjectName("label_for")
        self.gridLayout.addWidget(self.label_for, 2, 0, 1, 1)
        self.label_inp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_inp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_inp.setObjectName("label_inp")
        self.gridLayout.addWidget(self.label_inp, 1, 0, 1, 1)
        self.input_inp = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_inp.setObjectName("input_inp")
        self.gridLayout.addWidget(self.input_inp, 1, 1, 1, 1)
        self.label_workingdirection = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_workingdirection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_workingdirection.setObjectName("label_workingdirection")
        self.gridLayout.addWidget(self.label_workingdirection, 0, 0, 1, 1)
        self.input_working_dir = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_working_dir.setObjectName("input_working_dir")
        self.gridLayout.addWidget(self.input_working_dir, 0, 1, 1, 1)
        self.btn_work_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_work_select.setObjectName("btn_work_select")
        self.gridLayout.addWidget(self.btn_work_select, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn_run = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_run.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_run.setAutoFillBackground(False)
        self.btn_run.setIconSize(QtCore.QSize(16, 32))
        self.btn_run.setAutoRepeat(False)
        self.btn_run.setAutoExclusive(False)
        self.btn_run.setObjectName("btn_run")
        self.verticalLayout.addWidget(self.btn_run)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 571, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_dataSuffix = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_dataSuffix.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dataSuffix.setObjectName("label_dataSuffix")
        self.horizontalLayout.addWidget(self.label_dataSuffix)
        self.input_data_file = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.input_data_file.setText("")
        self.input_data_file.setObjectName("input_data_file")
        self.horizontalLayout.addWidget(self.input_data_file)
        self.btn_dataDealing = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_dataDealing.setObjectName("btn_dataDealing")
        self.horizontalLayout.addWidget(self.btn_dataDealing)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 80, 571, 471))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox_keyword = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_keyword.setGeometry(QtCore.QRect(70, 40, 131, 23))
        self.comboBox_keyword.setObjectName("comboBox_keyword")
        self.label_keyword = QtWidgets.QLabel(self.tab_2)
        self.label_keyword.setGeometry(QtCore.QRect(10, 40, 50, 21))
        self.label_keyword.setAlignment(QtCore.Qt.AlignCenter)
        self.label_keyword.setObjectName("label_keyword")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btn_run.clicked.connect(MainWindow.slot_runScrit)
        self.btn_inp_select.clicked.connect(MainWindow.slot_setInpName)
        self.btn_for_select.clicked.connect(MainWindow.slot_setForName)
        self.btn_dataDealing.clicked.connect(MainWindow.slot_dataDealing)
        self.comboBox_keyword.currentTextChanged['QString'].connect(MainWindow.slot_update)
        self.btn_work_select.clicked.connect(MainWindow.slot_setWorkingDir)
        self.input_inp.textChanged['QString'].connect(MainWindow.slot_input_inp_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_inp, self.input_for)
        MainWindow.setTabOrder(self.input_for, self.btn_inp_select)
        MainWindow.setTabOrder(self.btn_inp_select, self.btn_for_select)
        MainWindow.setTabOrder(self.btn_for_select, self.input_data_file)
        MainWindow.setTabOrder(self.input_data_file, self.btn_dataDealing)
        MainWindow.setTabOrder(self.btn_dataDealing, self.comboBox_keyword)
        MainWindow.setTabOrder(self.comboBox_keyword, self.plainTextEdit)
        MainWindow.setTabOrder(self.plainTextEdit, self.btn_run)
        MainWindow.setTabOrder(self.btn_run, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Subroutine Toolkit"))
        self.btn_for_select.setText(_translate("MainWindow", "SELECT"))
        self.btn_inp_select.setText(_translate("MainWindow", "SELECT"))
        self.label_for.setText(_translate("MainWindow", ".for Name"))
        self.label_inp.setText(_translate("MainWindow", ".inp Name"))
        self.label_workingdirection.setText(_translate("MainWindow", "Working Direction"))
        self.btn_work_select.setText(_translate("MainWindow", "SELECT"))
        self.btn_run.setText(_translate("MainWindow", "RUN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Run Cmd"))
        self.label_dataSuffix.setText(_translate("MainWindow", "data file"))
        self.btn_dataDealing.setText(_translate("MainWindow", "DATA DEALING"))
        self.label_keyword.setText(_translate("MainWindow", "keyword"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data Dealing"))
