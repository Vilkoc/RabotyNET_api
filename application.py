import requests
import json
from base import LOGIN_URL, BASE_URL

HEADERS = {'content-type': 'application/json'}

class Application():
    """The parent class for all tests"""

    def __init__(self):
        self.session = requests.Session()

    def authentication(self, username, password):
        self.request = self.session.post(LOGIN_URL, auth=(username, password))
        if self.request.status_code == 200:
            self.get(BASE_URL)
            self.session.headers.update({"X-XSRF-TOKEN": self.session.cookies.get_dict()['XSRF-TOKEN'],
                                         "XSRF-TOKEN": self.session.cookies.get_dict()['XSRF-TOKEN']})
        return self.request

    def get(self, endpoint, data='', headers=HEADERS):
        # converted_data = json.dumps(data)
        self.request = self.session.get(endpoint, params=data, headers=headers)
        return self.request

    def post(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        self.request = self.session.post(endpoint, data=converted_data, headers=headers)
        return self.request

    def put(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        self.request = self.session.put(endpoint, data=converted_data, headers=headers)
        return self.request

    def delete(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        self.request = self.session.delete(endpoint, data=converted_data, headers=headers)
        return self.request

    def debug_info(self):
        print(self.request.status_code, '\n', self.request.text)
        from pprint import pprint
        pprint(self.request.json())
