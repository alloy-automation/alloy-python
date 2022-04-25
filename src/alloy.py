from ast import While
from itertools import count
from urllib import request
import requests
import uuid

def run_alloy(apiKey="",workflowId = "",data = {},returnExecutionData = False):
	executionUuid = uuid.uuid4()
	data = {}
	session = requests.Session()
	print("Running",apiKey,workflowId)
	session.headers.update({'Authorization': 'Bearer '+apiKey})
	session.headers.update({'X-Execution-Uuid': "{executionUuid}"})
	print(executionUuid)
	response = session.post('https://webhooks.runalloy.com/'+workflowId, data)
	print("response",response.status_code)
	if response.status_code == 401:
		raise Exception("Not authorized to runalloy")

	if response.status_code == 400:
		raise Exception("Execution failed due to some internal error")
	
	if returnExecutionData == False:
		print("Go for execution data")
		isExecutionDone = ''
	try:
		i = 1
		while i < 10:
			pollResult = session.get("https://api.runalloy.com/sdk/output/{executionUuid}")
			print(pollResult.json())
			if pollResult and pollResult.data and pollResult.data.output:
				return pollResult.data
			elif i < 10:
				i += 1
			else:
				raise Exception("Timeout waiting for output")
	except:
		raise Exception("Could not find output")