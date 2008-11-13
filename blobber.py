#!/usr/bin/python

# drawtext.py

import sys
import random
from PyQt4 import QtGui, QtCore

#class Blobber(QtGui.QWidget):
#	def __init__ (self, *args):
#	    	apply(QWidget.__init__, (self,) + args)
#		self.pixmap=QtGui.QPixmap()
#		self.pixmap.load(":/Resources/blobs/blob-revert.png");
##		self.setAutoFillBackground(True);
#	def paintEvent(self):
#	    	painter=QPainter(self)
#		painter.drawPixmap(QtGui.QRectF(1, 1, 10, 10), self.pixmap, QtGui.QRectF(1,1,10,10));
#		painter.drawLine(QtGui.QLine(10,10,1,1));

class Blobber(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
	self.pixmap=QtGui.QPixmap()
	self.pixmap.load("Resources/blobs/blob-revert.png");

        self.text = u'Hola, amigos'


    def paintEvent(self, event):
        paint = QtGui.QPainter()
	line=QtCore.QLine(0,0,10,10)
        paint.begin(self)
        paint.setPen(QtGui.QColor(168, 34, 3))
#        paint.setFont(QtGui.QFont('Decorative', 10))
 #       paint.drawText(event.rect(), QtCore.Qt.AlignTop, self.text)
	print event.rect().x()
	print event.rect().y()
	paint.drawLine(line)
	paint.drawPixmap(QtCore.QRectF(0, 0, 15, 15), self.pixmap, QtCore.QRectF(0,0,15,15));
       # for i in range(1000):
       #     x = random.randint(1, size.width()-1)
  #          y = random.randint(1, size.height()-1)
 #           paint.drawPoint(x, y)
 #       paint.end()

        paint.end()
	del paint
#
#
#app = QtGui.QApplication(sys.argv)
#dt = DrawText()
#dt.show()
#app.exec_()
#
