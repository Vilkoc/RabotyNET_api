"""This module allows sending resume"""
import allure
from base import SEND_RESUME_URL
from credentials import Credentials
from data_tests.user_data import USER_RESUME


@allure.feature('Send resume test')
def test_send_resume(app):
    """Sending users resume"""

    with allure.step('Login'):
        app.authentication(*Credentials['USER'])

    with allure.step('Sending resume'):
        app.post(SEND_RESUME_URL, data=USER_RESUME)

    with allure.step('Checking result'):
        assert app.request.status_code == 200
