Python34-GCM
======================
Python3.4 push server for Google Cloud Messaging for Android(GCM)


Installation
-------------
.. code-block:: bash

   pip install requests


Example
------------
android.pem

.. code-block:: bash
	
	API_Key

example.py

.. code-block:: python

	from GCM import *

	class Test(object):

		def __init__(self):
			self.gcm = GCM()

		def sendGCM(self, registration_ids, message):
			return self.gcm.sendMessage(registration_ids, message)

	if __name__ == '__main__':
		test = Test()
		registration_ids = ["registration_ids"]
		data = {"message":"test"}
		return_data = test.sendGCM(registration_ids,data)
		print(return_data)