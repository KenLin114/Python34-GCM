# -*- coding: utf-8 -*-

from GCM import *

class Test(object):

	def __init__(self):
		self.gcm = GCM()

	def sendGCM(self, registration_ids, message):
		print(self.gcm.sendMessage(registration_ids, message))

if __name__ == '__main__':
	test = Test()
	
	registration_ids = ["APA91bHDN6v1KqjU6nK3aGjV9EMNnoCcxA20OVjS7LGb0r7h2-UdpcY0Iw2PWc0oC2m21SqbIx3ptzrHZ8b09JpAOxv2pvMHhSTzWQ-mnJiAwixOzF_vTEPPxAkux0dfUuZfC-S2sgiyKaNgXRtBRHe7iyLArYqo8Q"]
	data = {"message":"test"}
	test.sendGCM(registration_ids,data)
