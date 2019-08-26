"""This module allows you unblock company """
import allure
import pytest
from credentials import Credentials
from base import UPDATE_COMPANY_URL
from data_tests.admin_data import UNBLOCK_COMPANY_DATA


@pytest.mark.skip(reason='skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
def test_api_admin_unblock_co(app):
    """ Test that unblock company """
    with allure.step("Login"):
        app.authentication(*Credentials['ADMIN'])
    with allure.step('Create Claim to company'):
        response = app.put(UPDATE_COMPANY_URL, UNBLOCK_COMPANY_DATA)
        assert 'APPROVED' == response.json()[0]['status']
    with allure.step('Checking result'):
        assert app.request.status_code == 200
