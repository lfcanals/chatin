import requests

class ChatGPTClient:
    def  __init__(self, host):
        self.query_url = host + '/chatin/api/v1.0/query'


    def query(self, text):
        jsonMessage = {'message': text}
        response = requests.post(self.query_url, json = jsonMessage)
        return response.json()[0]['message']

