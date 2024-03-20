import requests

def ChatGTPClient:
    def  __init__(self, host):
        self.query_url = host + '/chatin/api/v1.0/query'


    def query(self, text):
        jsonMessage = {'message': text}
        response = request.post(self.query_url, json = jsonMessage)
        return response

