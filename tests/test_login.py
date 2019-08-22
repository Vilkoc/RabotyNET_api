import requests
import pytest
import json
from data_tests.auth import USERNAME_SIGNUP, PASSWORD, EMAIL_SIGNUP, FROM_SIGNUP
import allure
from utilities.func import login
from utilities.db import change_varification_link, wait_user_update

TOKEN = "3e83667c-c59c-4fda-aa7a-a47346a3cd6a"

# @pytest.mark.skip
@allure.feature('Sign In')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'ROLE_ADMIN'),
    ('user@gmail.com', 'user', 'ROLE_USER'),
    ('cowner@gmail.com', 'cowner', 'ROLE_COWNER')
    ])
def test_login(app, user, password, expected):
    # session = requests.Session()
    session = app.session
    response = session.post('http://localhost:8080/RabotyNET/login', auth=(user, password))
    assert response.status_code == 200, "Wrong status code"
    data = response.json()
    assert data['username'] == user, "Wrong username"
    assert data['authorities'][0]['authority'] == expected, "Wrong user role"
    session.get('http://localhost:8080/RabotyNET/logout')

@pytest.mark.skip
def test_sign_up_begin():
    session = requests.Session()
    headers = {'content-type': 'application/json'}
    data_sent = {
      "login": USERNAME_SIGNUP,
      "matchingPassword": PASSWORD,
      "password": PASSWORD
    }

    response = session.post('http://localhost:8080/RabotyNET/users/auth', data=json.dumps(data_sent), headers=headers)

    assert response.status_code == 200, "Wrong status code"
    data_received = response.json()
    assert data_received['login'] == data_sent['login'], "Wrong username"

def test_sign_up_begin1(app):
    data_sent = {
      "login": USERNAME_SIGNUP,
      "matchingPassword": PASSWORD,
      "password": PASSWORD
    }

    response = app.post('users/auth', data=data_sent)

    assert response.status_code == 200, "Wrong status code"
    data_received = response.json()
    assert data_received['login'] == data_sent['login'], "Wrong username"

@pytest.mark.skip
def test_sign_up_end():
    session = requests.Session()
    data_sent = {"token": TOKEN}
    headers = {'content-type': 'application/json'}

    response = session.get('http://localhost:8080/RabotyNET/users/auth/confirm', data=json.dumps(data_sent), headers=headers)

    print(response.text)
    assert response.status_code == 200, "Wrong status code"
    data_received = response.json()
    print(data_received)
