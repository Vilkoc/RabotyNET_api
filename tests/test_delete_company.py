"""This module allows you to delete company and check if the company is absent"""
import allure
from base import COMPANY_EXISTS_URL, DELETING_OF_COMPANY


@allure.feature('Deleting a company')
def test_delete_company(app):
    """Deleting of the company"""

    with allure.step("Login"):
        app.authentication("cowner@gmail.com", "cowner")
    with allure.step("Checking the presence of the company"):
        app.get(COMPANY_EXISTS_URL)
        assert app.request.text == "true"
    with allure.step("Deleting of a company"):
        app.delete(DELETING_OF_COMPANY)
    with allure.step("Checking the absence of the company"):
        app.get(COMPANY_EXISTS_URL)
        assert app.request.text == "false"
    app.check_200()
