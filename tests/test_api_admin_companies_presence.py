""" This module allows you to get all companies """
import allure
from credentials import Credentials
from base import ALL_COMPANIES_URL


def test_api_admin_companies_presence(app):
    """ Test that get all companies"""
    with allure.step("Login"):
        app.authentication(*Credentials['ADMIN'])
    with allure.step('Check if companies present'):
        response = app.get(ALL_COMPANIES_URL)
        assert 'SoftServe' == response.json()[0]['name']
        assert 'InventorSoft' == response.json()[1]['name']
        assert 'ValSoft' == response.json()[2]['name']
    with allure.step('Checking result'):
        assert app.request.status_code == 200
