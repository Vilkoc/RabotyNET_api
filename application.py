import requests
import json


MAIN_URL = 'http://localhost:8080/RabotyNET/'
HEADERS = {'content-type': 'application/json'}

class Application():
    """The parent class for all tests"""

    def __init__(self):
        self.session = requests.Session()

    def authentication(self, login, password):
        request = self.session.post(MAIN_URL+'login', auth=(login, password))
        if request.status_code == 200:
            self.get('')
            self.session.headers.update({"X-XSRF-TOKEN": self.session.cookies.get_dict()['XSRF-TOKEN'],
                                         "XSRF-TOKEN": self.session.cookies.get_dict()['XSRF-TOKEN']})
            return request
        raise Exception("Status code isn't 200")

    def get(self, endpoint, data='', headers=HEADERS):
        # converted_data = json.dumps(data)
        request = self.session.get(MAIN_URL+endpoint, params=data, headers=headers)
        return request

    def post(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        request = self.session.post(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return request

    def put(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        request = self.session.get(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return request

    def delete(self, endpoint, data='', headers=HEADERS):
        converted_data = json.dumps(data)
        request = self.session.get(MAIN_URL+endpoint, data=converted_data, headers=headers)
        return request
