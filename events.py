#!/usr/bin/python
# -*- coding: utf-8  -*-

import re
re_edit=re.compile(ur"14\[\[07(?P<page>[^\]]*)14\]\]4 (?P<flags>\w*)10 02(?P<diff>http://\S*) 5\* 03(?P<user>\S+) 5\* \((?P<bytes>[^\)]*)\) 10(?P<summary>.*)$")
re_newuser=re.compile(ur"14\[\[07Especial:Log/newusers14\]\]4 create10 02 5\* 03(?P<user>\S+) 5\*  10(?P<summary>.*)$")
re_upload=re.compile(ur"\[\[Special:Log/upload\]\] upload  \* (?P<user>\S+) \*  uploaded \"\[\[(?P<page>[^\]]*)\]\]\": (?P<summary>.*)$")
re_delete=re.compile(ur"\[\[Special:Log/delete\]\] delete  \* (?P<user>\S+) \*  deleted \"\[\[(?P<page>[^\]]*)\]\]\": (?P<summary>.*)$")
re_move=re.compile(ur"\[\[Special:Log\/move\]\] move  \* (?P<user>\S+) \*  moved \[\[(?P<page>[^\]]*)\]\] to \[\[(?P<destiny>[^\]]*)\]\]: (?P<summary>.*)$")
re_move_redir=re.compile(ur"\[\[Special:Log\/move\]\] move_redir  \* (?P<user>\S+) \*  moved \[\[(?P<page>[^\]]*)\]\] to \[\[(?P<destiny>[^\]]*)\]\] over redirect: (?P<summary>.*)$")
re_overwrite=re.compile(ur"\[\[Special:Log/upload\]\] overwrite  \* (?P<user>\S+) \*  uploaded a new version of \"\[\[(?P<page>[^\]]*)\]\]\"$")
re_protect=re.compile(ur"\[\[Special:Log/protect\]\] protect  \* (?P<user>\S+) \*  protected (?P<summary>.*)")
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
			self.type = "edit"  
			self.page = edit.group("page")
			self.flags = edit.group("flags")
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
		    print line
	
    
class EventManager:
	def __init__(self):
		self.events=[]
		self.computed=0
	def addEvent(self,event):
		self.events.append(event)
		print "Events in queue " + repr(self.length())
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
	    		return toreturn
		else:
		    	return None


		
