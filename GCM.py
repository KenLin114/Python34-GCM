# -*- coding: utf-8 -*-
import json,requests

class GCM(object):

	def __init__(self):
		self.url = "http://android.googleapis.com/gcm/send"

	def readAPIkey(self):
		f = open("android.pem")
		api_key = f.readline()
		f.close()
		return 'key='+api_key

	def data2json(self, regId, data):
		params = {"registration_ids":regId,"data":data}
		params = json.JSONEncoder().encode(params)
		return params

	def sendMessage(self, registration_ids, message):
	#	
	# Args:
	#	param1 (list of str): Android GCM registration_ids
	#	param2 (jsonObject) : send jsonObject
	#
		data = self.data2json(registration_ids, message)
		headers = { 'content-type':'application/json',
					'Authorization':self.readAPIkey()}
		r = requests.post(self.url,headers=headers,data=data)
		return r.text

if __name__ == '__main__':
	gcm = GCM()