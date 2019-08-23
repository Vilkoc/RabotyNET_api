import requests


def test_vacancies():
    """testing login response"""
    session = requests.Session()
    response = session.get(url='http://localhost:8080/RabotyNET/vacancies')

    assert response.status_code == 200
    assert response.json()[0]['description'] == 'Junior Java Developer'
    print(response.json())
