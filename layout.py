# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created: Mon Aug  4 19:18:14 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,800,600).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtGui.QWidget(self.centralwidget)
        self.verticalLayout.setGeometry(QtCore.QRect(14,9,771,531))
        self.verticalLayout.setObjectName("verticalLayout")

        self.vboxlayout = QtGui.QVBoxLayout(self.verticalLayout)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.pushButton_revert = QtGui.QPushButton(self.verticalLayout)
        self.pushButton_revert.setObjectName("pushButton_revert")
        self.hboxlayout.addWidget(self.pushButton_revert)

        self.pushButton_nextdiff = QtGui.QPushButton(self.verticalLayout)
        self.pushButton_nextdiff.setObjectName("pushButton_nextdiff")
        self.hboxlayout.addWidget(self.pushButton_nextdiff)

        self.pushButton_block = QtGui.QPushButton(self.verticalLayout)
        self.pushButton_block.setObjectName("pushButton_block")
        self.hboxlayout.addWidget(self.pushButton_block)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.visor = QtGui.QWidget(self.verticalLayout)
        self.visor.setObjectName("visor")
        self.vboxlayout.addWidget(self.visor)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,27))
        self.menubar.setObjectName("menubar")

        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionRevert = QtGui.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")

        self.actionNext_diff = QtGui.QAction(MainWindow)
        self.actionNext_diff.setObjectName("actionNext_diff")

        self.actionBlock = QtGui.QAction(MainWindow)
        self.actionBlock.setObjectName("actionBlock")
        self.menuActions.addAction(self.actionNext_diff)
        self.menuActions.addAction(self.actionRevert)
        self.menuActions.addAction(self.actionBlock)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionNext_diff,QtCore.SIGNAL("activated()"),self.visor.)
        QtCore.QObject.connect(self.pushButton_nextdiff,QtCore.SIGNAL("clicked()"),self.visor.)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_revert.setText(QtGui.QApplication.translate("MainWindow", "Revert", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_nextdiff.setText(QtGui.QApplication.translate("MainWindow", "Next diff", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_block.setText(QtGui.QApplication.translate("MainWindow", "Block", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRevert.setText(QtGui.QApplication.translate("MainWindow", "Revert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRevert.setShortcut(QtGui.QApplication.translate("MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_diff.setText(QtGui.QApplication.translate("MainWindow", "Next diff", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_diff.setShortcut(QtGui.QApplication.translate("MainWindow", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlock.setText(QtGui.QApplication.translate("MainWindow", "Block", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlock.setShortcut(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))

