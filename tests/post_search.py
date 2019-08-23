import requests
import json
import allure

data = {"direction": "asc", "firstResultNumber": 0, "resultsOnPage": 3, "searchDocument": "vacancies",
        "searchParameter": "city", "searchSort": "position", "searchText": "chernivtsi"}

HEADERS = {'content-type': 'application/json'}


@allure.feature("Search")
def test_search():
    """testing providing search"""
    session = requests.Session()
    response = session.post(url='http://localhost:8080/RabotyNET/searchVacancy', data=json.dumps(data), headers=HEADERS)

    print(response.json())
    assert response.status_code == 200
    assert response.json()['searchVacancyDtos'][0]['city'] == 'Chernivtsi'
