# -*- coding: utf-8 -*-

import Skype4Py
import time
import sys

class Skypit(object):
	def __init__(self):
		self.sp = Skype4Py.Skype(Transport='x11')
		self.sp.Attach()

	def run(self):
		while True:
			time.sleep(1)

		# self.sp.OnMessageStatus = self.

if __name__ == '__main__':
	roomName = uicode(sys.args[1], 'utf-8')
	pit = Skypit()
	pit.run()