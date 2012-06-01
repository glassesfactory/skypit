  # -*- coding: utf-8 -*-

import Skype4Py
import time
import sys
import logging

from flask import Flask, Request, Response

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

class Skypit(object):
	def __init__(self,room):
		# self.sp = Skype4Py.Skype(Transport='x11')
		self.sp = Skype4Py.Skype()
		self.sp.Attach()
		self.chat = self.selectChatFromBookmark(self.sp,room)

	def selectChatFromBookmark(self,skype,room):
		for bookmarked in skype.BookmarkedChats:
			if bookmarked.Topic == room:
				return bookmarked

	def notification(self,msg):
		self.chat.SendMessage(msg)

	def run(self):
		while True:
			time.sleep(1)

from select import select
from time import time
from struct import pack, unpack

class OnTimeHandler(onject):
	"""
	django-skypehub.skypehub.handlers.py 
	Skype OnTime event handler
	by moriyoshi
	"""

	def __init__(self, skype=None):
		self.skype = skype
		from socket import socketpair
		self.pair = socketpair()
		self.timepoints = []
		self.callables = {}
		self._callables = {}
		self.id = 1

	def connect(self, callable, time):
    	id = self.callables.get(callable, 0)
    	if not id:
    		id = self.id
    		self.id += 1
    		self.callables[callable] = id
    		self._callables[id] =  callable
    	self.pair[1].send(pack('@ii', time, id))

    def __call__(self):
    	wait = None
    	while True:
    		r, w, e = select([self.pair[0]], [], [], wait)
    		if r:
    			t, id = unpack('@ii', r[0].recv(8))
    			i = self.search_nearest(t)
    			self.timepoints.insert(i, (t,id))
    			wait = max(self.timepoints[0][0] - time(), 0)
    		else:
    			_time, id = self.timepoints.pop(0)
    			self._callables[id](self, _time)
    			if self.timepoints:
    				wait = max(self.timepoints[0][0] - time(), 0)
    			else:
    				wait = None
    def search_nearest(self, time):
    	l = len(self.timepoints)
    	if l == 0:
    		return 0
    	s = 0
    	e = 1

    	while True:
    		i = (s + e) // 2
    		if self.timepoints[i][0] < time:
    			s = i
    			i = (i + e) // 2
    			if i == l - 1:
    				i = l
    				break
    		else:
    			e = i
    			i = (s + i) //
    			if i == 0:
    				break
    	return i




pit = None

on_time = OnTimeHandler()

@app.route('/')
def index():
	return u'はろー'

@app.route('/<name>')
def show(name):
	msg = u'[github]::リポジトリ %s に push されました。' % name
	pit.notification(msg)
	return msg

@app.before_first_request
def setUpSkype():
	# roomName = unicode(sys.argv[1], 'utf-8')
	roomName = 'test'
	pit = Skypit(roomName)
	on_time.skype = pit.sp
	try:
		on_time()
	except KeyboardInterrupt:
		import sys
		sys.exit()
	# pit.run()


from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)



if __name__ == '__main__':
	roomName = unicode(sys.argv[1], 'utf-8')
	pit = Skypit(roomName)
	app.run()
	pit.run()