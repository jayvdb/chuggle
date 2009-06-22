#!/usr/bin/python
# -*- coding: utf-8  -*-

import urllib2, re
import connector
import config
import soliddata

re_inidiff=re.compile(ur"<table class='diff'>")
re_enddiff=re.compile(ur"</table>")
re_title  =re.compile("var wgTitle = \"([^\"]*)\";")

re_local=re.compile("href=\"/")
re_local1=re.compile("href='/")

re_edit=re.compile(ur"14\[\[07(?P<page>[^\]]*)14\]\]4 (?P<flags>\w*)10 02(?P<diff>http://\S*) 5\* 03(?P<user>[^]+) 5\* \((?P<bytes>[^\)]*)\) 10(?P<summary>.*)$")
re_newuser=re.compile(ur"14\[\[07Especial:Log/newusers14\]\]4 create10 02 5\* 03(?P<user>[^]+) 5\*  10(?P<summary>.*)$")
re_upload=re.compile(ur"\[\[Special:Log/upload\]\] upload  \* (?P<user>[^]\S+) \*  uploaded \"\[\[(?P<page>[^\]]*)\]\]\": (?P<summary>.*)$")
re_delete=re.compile(ur"\[\[Special:Log/delete\]\] delete  \* (?P<user>[^]+) \*  deleted \"\[\[(?P<page>[^\]]*)\]\]\": (?P<summary>.*)$")
re_move=re.compile(ur"14\[\[07Special:Log\/move14\]\]4 move10 02 5\* 03(?P<user>[^]+) 5\* moved \[\[(?P<page>[^\]]*)\]\] to \[\[(?P<destiny>[^\]]*)\]\]: (?P<summary>.*)$")
re_move_redir=re.compile(ur"\[\[Special:Log\/move\]\] move_redir  \* (?P<user>[^]+) \*  moved \[\[(?P<page>[^\]]*)\]\] to \[\[(?P<destiny>[^\]]*)\]\] over redirect: (?P<summary>.*)$")
re_overwrite=re.compile(ur"\[\[Special:Log/upload\]\] overwrite  \* (?P<user>[^]\S+) \*  uploaded a new version of \"\[\[(?P<page>[^\]]*)\]\]\"$")
re_protect=re.compile(ur"\[\[Special:Log/protect\]\] protect  \* (?P<user>[^]+) \*  protected (?P<summary>.*)")
re_try=re.compile(ur"")


#Describes an event received from the IRC bot
class Event:
    def __init__ (self,line):
        self.type = ""
        self.page = ""
        self.flags = ""
        self.diff = ""
        self.user = ""
        self.bytes = ""
        self.summary = ""
        self.destiny = ""
        self.diffhtml = ""
        self.whitelisted = False
        self.id=-1
        
        edit=re_edit.search(line)
        newuser=re_newuser.search(line)
        upload=re_upload.search(line)
        delete=re_delete.search(line)
        move=re_move.search(line)
        move_redir=re_move_redir.search(line)
        overwrite=re_overwrite.search(line)
        protect=re_protect.search(line)
        
        if edit: 
            self.flags = edit.group("flags")
            if "N" in self.flags:
                self.type="newpage"
            else:
                self.type = "edit"  
            
            self.page = edit.group("page")
            self.diff = edit.group("diff")
            self.user = edit.group("user")
            self.bytes = edit.group("bytes")
            self.summary = edit.group("summary")
            
            self.diffhtml = 0
        
        elif newuser:
            print "newuser"
        elif upload:
            print "upload"
        elif delete:
            print "delete"
        elif move:
            print "move"
        elif move_redir:
            print "move_redir"
        elif overwrite:
            print "overwrite"
        elif protect:
            print "protect"
        else:
            print "unknow event :"+ line
    
class EventManager:
    def __init__(self,conn,lm):
        self.whitelist=[]
        self.events=[]
        self.users={}
        self.pages={}
        self.computed=0
        self.queue=0
        self.conn=conn
        self.lm=lm
    #loads a diff
    def loadDiff(self, difflink, title):
        headers = { 'User-Agent' : config.useragent, 
            'Cookie': self.lm.cookies() }
        #We try to load the diff
        try:
            response = urllib2.urlopen(urllib2.Request(difflink, None, headers))
            html = response.read()
        except:
            print "Unable to get diff"
        #Get only the diff code and attach our css
        inidiff=re_inidiff.search(html)
        if not inidiff:
            return -1
        self.content=soliddata.cssdiff+"<h1>"+title+"</h1><div id=\"bodyContent\"><table class=\"diff\">"+re_inidiff.split(html)[1]
        endiff=re_enddiff.search(self.content)
        if not endiff:
            return -1
        diffhtml=re_enddiff.split(self.content)[0]+"</table></div><body></html>"
        #convert relative links to absolute
        diffhtml=re_local.sub("href=\"http://"+config.language+"."+config.project+".org/",diffhtml)
        diffhtml=re_local1.sub("href='http://"+config.language+"."+config.project+".org/",diffhtml)
        return diffhtml
    
    #enqueues the event
    def addEvent(self,event):
        if event.type=="edit":
            event.diffhtml=self.loadDiff(event.diff,event.page)
            #check if it succeeded
            if event.diffhtml == -1:
                return
        else:
            return
        event.id=self.length()
        if event.user not in self.users:
            self.users[event.user]=[event.id]
        else:
            self.users[event.user].append(event.id)
        if event.page not in self.pages:
            self.pages[event.page]=[event.id]
        else:
            self.pages[event.page].append(event.id)
        if event.user in self.whitelist:
            event.whitelisted = True
        else:
            self.queue=self.queue+1
        self.events.append(event)
        #update counter
        self.conn.sendSignal("setNumItems", self.queue)
    def delEvent(self,num=0):
        if num == 0:
            self.events=self.events[1:]
        else:
            self.events=self.events[:num].extend(self.events[num+1:])
    def clear(self):
        self.events=[]
    def length(self):
        return len(self.events)
    def get(self, num=-1):
        if num <0:
            num=self.computed
        if self.length()>num:
            user=self.events[num].user
            self.computed=self.computed+1
            if user not in self.whitelist:
                toreturn = self.events[num]
                self.queue=self.queue-1
                self.conn.sendSignal("setNumItems", self.queue)
                return toreturn
            else:
                return self.get()
        else:
            return None
    def addWhitelist(self, user):
        if user not in self.whitelist:
            self.whitelist.append(user)
            self.conn.sendSignal("writeMsgBox","User "+user+" added to whitelist")
            for event in self.events:
                if event.user == user:
                    self.events[event.id].whitelisted = True
                    if event.id > self.computed:
                        self.queue = self.queue - 1
        self.conn.sendSignal("setNumItems", self.queue)
    
    
