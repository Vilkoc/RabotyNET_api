"""This module allows you to update the company name"""
import allure
from data_tests.cowner_data import UPDATE_COMPANY_NAME_DATA, UPDATED_NAME
from base import UPDATE_COMPANY_URL


@allure.feature('Updating of the company name')
def test_update_company_name(app):
    """Updating of the company name"""

    with allure.step("Login"):
        app.authentication("cowner@gmail.com", "cowner")
    with allure.step("Updating company name"):
        app.put(UPDATE_COMPANY_URL, data=UPDATE_COMPANY_NAME_DATA)
    with allure.step("Check the result"):
        assert app.request.json()["name"] == UPDATED_NAME
    app.check_200()
