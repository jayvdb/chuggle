#! /usr/bin/env python

from ircbot import SingleServerIRCBot
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr
import random
import re, os
import config

import events

re_diff=re.compile(r"http://[^ ]*")


class PanBot(SingleServerIRCBot):
    def __init__(self, channel, eventmanager, conn):
	self.conn=conn
        self.channel = channel
        self.nickname = "pan"+ repr(random.randint(1000,9999))
	self.port = 6667
    	self.server = "browne.wikimedia.org"
        SingleServerIRCBot.__init__(self, [(self.server, self.port)], self.nickname, self.nickname)
	self.buffer=[]
	self.em=eventmanager
    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)
        self.conn.sendSignal("writeMsgBox", "bot connected")

    def on_pubmsg(self, c, e):
	self.em.addEvent(events.Event(e.arguments()[0]))
        return

def main():
    import sys
    channel = config.channel

    bot = PanBot(channel)
    bot.start()

if __name__ == "__main__":
    main()
