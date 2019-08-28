"""This module allows sending resume"""
import allure
import pytest
from base import SEND_RESUME_URL, GENERATE_RESUME, RESUME_DATA
from credentials import Credentials


@allure.feature('Send resume test')
def test_send_resume(app):
    """Sending users resume"""

    with allure.step('Login'):
        app.authentication(*Credentials['USER'])

    with allure.step('Getting resume data'):
        app.get(GENERATE_RESUME)
        resume = app.get(RESUME_DATA).json()

    with allure.step('Sending resume'):
        app.post(SEND_RESUME_URL, data=resume)

    with allure.step('Checking result'):
        assert app.request.status_code == 200
