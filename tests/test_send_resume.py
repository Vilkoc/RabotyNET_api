"""This module allows sending resume"""
import allure
from base import SEND_RESUME_URL
from credentials import Credentials
from data_tests.user_data import user_resume


@allure.feature('Send resume test')
def test_send_resume(app):
    """Sending users resume"""

    with allure.step('Login'):
        app.authentication(*Credentials['USER'])

    with allure.step('Sending resume'):
        app.post(SEND_RESUME_URL, data=user_resume)

    app.check_200()
