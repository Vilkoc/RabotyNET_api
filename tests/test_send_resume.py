import requests

session = requests.Session()
user_data = ("user@gmail.com", "user")


def test_change_data():
    login = session.post('http://localhost:8080/RabotyNET/login', auth=user_data)
    change = session.get('http://localhost:8080/RabotyNET/pdf/sendEmail')

    print(change.status_code)