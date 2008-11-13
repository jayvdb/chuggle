# -*- coding: utf-8 -*-

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
import init
import connector
import blobber
import re

re_local=re.compile("href=\"/")
re_local1=re.compile("href=\"/")
re_src=re.compile("src=\"/")
re_action=re.compile("action=\"/")

class Mw(KParts.MainWindow):
    def setupUi(self):
	apply (KParts.MainWindow.__init__, (self,))
        self.resize(QtCore.QSize(QtCore.QRect(0,0,1100,671).size()).expandedTo(self.minimumSizeHint()))
      	self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.setObjectName("mainwindow")

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0,0,1098,72))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxlayout.setContentsMargins(5,-1,5,-1)
        self.hboxlayout.setObjectName("hboxlayout")

        self.TB_diff_revert_warn = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_diff_revert_warn.setMinimumSize(QtCore.QSize(55,55))
	self.TB_diff_revert_warn.setIcon(QtGui.QIcon("Resources/icons/diff-revert-warn.png"))
	self.TB_diff_revert_warn.setIconSize(QSize(55,55))
        self.TB_diff_revert_warn.setObjectName("TB_diff_revert_warn")
        self.hboxlayout.addWidget(self.TB_diff_revert_warn)

        self.TB_diff_next = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_diff_next.setMinimumSize(QtCore.QSize(55,55))
	self.TB_diff_next.setIcon(QtGui.QIcon("Resources/icons/diff-next.png"))
	self.TB_diff_next.setIconSize(QSize(55,55))
        self.TB_diff_next.setObjectName("diff_next")
        self.hboxlayout.addWidget(self.TB_diff_next)

        self.line = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout.addWidget(self.line)

        self.TB_user_whitelist = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_user_whitelist.setMinimumSize(QtCore.QSize(55,55))
	self.TB_user_whitelist.setIcon(QtGui.QIcon("Resources/icons/user-whitelist.png"))
	self.TB_user_whitelist.setIconSize(QSize(55,55))
        self.TB_user_whitelist.setObjectName("TB_user_whitelist")
        self.hboxlayout.addWidget(self.TB_user_whitelist)

        self.TB_diff_revert = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_diff_revert.setMinimumSize(QtCore.QSize(55,55))
	self.TB_diff_revert.setIconSize(QSize(55,55))
	self.TB_diff_revert.setIcon(QtGui.QIcon("Resources/icons/diff-revert.png"))
        self.TB_diff_revert.setObjectName("TB_diff_revert")
        self.hboxlayout.addWidget(self.TB_diff_revert)

        self.TB_user_template = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_user_template.setMinimumSize(QtCore.QSize(55,55))
	self.TB_user_template.setIconSize(QSize(55,55))
	self.TB_user_template.setIcon(QtGui.QIcon("Resources/icons/user-template.png"))
        self.TB_user_template.setObjectName("TB_user_template")
        self.hboxlayout.addWidget(self.TB_user_template)

        self.TB_user_warn = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_user_warn.setMinimumSize(QtCore.QSize(55,55))
	self.TB_user_warn.setIconSize(QSize(55,55))
	self.TB_user_warn.setIcon(QtGui.QIcon("Resources/icons/user-warn.png"))
        self.TB_user_warn.setObjectName("TB_user_warn")
        self.hboxlayout.addWidget(self.TB_user_warn)

        self.line_2 = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hboxlayout.addWidget(self.line_2)

        self.TB_cancel_all = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_cancel_all.setMinimumSize(QtCore.QSize(55,55))
	self.TB_cancel_all.setIconSize(QSize(55,55))
	self.TB_cancel_all.setIcon(QtGui.QIcon("Resources/icons/cancel-all.png"))
        self.TB_cancel_all.setObjectName("TB_cancel_all")
        self.hboxlayout.addWidget(self.TB_cancel_all)

        self.TB_undo = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_undo.setMinimumSize(QtCore.QSize(55,55))
	self.TB_undo.setIconSize(QSize(55,55))
	self.TB_undo.setIcon(QtGui.QIcon("Resources/icons/undo.png"))
        self.TB_undo.setObjectName("TB_undo")
        self.hboxlayout.addWidget(self.TB_undo)

        self.line_8 = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.hboxlayout.addWidget(self.line_8)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0,0))
        self.label.setMaximumSize(QtCore.QSize(70,70))
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(150,0))
        self.comboBox.setMaximumSize(QtCore.QSize(150,16777215))
        self.comboBox.setObjectName("comboBox")
        self.gridlayout.addWidget(self.comboBox,0,1,1,1)

        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        self.comboBox_2 = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150,0))
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridlayout.addWidget(self.comboBox_2,1,1,1,1)
        self.hboxlayout.addLayout(self.gridlayout)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5,1,0,1,1)

        self.TB_history_prev = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_history_prev.setObjectName("TB_history_prev")
	self.TB_history_prev.setIconSize(QSize(20,20))
	self.TB_history_prev.setIcon(QtGui.QIcon("Resources/icons/history-previous.png"))
        self.gridlayout1.addWidget(self.TB_history_prev,0,1,1,1)

        self.TB_contribs_prev = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_contribs_prev.setObjectName("TB_contribs_prev")
	self.TB_contribs_prev.setIconSize(QSize(20,20))
	self.TB_contribs_prev.setIcon(QtGui.QIcon("Resources/icons/contribs-prev.png"))
        self.gridlayout1.addWidget(self.TB_contribs_prev,1,1,1,1)

        self.TB_history_next = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_history_next.setObjectName("TB_history_next")
	self.TB_history_next.setIconSize(QSize(20,20))
	self.TB_history_next.setIcon(QtGui.QIcon("Resources/icons/history-next.png"))
        self.gridlayout1.addWidget(self.TB_history_next,0,3,1,1)

        self.TB_contribs_next = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.TB_contribs_next.setObjectName("TB_contribs_next")
	self.TB_contribs_next.setIconSize(QSize(20,20))
	self.TB_contribs_next.setIcon(QtGui.QIcon("Resources/icons/contribs-next.png"))
        self.gridlayout1.addWidget(self.TB_contribs_next,1,3,1,1)

        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(70,16777215))
        self.label_4.setObjectName("label_4")
        self.gridlayout1.addWidget(self.label_4,0,0,1,1)

        self.listContribs = blobber.Blobber(self.horizontalLayoutWidget)
        self.listContribs.setMinimumSize(QtCore.QSize(160,0))
        self.listContribs.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.listContribs.setObjectName("listContribs")
        self.gridlayout1.addWidget(self.listContribs,0,2,1,1)

        self.widget_2 = QtGui.QWidget(self.horizontalLayoutWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(200,0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.widget_2.setObjectName("widget_2")
        self.gridlayout1.addWidget(self.widget_2,1,2,1,1)
        self.hboxlayout.addLayout(self.gridlayout1)

        self.verticalLayout = QtGui.QWidget(self.centralwidget)
        self.verticalLayout.setGeometry(QtCore.QRect(0,110,201,401))
        self.verticalLayout.setObjectName("verticalLayout")

        self.vboxlayout = QtGui.QVBoxLayout(self.verticalLayout)
        self.vboxlayout.setSpacing(3)
        self.vboxlayout.setContentsMargins(5,3,3,3)
        self.vboxlayout.setObjectName("vboxlayout")

        self.numitems = QtGui.QLabel(self.verticalLayout)
        self.numitems.setMaximumSize(QtCore.QSize(16777215,15))
        self.numitems.setObjectName("numitems")
        self.vboxlayout.addWidget(self.numitems)

        self.listitems = QtGui.QWidget(self.verticalLayout)
        self.listitems.setObjectName("listitems")
        self.vboxlayout.addWidget(self.listitems)

        self.msgBox = QtGui.QListWidget(self.centralwidget)
        self.msgBox.setGeometry(QtCore.QRect(0,523,1061,81))
        self.msgBox.setObjectName("msgBox")

        self.horizontalLayout = QtGui.QWidget(self.centralwidget)
        self.horizontalLayout.setGeometry(QtCore.QRect(1,60,857,65))
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.horizontalLayout)
        self.hboxlayout1.setContentsMargins(5,3,3,3)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.TB_browser_prev = QtGui.QToolButton(self.horizontalLayout)
        self.TB_browser_prev.setMinimumSize(QtCore.QSize(35,35))
	self.TB_browser_prev.setIconSize(QSize(35,35))
	self.TB_browser_prev.setIcon(QtGui.QIcon("Resources/icons/browser-prev.png"))
        self.TB_browser_prev.setObjectName("TB_browser_prev")
        self.hboxlayout1.addWidget(self.TB_browser_prev)

        self.TB_browser_next = QtGui.QToolButton(self.horizontalLayout)
        self.TB_browser_next.setMinimumSize(QtCore.QSize(35,35))
	self.TB_browser_next.setIconSize(QSize(35,35))
	self.TB_browser_next.setIcon(QtGui.QIcon("Resources/icons/browser-next.png"))
        self.TB_browser_next.setObjectName("TB_browser_next")
        self.hboxlayout1.addWidget(self.TB_browser_next)

        self.line_3 = QtGui.QFrame(self.horizontalLayout)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.hboxlayout1.addWidget(self.line_3)

        self.TB_browser_open = QtGui.QToolButton(self.horizontalLayout)
        self.TB_browser_open.setMinimumSize(QtCore.QSize(35,35))
	self.TB_browser_open.setIconSize(QSize(35,35))
	self.TB_browser_open.setIcon(QtGui.QIcon("Resources/icons/browser-open.png"))
        self.TB_browser_open.setObjectName("TB_browser_open")
        self.hboxlayout1.addWidget(self.TB_browser_open)

        self.TB_browser_add_tab = QtGui.QToolButton(self.horizontalLayout)
        self.TB_browser_add_tab.setMinimumSize(QtCore.QSize(35,35))
	self.TB_browser_add_tab.setIconSize(QSize(35,35))
	self.TB_browser_add_tab.setIcon(QtGui.QIcon("Resources/icons/browser-add-tab.png"))
        self.TB_browser_add_tab.setObjectName("TB_browser_add_tab")
        self.hboxlayout1.addWidget(self.TB_browser_add_tab)

        self.TB_browser_remove_tab = QtGui.QToolButton(self.horizontalLayout)
        self.TB_browser_remove_tab.setMinimumSize(QtCore.QSize(35,35))
	self.TB_browser_remove_tab.setIconSize(QSize(35,35))
	self.TB_browser_remove_tab.setIcon(QtGui.QIcon("Resources/icons/browser-remove-tab.png"))
        self.TB_browser_remove_tab.setObjectName("TB_browser_remove_tab")
        self.hboxlayout1.addWidget(self.TB_browser_remove_tab)

        self.line_4 = QtGui.QFrame(self.horizontalLayout)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.hboxlayout1.addWidget(self.line_4)

        self.TB_history_prev_2 = QtGui.QToolButton(self.horizontalLayout)
        self.TB_history_prev_2.setMinimumSize(QtCore.QSize(35,35))
	self.TB_history_prev_2.setIconSize(QSize(35,35))
	self.TB_history_prev_2.setIcon(QtGui.QIcon("Resources/icons/history-previous.png"))
        self.TB_history_prev_2.setObjectName("TB_history_prev_2")
        self.hboxlayout1.addWidget(self.TB_history_prev_2)

        self.TB_history_next_2 = QtGui.QToolButton(self.horizontalLayout)
        self.TB_history_next_2.setMinimumSize(QtCore.QSize(35,35))
	self.TB_history_next_2.setIconSize(QSize(35,35))
	self.TB_history_next_2.setIcon(QtGui.QIcon("Resources/icons/history-next.png"))
        self.TB_history_next_2.setObjectName("TB_history_next_2")
        self.hboxlayout1.addWidget(self.TB_history_next_2)

        self.TB_history_last = QtGui.QToolButton(self.horizontalLayout)
        self.TB_history_last.setMinimumSize(QtCore.QSize(35,35))
	self.TB_history_last.setIconSize(QSize(35,35))
	self.TB_history_last.setIcon(QtGui.QIcon("Resources/icons/history-last.png"))
        self.TB_history_last.setObjectName("TB_history_last")
        self.hboxlayout1.addWidget(self.TB_history_last)

        self.TB_history_to_cur = QtGui.QToolButton(self.horizontalLayout)
        self.TB_history_to_cur.setMinimumSize(QtCore.QSize(35,35))
	self.TB_history_to_cur.setIconSize(QSize(35,35))
	self.TB_history_to_cur.setIcon(QtGui.QIcon("Resources/icons/history-to-cur.png"))
        self.TB_history_to_cur.setObjectName("TB_history_to_cur")
        self.hboxlayout1.addWidget(self.TB_history_to_cur)

        self.line_5 = QtGui.QFrame(self.horizontalLayout)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.hboxlayout1.addWidget(self.line_5)

        self.TB_contribs_prev_2 = QtGui.QToolButton(self.horizontalLayout)
        self.TB_contribs_prev_2.setMinimumSize(QtCore.QSize(35,35))
	self.TB_contribs_prev_2.setIconSize(QSize(35,35))
	self.TB_contribs_prev_2.setIcon(QtGui.QIcon("Resources/icons/contribs-prev.png"))
        self.TB_contribs_prev_2.setObjectName("TB_contribs_prev_2")
        self.hboxlayout1.addWidget(self.TB_contribs_prev_2)

        self.TB_contribs_next_2 = QtGui.QToolButton(self.horizontalLayout)
        self.TB_contribs_next_2.setMinimumSize(QtCore.QSize(35,35))
	self.TB_contribs_next_2.setIconSize(QSize(35,35))
	self.TB_contribs_next_2.setIcon(QtGui.QIcon("Resources/icons/contribs-next.png"))
        self.TB_contribs_next_2.setObjectName("TB_contribs_next_2")
        self.hboxlayout1.addWidget(self.TB_contribs_next_2)

        self.TB_contribs_last = QtGui.QToolButton(self.horizontalLayout)
        self.TB_contribs_last.setMinimumSize(QtCore.QSize(35,35))
	self.TB_contribs_last.setIconSize(QSize(35,35))
	self.TB_contribs_last.setIcon(QtGui.QIcon("Resources/icons/contribs-last.png"))
        self.TB_contribs_last.setObjectName("TB_contribs_last")
        self.hboxlayout1.addWidget(self.TB_contribs_last)

        self.line_6 = QtGui.QFrame(self.horizontalLayout)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.hboxlayout1.addWidget(self.line_6)

        self.TB_page_view = QtGui.QToolButton(self.horizontalLayout)
        self.TB_page_view.setMinimumSize(QtCore.QSize(35,35))
	self.TB_page_view.setIconSize(QSize(35,35))
	self.TB_page_view.setIcon(QtGui.QIcon("Resources/icons/page-view.png"))
        self.TB_page_view.setObjectName("TB_page_view")
        self.hboxlayout1.addWidget(self.TB_page_view)

        self.TB_page_edit = QtGui.QToolButton(self.horizontalLayout)
        self.TB_page_edit.setMinimumSize(QtCore.QSize(35,35))
	self.TB_page_edit.setIconSize(QSize(35,35))
	self.TB_page_edit.setIcon(QtGui.QIcon("Resources/icons/page-edit.png"))
        self.TB_page_edit.setObjectName("TB_page_edit")
        self.hboxlayout1.addWidget(self.TB_page_edit)

        self.TB_page_tag = QtGui.QToolButton(self.horizontalLayout)
        self.TB_page_tag.setMinimumSize(QtCore.QSize(35,35))
	self.TB_page_tag.setIconSize(QSize(35,35))
	self.TB_page_tag.setIcon(QtGui.QIcon("Resources/icons/page-tag.png"))
        self.TB_page_tag.setObjectName("TB_page_tag")
        self.hboxlayout1.addWidget(self.TB_page_tag)

        self.TB_page_delete = QtGui.QToolButton(self.horizontalLayout)
        self.TB_page_delete.setMinimumSize(QtCore.QSize(35,35))
	self.TB_page_delete.setIconSize(QSize(35,35))
	self.TB_page_delete.setIcon(QtGui.QIcon("Resources/icons/page-delete.png"))
        self.TB_page_delete.setObjectName("TB_page_delete")
        self.hboxlayout1.addWidget(self.TB_page_delete)

        self.TB_page_watch = QtGui.QToolButton(self.horizontalLayout)
        self.TB_page_watch.setMinimumSize(QtCore.QSize(35,35))
	self.TB_page_watch.setIconSize(QSize(35,35))
	self.TB_page_watch.setIcon(QtGui.QIcon("Resources/icons/page-watch.png"))
        self.TB_page_watch.setObjectName("TB_page_watch")
        self.hboxlayout1.addWidget(self.TB_page_watch)

        self.line_7 = QtGui.QFrame(self.horizontalLayout)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.hboxlayout1.addWidget(self.line_7)

        self.TB_user_info = QtGui.QToolButton(self.horizontalLayout)
        self.TB_user_info.setMinimumSize(QtCore.QSize(35,35))
	self.TB_user_info.setIconSize(QSize(35,35))
	self.TB_user_info.setIcon(QtGui.QIcon("Resources/icons/user-info.png"))
        self.TB_user_info.setObjectName("TB_user_info")
        self.hboxlayout1.addWidget(self.TB_user_info)

        self.TB_user_talk = QtGui.QToolButton(self.horizontalLayout)
        self.TB_user_talk.setMinimumSize(QtCore.QSize(35,35))
	self.TB_user_talk.setIconSize(QSize(35,35))
	self.TB_user_talk.setIcon(QtGui.QIcon("Resources/icons/user-talk.png"))
        self.TB_user_talk.setObjectName("TB_user_talk")
        self.hboxlayout1.addWidget(self.TB_user_talk)

        self.TB_user_message = QtGui.QToolButton(self.horizontalLayout)
        self.TB_user_message.setMinimumSize(QtCore.QSize(35,35))
	self.TB_user_message.setIconSize(QSize(35,35))
	self.TB_user_message.setIcon(QtGui.QIcon("Resources/icons/user-message.png"))
        self.TB_user_message.setObjectName("TB_user_message")
        self.hboxlayout1.addWidget(self.TB_user_message)

        self.TB_user_report = QtGui.QToolButton(self.horizontalLayout)
        self.TB_user_report.setMinimumSize(QtCore.QSize(35,35))
	self.TB_user_report.setIconSize(QSize(35,35))
	self.TB_user_report.setIcon(QtGui.QIcon("Resources/icons/user-report.png"))
        self.TB_user_report.setObjectName("TB_user_report")
        self.hboxlayout1.addWidget(self.TB_user_report)

        self.verticalLayout_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayout_2.setGeometry(QtCore.QRect(210,110,881,401))
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.verticalLayout_2)
        self.vboxlayout1.setObjectName("vboxlayout1")
	
	self.visor =KHTMLPart(self.verticalLayout_2)
	self.visor.setObjectName("visor")
	self.visor.begin()

	url = "http://"+config.language+"."+config.project+".org"

	self.visor.openUrl (KUrl(url))
        self.vboxlayout1.addWidget(self.visor.view())

	self.visor.show()
	self.extension=self.visor.browserExtension()


        self.widget_3 = QtGui.QWidget(self.verticalLayout_2)
        self.widget_3.setObjectName("widget_3")
        self.vboxlayout1.addWidget(self.widget_3)
        self.setCentralWidget(self.centralwidget)
	
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0,0,1270,27))
        self.menubar.setObjectName("menubar")

        self.menuSystem = QtGui.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")

        self.menuQueue = QtGui.QMenu(self.menubar)
        self.menuQueue.setObjectName("menuQueue")

        self.menu_page = QtGui.QMenu(self.menubar)
        self.menu_page.setObjectName("menu_page")

        self.menuUser = QtGui.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")

        self.menuBrowser = QtGui.QMenu(self.menubar)
        self.menuBrowser.setObjectName("menuBrowser")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSystem.menuAction())
        self.menubar.addAction(self.menuQueue.menuAction())
        self.menubar.addAction(self.menu_page.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuBrowser.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.comboBox)
        self.label_2.setBuddy(self.comboBox_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.comboBox,self.comboBox_2)
        self.setTabOrder(self.comboBox_2,self.TB_history_prev)
        self.setTabOrder(self.TB_history_prev,self.TB_contribs_prev)
        self.setTabOrder(self.TB_contribs_prev,self.TB_history_next)
        self.setTabOrder(self.TB_history_next,self.TB_contribs_next)
        self.setTabOrder(self.TB_contribs_next,self.msgBox)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("mainwindow", "Chuggle v0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_diff_revert_warn.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        #self.TB_diff_next.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_whitelist.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_diff_revert.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_template.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_warn.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_cancel_all.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_undo.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainwindow", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mainwindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mainwindow", "Contribs", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_history_prev.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_contribs_prev.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_history_next.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_contribs_next.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mainwindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.numitems.setText(QtGui.QApplication.translate("mainwindow", "No events", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_browser_prev.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_browser_next.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_browser_open.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_browser_add_tab.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_browser_remove_tab.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_history_prev_2.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_history_next_2.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_history_last.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_history_to_cur.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_contribs_prev_2.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_contribs_next_2.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_contribs_last.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_page_view.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_page_edit.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_page_tag.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_page_delete.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_page_watch.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_info.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_talk.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_message.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TB_user_report.setText(QtGui.QApplication.translate("mainwindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSystem.setTitle(QtGui.QApplication.translate("mainwindow", "&System", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQueue.setTitle(QtGui.QApplication.translate("mainwindow", "Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_page.setTitle(QtGui.QApplication.translate("mainwindow", "&Page", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUser.setTitle(QtGui.QApplication.translate("mainwindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBrowser.setTitle(QtGui.QApplication.translate("mainwindow", "Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainwindow", "Help", None, QtGui.QApplication.UnicodeUTF8))

    def __init__ (self, *args):
    	self.setupUi()
	self.dialog=init.initform(self)
	QtCore.QObject.connect(self.dialog.ui.PB_login,QtCore.SIGNAL("clicked()"),self.login)
	QtCore.QObject.connect(self.dialog.ui.PB_exit,QtCore.SIGNAL("clicked()"),self.queryExit)
	QtCore.QObject.connect(self.extension, SIGNAL ('openUrlRequest (const KUrl&, const KParts::OpenUrlArguments&, const KParts::BrowserArguments&)'), self.changePage)
	self.conn=connector.Connector()
	self.conn.register(self.writeMsgBox,"writeMsgBox")	
	self.conn.register(self.setNumItems,"setNumItems")	
	self.dialog.exec_()
    def changePage(self, url, args):
	myurl = str(KUrl(url).prettyUrl().toUtf8())
	#if it is an external link, we feed id directly to KHTMLpart
	#it it is not, we do a workaround to inject our headers
	if myurl.find("http://"+config.language+"."+config.project+".org/") == -1:
	    	self.visor.openUrl(KUrl(url))
	else:
		headers = { 'User-Agent' : config.useragent, 
			'Cookie': self.dv.lm.cookies() }
		#convert relative links to absolute
		if myurl[0:8]=="file:///":
			myurl="href=\"http://"+config.language+"."+config.project+".org/"+myurl[7:]
		try:
			response = urllib2.urlopen(urllib2.Request(myurl, None, headers))
			html = response.read()
			html=re_local.sub("href=\"http://"+config.language+"."+config.project+".org/",html)
			html=re_local1.sub("href='http://"+config.language+"."+config.project+".org/",html)

			html=re_src.sub("src=\"http://"+config.language+"."+config.project+".org/",html)
			html=re_action.sub("action=\"http://"+config.language+"."+config.project+".org/",html)
			self.visor.begin()
			self.visor.write(html)
			self.visor.end()
		except:
			self.writeMsgBox("Unable to open link")

    def connect(self):
	#connections
	QtCore.QObject.connect(self.TB_diff_next,QtCore.SIGNAL("clicked()"),self.dv.viewDiff)
	QtCore.QObject.connect(self.TB_diff_revert,QtCore.SIGNAL("clicked()"),self.dv.revert)    
	QtCore.QObject.connect(self.TB_user_whitelist,QtCore.SIGNAL("clicked()"),self.dv.addWhitelist)
	
    def login(self):
	username = self.dialog.ui.LE_username.text()
	password = self.dialog.ui.LE_password.text()
	self.dialog.ui.Result.setText("Logging as "+username)
	self.dv=deliverer.Dv(self.visor,self.conn)
	if self.dv.login(username,password):
		self.show()
		self.dialog.hide()
		self.connect()
		self.dv.startbot()
		self.writeMsgBox("Connecting irc bot")

	else :
	    self.dialog.ui.Result.setText("Login failed")

    def writeMsgBox(self,msg):
	self.msgBox.insertItem(0,msg)
    def setNumItems(self,num):
	self.numitems.setText(QtGui.QApplication.translate("mainwindow", "Events in queue: ", None, QtGui.QApplication.UnicodeUTF8)+repr(num))
#	self.numItems.setText("Elements in queue: "+repr(num))
    def queryExit(self):
	#// this slot is invoked in addition when the *last* window is going
	#// to be closed. We could do some final cleanup here.
	sys.exit()
	return TRUE #// accept


appName     = "Chuggle"
catalog     = ""
programName = ki18n ("Chuggle")
version     = "0.1"
description = ki18n ("Chuggle")
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
sys.exit(app.exec_())

