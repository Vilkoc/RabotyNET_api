"""This module allows finding vacancies"""
import allure
from base import VACANCIES_URL


@allure.feature('Get vacancies')
def test_vacancies(app):
    """Get vacancies"""

    with allure.step('Getting vacancies'):
        app.get(VACANCIES_URL)

    with allure.step('Cheking result'):
        assert app.request.status_code == 200

    with allure.step('Cheking first vacancy'):
        assert app.request.json()[0]['description'] == 'Junior Java Developer'
