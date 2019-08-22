import requests
import json


MAIN_URL = 'http://localhost:8080/RabotyNET/'
HEADERS = {'content-type': 'application/json'}

class Application():
    """The parent class for all tests"""

    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        request = self.session.get(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return request

    def post(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        request = self.session.post(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return request

    def put(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        request = self.session.get(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return request

