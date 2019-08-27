""" This module allows you create claim to company """
import allure
from credentials import Credentials
from base import COMPANY_GET_CLAIM_URL, CREATE_CLAIM_URL, GET_USER_ADMIN_INFO
from data_tests.admin_data import CREATE_CLAIM_DATA, ASSERT_BY_TITLE, CLAIM_TITLE


def test_api_admin_create_claim(app):
    """ Test that create claim to company """
    with allure.step("Login"):
        app.authentication(*Credentials['ADMIN'])
    with allure.step('Create Claim to company'):
        app.session.get(GET_USER_ADMIN_INFO)
        app.post(CREATE_CLAIM_URL, CREATE_CLAIM_DATA)
    with allure.step('Check if claim created'):
        response = app.get(COMPANY_GET_CLAIM_URL)
        assert response.json()[0][ASSERT_BY_TITLE] == CLAIM_TITLE
    with allure.step('Checking result'):
        assert app.request.status_code == 200
