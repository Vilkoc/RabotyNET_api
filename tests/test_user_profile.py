""" User Profile test"""
import allure
from base import USER_PROFILE_URL, USER_URL
from credentials import Credentials
from data_tests.user_data import UPDATE_DATA


@allure.feature('Getting user data')
def test_user_profile_get(app):
    """Checking if user profile info is extracted"""
    with allure.step('Sign in and get user profile info'):
        app.authentication(*Credentials['USER'])
        response_after_get = app.get(USER_PROFILE_URL)
        assert response_after_get.status_code == 200, "Wrong status code"


@allure.feature('Updating user data')
def test_user_profile_update(app):
    """Checking if user profile info is updated"""
    with allure.step('Sign in and update user profile'):
        app.authentication(*Credentials['USER'])
        response_after_put = app.put(USER_URL, data=UPDATE_DATA)
        assert response_after_put.status_code == 200, "Wrong status code"
