""" T This module allows you unblock company """
import allure
import pytest
from base import UPDATE_COMPANY_URL
from data_tests.admin_data import UNBLOCK_COMPANY_DATA


@pytest.skip(reason='skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
def test_api_admin_unblock_co(app):
    """ Test that unblock company """
    with allure.step("Login"):
        app.authentication('admin@gmail.com', 'admin')
    with allure.step('Create Claim to company'):
        response = app.put(UPDATE_COMPANY_URL, UNBLOCK_COMPANY_DATA)
        assert 'APPROVED' == response.json()[0]['status']
    app.check_200()

