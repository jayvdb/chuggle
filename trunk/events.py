#!/usr/bin/python
# -*- coding: utf-8  -*-

import urllib2, re
import connector
import config
import soliddata

re_inidiff=re.compile(ur"<table class='diff'>")
re_enddiff=re.compile(ur"</table>")
re_title  =re.compile("var wgTitle = \"([^\"]*)\";")


re_edit=re.compile(ur"14\[\[07(?P<page>[^\]]*)14\]\]4 (?P<flags>\w*)10 02(?P<diff>http://\S*) 5\* 03(?P<user>[^]+) 5\* \((?P<bytes>[^\)]*)\) 10(?P<summary>.*)$")
re_newuser=re.compile(ur"14\[\[07Especial:Log/newusers14\]\]4 create10 02 5\* 03(?P<user>[^]+) 5\*  10(?P<summary>.*)$")
re_upload=re.compile(ur"\[\[Special:Log/upload\]\] upload  \* (?P<user>[^]\S+) \*  uploaded \"\[\[(?P<page>[^\]]*)\]\]\": (?P<summary>.*)$")
re_delete=re.compile(ur"\[\[Special:Log/delete\]\] delete  \* (?P<user>[^]+) \*  deleted \"\[\[(?P<page>[^\]]*)\]\]\": (?P<summary>.*)$")
re_move=re.compile(ur"14\[\[07Special:Log\/move14\]\]4 move10 02 5\* 03(?P<user>[^]+) 5\*  moved \[\[(?P<page>[^\]]*)\]\] to \[\[(?P<destiny>[^\]]*)\]\]: (?P<summary>.*)$")
re_move_redir=re.compile(ur"\[\[Special:Log\/move\]\] move_redir  \* (?P<user>[^]+) \*  moved \[\[(?P<page>[^\]]*)\]\] to \[\[(?P<destiny>[^\]]*)\]\] over redirect: (?P<summary>.*)$")
re_overwrite=re.compile(ur"\[\[Special:Log/upload\]\] overwrite  \* (?P<user>[^]\S+) \*  uploaded a new version of \"\[\[(?P<page>[^\]]*)\]\]\"$")
re_protect=re.compile(ur"\[\[Special:Log/protect\]\] protect  \* (?P<user>[^]+) \*  protected (?P<summary>.*)")
re_try=re.compile(ur"")



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
		self.reverted = 0
	
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
		self.computed=0
		self.conn=conn
		self.lm=lm
	def addEvent(self,event):
		if event.user in self.whitelist:
		    	print event.user+" in WL"
			return
		if event.type=="edit":
			self.events.append(event)
			diff=event.diff
			headers = { 'User-Agent' : config.useragent, 
				'Cookie': self.lm.cookies() }
			try:
				response = urllib2.urlopen(urllib2.Request(diff, None, headers))
			except:
				print "Unable to get diff"	
			html = response.read()
			self.title=event.page
			self.content=soliddata.cssdiff+"<h1>"+self.title+"</h1>"+"<table class=\"diff\">"+re_inidiff.split(html)[1]
			event.diffhtml=re_enddiff.split(self.content)[0]+"</table><body></html>"

		self.conn.sendSignal("setNumItems", self.length())
	def delEvent(self,num=0):
		if num == 0:
			self.events=self.events[1:]
		else:
			self.events=self.events[:num].extend(self.events[num+1:])
	def clear(self):
	    	self.events=[]
	def length(self):
	    	return len(self.events)
	def get(self, num=0):
		if self.length()>num:
			toreturn = self.events[num]
		    	self.delEvent()
			self.conn.sendSignal("setNumItems", self.length())
	    		return toreturn
		else:
		    	return None
	def addWhitelist(self, user):
		if user not in self.whitelist:
		    self.whitelist.append(user)
		    self.conn.sendSignal("writeMsgBox","User "+user+" added to whitelist")


		
