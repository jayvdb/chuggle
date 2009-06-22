# -*- coding: utf-8  -*-

# A simple connector. It calls functions of other objects registered
#usage example:
#def a():
#    print "hola"
#
#def b(*args):
#    print args[0]
#    
#def c():
#    conn.sendSignal("A")
#    conn.sendSignal("B","hola")
#
#conn=Connector()
#conn.register(a,"A")
#conn.register(b,"B")
#c()

    

class Connector:
    def __init__ (self):
        self.signals={}
    def register(self, procedure, name):
        self.signals[name]=procedure;
    def sendSignal(self, name, *args):
        self.signals[name](*args)

global conn
conn=Connector()
