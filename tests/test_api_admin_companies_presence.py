# import allure
import pytest


def test_api_admin_companies_presence(app):

    # response = app('/login', auth=('admin@gmail.com', 'admin'))
    app.authentication('http://localhost:8080/RabotyNET/login', 'admin@gmail.com', 'admin')
    # assert response.status_code == 200, "Wrong status code"
    response = app.get('companies/all')

    assert response.status_code == 200, "Wrong status code"
    print(response.text)
    data_of_companies = response.json()
    assert response.status_code == 200, "Wrong status code"
    print(response.json())

