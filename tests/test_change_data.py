"""This module allows changing data in user resume"""
import allure
from base import RESUME_URL
from credentials import Credentials
from data_tests.user_data import user_resume


@allure.feature('Changing data in user resume')
def test_change_data(app):
    """Changing data in user resume"""

    with allure.step('Login'):
        app.authentication(*Credentials['USER'])

    with allure.step('Changing data'):
        app.put(RESUME_URL, data=user_resume)

    app.check_200()