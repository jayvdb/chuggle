#!/usr/bin/python
# -*- coding: utf-8  -*-

from PyKDE4.khtml import KHTMLPart, KHTMLView
import thread, urllib2, re

import panbot, config, login, soliddata, events

re_revert =re.compile(ur"<span class=\"mw-rollback-link\">\[<a href=\"([^\"]*)\"")
re_amp    =re.compile(ur"&amp;")



class Dv:
    def __init__ (self, visor, conn):
        #reference to  our KHTMLPart
        self.visor=visor
        #connector
        self.conn=conn
        #login manager initialization
        self.lm=login.LoginManager()
        #Event manager
        self.em=events.EventManager(self.conn,self.lm)
        #bot stuff
        self.bot=panbot.PanBot("#"+config.language+"."+config.project,self.em, self.conn)

        self.title=""
        self.content=""
        self.currevent=""
        self.event=""
    def login(self,username,password):
        return self.lm.login(username,password)

    def startbot(self):
        thread.start_new_thread(self.bot.start,())

    def rollback(self):
        print "rollback!"
        revertsearch = re_revert.search(self.content)
        #Check if rollback link exists
        if (revertsearch):
            reverttemp = re_amp.sub("&",revertsearch.group(1))
            rollbacklink = reverttemp
            headers = { 'User-Agent' : config.useragent, 
                'Cookie': self.lm.cookies() }
            try:
                response = urllib2.urlopen(urllib2.Request(rollbacklink, None, headers))
                self.conn.sendSignal("writeMsgBox", "edit by "+self.event.user.decode('utf-8')+ " in "+self.event.page.decode('utf-8')+" reverted")
                #Go to next diff
                self.viewDiff()

            except:
                print "Error reverting"

    def viewDiff(self):
        event = self.em.get()
        self.event = event
        if event:
            if event.type == "edit":
                self.currevent=event
                diff=event.diff
                self.content=event.diffhtml
                try:
                    self.visor.begin()
                    self.visor.write(event.diffhtml)
                    self.visor.end()
                    self.conn.sendSignal("writeMsgBox", "edit in "+self.event.page.decode('utf-8'))
                except:
                    print "Error showing diff"
                    print event.diffhtml
    def addWhitelist(self):
        if self.currevent != "":
            self.em.addWhitelist(self.currevent.user)
            self.viewDiff()
