import requests
import json


MAIN_URL = 'http://localhost:8080/RabotyNET/'
HEADERS = {'content-type': 'application/json'}

class Application():
    """The parent class for all tests"""

    def __init__(self):
        self.session = requests.Session()

    def authentication(self, login, password):
        self.request = self.session.post(MAIN_URL+'login', auth=(login, password))
        if self.request.status_code == 200:
            self.get('')
            self.session.headers.update({"X-XSRF-TOKEN": self.session.cookies.get_dict()['XSRF-TOKEN'],
                                         "XSRF-TOKEN": self.session.cookies.get_dict()['XSRF-TOKEN']})
        return self.request

    def get(self, endpoint, data='', headers=HEADERS):
        # converted_data = json.dumps(data)
        self.request = self.session.get(MAIN_URL+endpoint, params=data, headers=headers)
        return self.request

    def post(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        self.request = self.session.post(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return self.request

    def put(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        self.request = self.session.put(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return self.request

    def delete(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        self.request = self.session.delete(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return self.request

    def debug_info(self):
        print(self.request.status_code, '\n', self.request.text)
        from pprint import pprint
        pprint(self.request.json())
