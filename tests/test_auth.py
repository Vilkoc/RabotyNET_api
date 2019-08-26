""" Test case for sign in and sign up """
import pytest
import allure
from data_tests.auth import REGISTER_DATA, TOKEN
from utilities.db import change_varification_link
from base import LOGIN_URL, LOGOUT_URL, USER_CONFIRM_EMAIL_URL, USER_REGISTER_URL


@allure.story('Sign In')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'ROLE_ADMIN'),
    ('user@gmail.com', 'user', 'ROLE_USER'),
    ('cowner@gmail.com', 'cowner', 'ROLE_COWNER')
])
def test_login(app, user, password, expected):
    """ Test for authenticate and authorize user.
    doesn't use application method, to check auth step by step"""
    session = app.session
    response = session.post(LOGIN_URL, auth=(user, password))
    with allure.step("Check if status code equal 200"):
        assert response.status_code == 200, "Wrong status code"
    data = response.json()
    with allure.step("Check if username is correct"):
        assert data['username'] == user, "Wrong username"
    with allure.step("Check if user authorized correctly"):
        assert data['authorities'][0]['authority'] == expected, "Wrong user role"
    session.get(LOGOUT_URL)


@allure.feature('Sign Up')
def test_sign_up_begin(app):
    """ Start to register user. Up to send email """
    app.post(USER_REGISTER_URL, data=REGISTER_DATA)
    app.check_200()
    data_received = app.request.json()
    with allure.step("Check if username is correct"):
        assert data_received['login'] == REGISTER_DATA['login'], "Wrong username"


@allure.feature('Sign Up')
def test_sign_up_end(app):
    """ Finish to register user. From receive email"""
    change_varification_link(REGISTER_DATA['login'])
    app.get(USER_CONFIRM_EMAIL_URL, data=TOKEN)
    app.check_200()
    app.authentication(REGISTER_DATA['login'], REGISTER_DATA['password'])
    app.check_200()
