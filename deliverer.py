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
	def login(self,username,password):
	    	return self.lm.login(username,password)
		
	def startbot(self):
		thread.start_new_thread(self.bot.start,())
	def revert(self):
	    	print "revert!"
		revertsearch=re_revert.search(self.content)
		#TODO: Check if revert link exists
		print self.content
		reverttemp=re_amp.sub("&",revertsearch.group(1))
		revertlink="http://"+config.language+"."+config.project+".org"+reverttemp
		print revertlink
		headers = { 'User-Agent' : config.useragent, 
					'Cookie': self.lm.cookies() }
		response = urllib2.urlopen(urllib2.Request(revertlink, None, headers))

	def viewDiff(self):
		event=self.em.get()
		if event:
		    	print event.type
			
		    	if event.type == "edit":
			    	self.currevent=event
				diff=event.diff
				print "pag: "+event.page+" diff: " +  diff
				self.content=event.diffhtml
				try:
					self.visor.begin()
					self.visor.write(event.diffhtml)
					self.visor.end()
				except:
				     	print "Unexpected error"
					print event.diffhtml
	def addWhitelist(self):
	    	if self.currevent != "":
			self.em.addWhitelist(self.currevent.user)
