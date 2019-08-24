""" User Profile test"""
from base import USER_PROFILE_URL, USER_URL
import allure
from credentials import Credentials
from data_tests.user_data import updated_data

@allure.feature('Getting user data')
def test_user_profile_get(app):
    with allure.step('Sign in and get user profile info'):
        app.authentication(*Credentials['USER'])
        response_after_get = app.get(USER_PROFILE_URL)
        assert response_after_get.status_code == 200, "Wrong status code"


@allure.feature('Updating user data')
def test_user_profile_update(app):
    with allure.step('Sign in and update user profile'):
        app.authentication(*Credentials['USER'])

        response_after_put = app.put(USER_URL, data=updated_data)
        assert response_after_put.status_code == 200, "Wrong status code"

