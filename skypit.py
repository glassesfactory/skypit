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

pit = None

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
	pit.run()

from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)



if __name__ == '__main__':
	roomName = unicode(sys.argv[1], 'utf-8')
	pit = Skypit(roomName)
	app.run()
	pit.run()