""" This module allows you to get all companies """
import allure
from credentials import Credentials
from base import ALL_COMPANIES_URL,
from data_tests.admin_data import ASSERT_BY_NAME, NAME_OF_COMPANIES


def test_api_admin_companies_presence(app):
    """ Test that get all companies"""
    with allure.step("Login"):
        app.authentication(*Credentials['ADMIN'])
    with allure.step('Check if companies present'):
        response = app.get(ALL_COMPANIES_URL)
        assert NAME_OF_COMPANIES[0] == response.json()[0][ASSERT_BY_NAME]
        assert NAME_OF_COMPANIES[1] == response.json()[1][ASSERT_BY_NAME]
        assert NAME_OF_COMPANIES[2] == response.json()[2][ASSERT_BY_NAME]
    with allure.step('Checking result'):
        assert app.request.status_code == 200
