#!/usr/bin/python
# -*- coding: utf-8  -*-

import sys, os, re, urllib2, urllib, thread
from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs, KUrl
from PyKDE4.kdeui import KApplication, KMainWindow
from PyKDE4.khtml import KHTMLPart, KHTMLView
from PyKDE4.kparts import KParts
from PyKDE4.kdecore import KComponentData
from PyQt4.QtGui import *
from PyQt4.QtCore import * 

from PyQt4 import *

#Our stuff
import config
import deliverer



def urlencode(query):
    """This can encode a query so that it can be sent as a query using
       a http POST request"""
    l=[]
    for k, v in query:
        k = urllib.quote(k)
        v = urllib.quote(v)
        l.append(k + '=' + v)
    return '&'.join(l)

class Mw (KParts.MainWindow):
        def setupUi(self):
		apply (KParts.MainWindow.__init__, (self,))
		
		self.resize(QtCore.QSize(QtCore.QRect(0,0,800,600).size()).expandedTo(self.minimumSizeHint()))
       		self.centralwidget = QtGui.QWidget(self)
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
    
		self.visor =KHTMLPart(self.verticalLayout)
		self.visor.setObjectName("visor")
#		self.vboxlayout.addWidget(self.visor)
		self.visor.begin()
		url = "http://"+config.language+"."+config.project+".org"

		self.visor.openUrl (KUrl(url))
	        self.vboxlayout.addWidget(self.visor.view())

		self.visor.show()
		self.extension=self.visor.browserExtension()
            	self.setCentralWidget(self.centralwidget)
    
            	self.menubar = QtGui.QMenuBar(self)
            	self.menubar.setGeometry(QtCore.QRect(0,0,1024,27))
            	self.menubar.setObjectName("menubar")
    
            	self.menuActions = QtGui.QMenu(self.menubar)
            	self.menuActions.setObjectName("menuActions")
            	self.setMenuBar(self.menubar)
    
            	self.statusbar = QtGui.QStatusBar(self)
            	self.statusbar.setObjectName("statusbar")
            	self.setStatusBar(self.statusbar)
    
            	self.actionRevert = QtGui.QAction(self)
            	self.actionRevert.setObjectName("actionRevert")
    
            	self.actionNext_diff = QtGui.QAction(self)
            	self.actionNext_diff.setObjectName("actionNext_diff")
    
            	self.actionBlock = QtGui.QAction(self)
            	self.actionBlock.setObjectName("actionBlock")
            	self.menuActions.addAction(self.actionNext_diff)
            	self.menuActions.addAction(self.actionRevert)
            	self.menuActions.addAction(self.actionBlock)
            	self.menubar.addAction(self.menuActions.menuAction())
		self.show()
    
            	self.retranslateUi()
    
        def retranslateUi(self):
            	self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chugel", None, QtGui.QApplication.UnicodeUTF8))
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


	def __init__ (self, *args):
	    	self.setupUi()


		#deliverer stuff
		self.dv=deliverer.Dv(self.visor)
	
		#Connections
#		self.connect(self.extension, SIGNAL ('openUrlRequest (const KUrl&, const KParts::OpenUrlArguments&, const KParts::BrowserArguments&)'), self.dv.viewDiff)
        	QtCore.QObject.connect(self.actionNext_diff,QtCore.SIGNAL("activated()"),self.dv.viewDiff)
	        QtCore.QObject.connect(self.pushButton_nextdiff,QtCore.SIGNAL("clicked()"),self.dv.viewDiff)
        	QtCore.QObject.connect(self.actionRevert,QtCore.SIGNAL("activated()"),self.dv.revert)
	        QtCore.QObject.connect(self.pushButton_revert,QtCore.SIGNAL("clicked()"),self.dv.revert)

            	QtCore.QMetaObject.connectSlotsByName(self)

	def queryExit(self):
#		#// this slot is invoked in addition when the *last* window is going
#		#// to be closed. We could do some final cleanup here.
		return TRUE #// accept

		
appName     = "Chugel"
catalog     = ""
programName = ki18n ("Chugel")
version     = "0.1"
description = ki18n ("Chugel")
license     = KAboutData.License_GPL
copyright   = ki18n ("Chabacano")
text        = ki18n ("none")
homePage    = "es.wikipedia.org/wiki/User:Chabacano"
bugEmail    = "chabawiki@gmail.com"

aboutData   = KAboutData (appName, catalog, programName, version, description,
			license, copyright, text, homePage, bugEmail)


KCmdLineArgs.init (sys.argv, aboutData)

app = KApplication ()
FALSE = 0
TRUE  = not FALSE

TOOLBAR_EXIT = 0
TOOLBAR_OPEN = 1

mainw=Mw()
mainw.show()
app.exec_()	

