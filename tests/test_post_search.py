"""This module allows searching for  vacancies"""
import allure
import pytest
from base import SEARCH_VACANCY_URL
from data_tests.guest_data import SEARCH_VACANCY_DATA
from data_tests.guest_data import HEADERS


@allure.feature("Search")
# @pytest.mark.skip(reason='patamushto-because')
def test_zsearch(app):
    """testing providing search"""
    with allure.step('Providing search for vacancy'):
        app.post(SEARCH_VACANCY_URL, data=SEARCH_VACANCY_DATA, headers=HEADERS)

    with allure.step('Cheking status code'):
        assert app.request.status_code == 200

    with allure.step('Cheking resulit'):
        assert app.request.json()['searchVacancyDtos'][0]['city'] == 'Chernivtsi'
