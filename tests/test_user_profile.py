""" User Profile test"""
from base import USER_PROFILE_URL, USER_URL, LOGOUT_URL
import allure
from credentials import Credentials
from data_tests.user_data import updated_data


@allure.feature('Getting user data')
def test_user_profile_get(app):
    """Checking if user profile info is extracted"""
    with allure.step('Sign in and get user profile info'):
        app.authentication(*Credentials['USER'])
        app.get(USER_PROFILE_URL)
        assert app.request.status_code == 200, "Wrong status code"
        app.get(LOGOUT_URL)

@allure.feature('Updating user data')
def test_user_profile_update(app):
    """Checking if user profile info is updated"""
    with allure.step('Sign in and update user profile'):
        app.authentication(*Credentials['USER'])
        app.put(USER_URL, data=updated_data)
        assert app.request.status_code == 200, "Wrong status code"
        app.get(LOGOUT_URL)


