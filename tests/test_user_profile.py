""" User Profile test"""

import pytest
from data_tests.auth import REGISGER_DATA, TOKEN
from base import LOGIN_URL, LOGOUT_URL, USER_CONFIRM_EMAIL_URL, USER_REGISTER_URL
import allure
from utilities.db import change_varification_link, wait_user_update
from credentials import Credentials

@allure.feature('Sign In')
def test_user_profile(app):
    response = app.authentication(*Credentials['USER'])
    assert response.status_code == 200, "Wrong status code"
