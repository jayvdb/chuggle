#!/usr/bin/python

# drawtext.py

import sys
import random
from PyQt4 import QtGui, QtCore

class Blobber(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
    self.pixmap=QtGui.QPixmap()
    self.bar=QtGui.QPixmap()
    self.setGeometry(QtCore.QRect(107,17,225,23))
    self.pixmap.load("Resources/blobs/blob-revert.png");
    self.bar.load("Resources/bar.png");
    self.multiselect=True

    self.selected1=0
    self.selected2=0
    self.content=["nothing","nothing","nothing","me","me","anon","nothing","nothing","nothing","nothing","nothing","nothing","nothing","nothing","nothing"]
    self.blobs={
        "anon":QtGui.QPixmap("Resources/blobs/blob-anon.png"),
        "blanked":QtGui.QPixmap("Resources/blobs/blob-blanked.png"),
        "blank":QtGui.QPixmap("Resources/blobs/blob-blank.png"),
        "blocked":QtGui.QPixmap("Resources/blobs/blob-blocked.png"),
        "blocknote":QtGui.QPixmap("Resources/blobs/blob-blocknote.png"),
        "bot":QtGui.QPixmap("Resources/blobs/blob-bot.png"),
        "ignored":QtGui.QPixmap("Resources/blobs/blob-ignored.png"),
        "me":QtGui.QPixmap("Resources/blobs/blob-me.png"),
        "message":QtGui.QPixmap("Resources/blobs/blob-message.png"),
        "new":QtGui.QPixmap("Resources/blobs/blob-new.png"),
        "none":QtGui.QPixmap("Resources/blobs/blob-none.png"),
        "nothing":QtGui.QPixmap("Resources/blobs/nothing.png"),
        "redirect":QtGui.QPixmap("Resources/blobs/blob-redirect.png"),
        "replaced":QtGui.QPixmap("Resources/blobs/blob-replaced.png"),
        "reported":QtGui.QPixmap("Resources/blobs/blob-reported.png"),
        "report":QtGui.QPixmap("Resources/blobs/blob-report.png"),
        "reverted":QtGui.QPixmap("Resources/blobs/blob-reverted.png"),
        "revert":QtGui.QPixmap("Resources/blobs/blob-revert.png"),
        "tag":QtGui.QPixmap("Resources/blobs/blob-tag.png"),
        "warn-1":QtGui.QPixmap("Resources/blobs/blob-warn-1.png"),
        "warn-2":QtGui.QPixmap("Resources/blobs/blob-warn-2.png"),
        "warn-3":QtGui.QPixmap("Resources/blobs/blob-warn-3.png"),
        "warn-4":QtGui.QPixmap("Resources/blobs/blob-warn-4.png"),
        "warning":QtGui.QPixmap("Resources/blobs/blob-warning.png")
        }


    def paintEvent(self, event):
        paint = QtGui.QPainter()
    line=QtCore.QLine(0,0,10,10)
        paint.begin(self)
        paint.setPen(QtGui.QColor(255, 0, 0))
    paint.drawPixmap(QtCore.QRectF(0, 0, 244, 17), self.bar, QtCore.QRectF(0,0,199,17))
    for i in range(0,15) :
        paint.drawPixmap(QtCore.QRectF((14-i)*16+1, 1, 15, 15), self.blobs[self.content[i]], QtCore.QRectF(0,0,15,15))
    if self.multiselect:
        if self.selected1 >= 0 and self.selected1 < 16:
            paint.drawRect(QtCore.QRect(239-(self.selected1*16),0,-(1+self.selected2-self.selected1)*16+2,16))
    else:
            if self.selected1 >= 0:
                paint.drawRect(QtCore.QRect(239-(self.selected1*16),0,-15,16))

    paint.end()
    
    def mousePressEvent(self, event):
    x=event.x()
    print x
    tmp = (239-x) / 17
    print tmp
    if self.content[tmp] != "nothing":
        self.selected1=tmp
        self.selected2=self.selected1
        self.update()
    
    def mouseReleaseEvent(self, event):
    x=event.x()
    tmp= (239-x) / 17
    if tmp >= 0 and tmp >= self.selected1 and self.content[tmp] != "nothing":
        self.selected2 = tmp
    self.update()

    def setMultiSelect(self, value):
    self.multiselect=value
    
    def select(self,s1,s2=None):
    self.selected1=s1
    if s2==None:
        s2=s1
    self.selected2=s2
    def unselect(self):
    self.selected1=-1
