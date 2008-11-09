#!/usr/bin/python
# -*- coding: utf-8  -*-

from PyKDE4.khtml import KHTMLPart, KHTMLView
import thread, urllib2, re

import panbot, config, login, soliddata, events

re_inidiff=re.compile(ur"<table class='diff'>")
re_enddiff=re.compile(ur"</table>")
re_revert =re.compile(ur"<span class=\"mw-rollback-link\">\[<a href=\"([^\"]*)\"")
re_amp    =re.compile(ur"&amp;")
re_title  =re.compile("var wgTitle = \"([^\"]*)\";")


class Dv:
	def __init__ (self, visor):
	    	#reference to  our KHTMLPart
		self.visor=visor
		#Event manager
		self.em=events.EventManager()
		#bot stuff
		self.bot=panbot.PanBot("#"+config.language+"."+config.project,self.em)
		thread.start_new_thread(self.bot.start,())
		#login manager initialization
		self.lm=login.LoginManager()
		self.lm.login()

		self.title=""
		self.content=""

	def revert(self):
	    	print "revert!"
		revertsearch=re_revert.search(self.content)
		#TODO: Check if revert link exists
		reverttemp=re_amp.sub("&",revertsearch.group(1))
		revertlink="http://"+config.language+"."+config.project+".org"+reverttemp
		print revertlink
		headers = { 'User-Agent' : config.useragent, 
					'Cookie': self.lm.cookies() }
		response = urllib2.urlopen(urllib2.Request(revertlink, None, headers))

	def viewDiff(self):
		event=self.em.get()
		if event:
		    	if event.type == "edit":
				diff=event.diff
				print "Getting diff"
				headers = { 'User-Agent' : config.useragent, 
					'Cookie': self.lm.cookies() }
				response = urllib2.urlopen(urllib2.Request(diff, None, headers))
				html = response.read()
				title=re_title.search(html)
				self.title=title.group(1)
				self.content=soliddata.cssdiff+"<h1>"+self.title+"</h1>"+"<table class=\"diff\">"+re_inidiff.split(html)[1]
				self.content=re_enddiff.split(self.content)[0]+"</table><body></html>"
				self.visor.begin()
				self.visor.write(self.content)
				self.visor.end()

	
