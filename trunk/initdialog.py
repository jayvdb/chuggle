# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
#
# Created: Mon Nov 10 20:50:57 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_initdialog(object):
    def setupUi(self, initdialog):
        initdialog.setObjectName("initdialog")
        initdialog.resize(QtCore.QSize(QtCore.QRect(0,0,318,246).size()).expandedTo(initdialog.minimumSizeHint()))

        self.gridLayout = QtGui.QWidget(initdialog)
        self.gridLayout.setGeometry(QtCore.QRect(10,10,301,171))
        self.gridLayout.setObjectName("gridLayout")

        self.gridlayout = QtGui.QGridLayout(self.gridLayout)
        self.gridlayout.setObjectName("gridlayout")

        self.label_language = QtGui.QLabel(self.gridLayout)
        self.label_language.setObjectName("label_language")
        self.gridlayout.addWidget(self.label_language,0,0,1,1)

        self.CB_language = QtGui.QComboBox(self.gridLayout)
        self.CB_language.setObjectName("CB_language")
        self.gridlayout.addWidget(self.CB_language,0,1,1,1)

        self.label_project = QtGui.QLabel(self.gridLayout)
        self.label_project.setObjectName("label_project")
        self.gridlayout.addWidget(self.label_project,1,0,1,1)

        self.label_username = QtGui.QLabel(self.gridLayout)
        self.label_username.setObjectName("label_username")
        self.gridlayout.addWidget(self.label_username,2,0,1,1)

        self.label_password = QtGui.QLabel(self.gridLayout)
        self.label_password.setObjectName("label_password")
        self.gridlayout.addWidget(self.label_password,3,0,1,1)

        self.CB_project = QtGui.QComboBox(self.gridLayout)
        self.CB_project.setObjectName("CB_project")
        self.gridlayout.addWidget(self.CB_project,1,1,1,1)

        self.LE_username = QtGui.QLineEdit(self.gridLayout)
        self.LE_username.setObjectName("LE_username")
        self.gridlayout.addWidget(self.LE_username,2,1,1,1)

        self.LE_password = QtGui.QLineEdit(self.gridLayout)
        self.LE_password.setObjectName("LE_password")
	self.LE_password.setEchoMode(QtGui.QLineEdit.Password)
        self.gridlayout.addWidget(self.LE_password,3,1,1,1)

        self.horizontalLayout = QtGui.QWidget(initdialog)
        self.horizontalLayout.setGeometry(QtCore.QRect(10,180,301,32))
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.hboxlayout = QtGui.QHBoxLayout(self.horizontalLayout)
        self.hboxlayout.setObjectName("hboxlayout")

        self.PB_login = QtGui.QPushButton(self.horizontalLayout)
        self.PB_login.setObjectName("PB_login")
        self.hboxlayout.addWidget(self.PB_login)

        self.PB_exit = QtGui.QPushButton(self.horizontalLayout)
        self.PB_exit.setObjectName("PB_exit")
        self.hboxlayout.addWidget(self.PB_exit)

        self.Result = QtGui.QLabel(initdialog)
        self.Result.setGeometry(QtCore.QRect(10,220,301,20))
        self.Result.setObjectName("Result")

        self.retranslateUi(initdialog)
        QtCore.QMetaObject.connectSlotsByName(initdialog)

    def retranslateUi(self, initdialog):
        initdialog.setWindowTitle(QtGui.QApplication.translate("initdialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_language.setText(QtGui.QApplication.translate("initdialog", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_language.addItem(QtGui.QApplication.translate("initdialog", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_language.addItem(QtGui.QApplication.translate("initdialog", "Spanish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_project.setText(QtGui.QApplication.translate("initdialog", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_username.setText(QtGui.QApplication.translate("initdialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_password.setText(QtGui.QApplication.translate("initdialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.PB_login.setText(QtGui.QApplication.translate("initdialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.PB_exit.setText(QtGui.QApplication.translate("initdialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))

