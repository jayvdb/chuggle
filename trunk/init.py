# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
import sys
from PyQt4 import QtCore, QtGui
from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs, KUrl
from PyKDE4.kdeui import KApplication, KMainWindow
from PyKDE4.khtml import KHTMLPart, KHTMLView
from PyKDE4.kparts import KParts
from PyKDE4.kdecore import KComponentData
from PyQt4 import *
from initdialog import Ui_initdialog

#import main

class initform(QtGui.QDialog):
	def __init__(self, parent=None):
        	QtGui.QWidget.__init__(self, parent)
		self.parent=parent
	        self.ui = Ui_initdialog()
        	self.ui.setupUi(self)
	def closeEvent(self,arg):
	    	#if this dialog is closed, close everything
	    	self.parent.queryExit()
