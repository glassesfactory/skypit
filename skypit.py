# -*- coding: utf-8 -*-

import Skype4Py
import time
import sys

from flask import Flask,

app = Flask(__name__)

class Skypit(object):
	def __init__(self,room):
		self.sp = Skype4Py.Skype(Transport='x11')
		self.sp.Attach()
		self.chat = self.selectChatFromBookmark(self.sp,room)

	def selectChatFromBookmark(self,skype,room):
		for bookmarked in skype.BookMarkedChats:
			if bookmarked.Topic == topic:
				return chat

	def notification(self,msg):
		self.chat.SendMessage(msg)

	def run(self):
		while True:
			time.sleep(1)

pit = None

@app.rout('/<path:name>')
def show(name):
	msg = u'リポジトリ' + name + u'に push されました。'
	pit.notification(msg)

if __name__ == '__main__':
	roomName = uicode(sys.args[1], 'utf-8')
	pit = Skypit(roomName)
	pit.run()
	app.run()