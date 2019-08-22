import pytest


def test_api_admin_companies_presence(app):
    app.authentication('login', 'admin@gmail.com', 'admin')

    response = app.put('companies/update')

    assert response.status_code == 200, "Wrong status code"

    assert 'SoftServe' == response.json()[0]['name']
    assert 'InventorSoft' == response.json()[1]['name']
    assert 'ValSoft' == response.json()[2]['name']
