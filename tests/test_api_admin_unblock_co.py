import pytest


@pytest.skip(reason='skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
def test_api_admin_unblock_co(app):
    app.authentication('login', 'admin@gmail.com', 'admin')
    data = {'companyId': 3, 'name': 'ValSoft', 'edrpou': '63964221', 'description': 'Third company',
            'website': 'www.valsoft.com', 'status': 'APPROVED',
            'contact': {'contactId': 5, 'email': 'valsoft@gmail.com', 'phoneNumber': '+380972993270'},
            'address': {'addressId': 5, 'country': 'Ukraine', 'city': 'Chernivtsi', 'street': 'Rivnenska',
                        'building': '15', 'zipCode': 58000}, 'vacancies': [
            {'vacancyId': 7, 'description': 'Junior Java Developer', 'position': 'Junior Developer',
             'employment': 'FULL', 'vacancyStatus': 'OPEN', 'salary': 1000, 'currency': 'USD', 'hotVacancy': False,
             'requirements': [{'requirementId': 13, 'description': 'Experience with monitoring and log management '},
                              {'requirementId': 14,
                               'description': 'Degree in Computer Science, Engineering or relevant field'}]},
            {'vacancyId': 8, 'description': 'Middle WebUI Developer', 'position': 'Middle Developer',
             'employment': 'HOURLY', 'vacancyStatus': 'OPEN', 'salary': 3000, 'currency': 'UAH', 'hotVacancy': True,
             'requirements': [
                 {'requirementId': 16, 'description': 'Good written and verbal English communications skills'},
                 {'requirementId': 15, 'description': 'Extensive understanding of enterprise monitoring solutions'}]},
            {'vacancyId': 9, 'description': 'Senior React Developer', 'position': 'Senior Developer',
             'employment': 'PART_TIME', 'vacancyStatus': 'OPEN', 'salary': 4000, 'currency': 'EUR', 'hotVacancy': True,
             'requirements': [{'requirementId': 17, 'description': 'Deep knowledge DBs, RDBMS, SQL'},
                              {'requirementId': 18,
                               'description': 'You are adept at writing unit tests and testable code, and working under distributed version control'}]}],
            'user': {'userId': 2, 'login': 'cowner@gmail.com',
                     'password': '$2a$10$DmeWO6UlY/m2QjJaxLGUzezqOotvJmpzbBmZGBr8o/HHeNUuCWcpK', 'enabled': True}}

    response = app.put('companies/update', data)

    assert response.status_code == 200, "Wrong status code"
    assert 'APPROVED' == response.json()[0]['status']

