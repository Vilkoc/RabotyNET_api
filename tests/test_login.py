import pytest
from data_tests.auth import USERNAME_SIGNUP, PASSWORD, EMAIL_SIGNUP, FROM_SIGNUP
import allure
import json
from utilities.db import change_varification_link, wait_user_update

from pprint import pprint

TOKEN = "3e83667c-c59c-4fda-aa7a-a47346a3cd6a"

@pytest.mark.skip
@allure.feature('Sign In')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'ROLE_ADMIN'),
    ('user@gmail.com', 'user', 'ROLE_USER'),
    ('cowner@gmail.com', 'cowner', 'ROLE_COWNER')
    ])
def test_login(app, user, password, expected):
    # session = requests.Session()
    session = app.session
    response = session.post('http://localhost:8080/RabotyNET/login', auth=(user, password))
    assert response.status_code == 200, "Wrong status code"
    data = response.json()
    assert data['username'] == user, "Wrong username"
    assert data['authorities'][0]['authority'] == expected, "Wrong user role"
    session.get('http://localhost:8080/RabotyNET/logout')

@pytest.mark.skip
def test_sign_up_begin(app):
    data_sent = {
      "login": USERNAME_SIGNUP,
      "matchingPassword": PASSWORD,
      "password": PASSWORD
    }

    response = app.post('users/auth', data=data_sent)

    assert response.status_code == 200, "Wrong status code"
    data_received = response.json()
    assert data_received['login'] == data_sent['login'], "Wrong username"

@pytest.mark.skip
def test_sign_up_end(app):
    # session = requests.Session()
    data = {'token': TOKEN}
    change_varification_link(USERNAME_SIGNUP)

    response = app.get('users/auth/confirm', data=data)

    print(response.text)
    assert response.status_code == 200, "Wrong status code"
    data_received = response.json()
    print(data_received)
    request = app.authentication(USERNAME_SIGNUP, PASSWORD)
    assert request.status_code == 200
    print(request.text)


@pytest.mark.skip
def test_others_Roma(app):
    # l = app.authentication('cowner@gmail.com', 'cowner')
    # r = app.get('companies/my')
    # print(r.text,  l.text)
    #
    # from pprint import pprint
    # pprint(request.json())

    app.authentication('admin@gmail.com', 'admin')

    data = {"user": {"userId": 1, "login": "admin@gmail.com",
                     "password": "$2a$10$E2.PwtnpF2p6aB3NFM3Qo.TarTYsaiWD0yTZ7qY1U3K.ybKxNvCku", "enabled": "true"},
            "company": {"companyId": 1, "name": "SoftServe", "edrpou": "23456742",
                        "description": "We are digital advisors and providers who operate at the cutting edge of technology. We deliver the innovation, quality, and speed that our clients’ users expect.",
                        "website": "www.softserveinc.com", "status": "APPROVED",
                        "contact": {"contactId": 3, "email": "softserve.inc@gmail.com", "phoneNumber": "+380322409999"},
                        "address": {"addressId": 3, "country": "Ukraine", "city": "Chernivtsi", "street": "Holovna",
                                    "building": "246", "zipCode": 58000},
                        "vacancies": [
                            {"vacancyId": 30, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 60, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 59, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 18, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 36, "description": "Good knowledge of Python"},
                                              {"requirementId": 35,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 11, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [
                                 {"requirementId": 21, "description": "Fundamental understanding of testing process"},
                                 {"requirementId": 22, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 33, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 65, "description": "Good knowledge of Python"},
                                              {"requirementId": 66,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 14, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [{"requirementId": 27, "description": "Good knowledge of Python"},
                                              {"requirementId": 28,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 15, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [
                                 {"requirementId": 30, "description": "Fundamental understanding of testing process"},
                                 {"requirementId": 29, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 22, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 44, "description": "Good knowledge of Python"},
                                              {"requirementId": 43,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 2, "description": "Middle React Developer", "position": "Middle Developer",
                             "employment": "HOURLY", "vacancyStatus": "OUTDATED", "salary": 3000, "currency": "UAH",
                             "hotVacancy": "false", "requirements": [{"requirementId": 4,
                                                                      "description": "Proven experience as a Java Software Engineer, Java Developer or similar role"},
                                                                     {"requirementId": 3,
                                                                      "description": "Strong organizational and leadership skills"}]},
                            {"vacancyId": 25, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 50, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 49, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 3, "description": "Senior Angular Developer", "position": "Senior Developer",
                             "employment": "PART_TIME", "vacancyStatus": "OUTDATED", "salary": 4000, "currency": "UAH",
                             "hotVacancy": "false", "requirements": [{"requirementId": 5,
                                                                      "description": "Strong experience building Java EE applications, preferably using Java 8"},
                                                                     {"requirementId": 6,
                                                                      "description": "Degree in Computer Science, Engineering or relevant field"}]},
                            {"vacancyId": 13, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [
                                 {"requirementId": 26, "description": "Fundamental understanding of testing process"},
                                 {"requirementId": 25, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 29, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 58, "description": "Good knowledge of Python"},
                                              {"requirementId": 57,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 28, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 56, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 55, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 17, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 34, "description": "Good knowledge of Python"},
                                              {"requirementId": 33,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 24, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 47, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 48, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 10, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [{"requirementId": 20, "description": "Good knowledge of Python"},
                                              {"requirementId": 19,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 23, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 46, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 45, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 20, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 39, "description": "Good knowledge of Python"},
                                              {"requirementId": 40,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 21, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 42, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 41, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 27, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true", "requirements": [
                                {"requirementId": 53, "description": "Fundamental understanding of testing process"},
                                {"requirementId": 54, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 34, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 67, "description": "Good knowledge of Python"},
                                              {"requirementId": 68,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 4, "description": "Junior Junior Developer", "position": "Junior Developer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 1000, "currency": "EUR",
                             "hotVacancy": "false", "requirements": [{"requirementId": 8,
                                                                      "description": "Ability to program production-grade applications with Node.js"},
                                                                     {"requirementId": 7,
                                                                      "description": "Bachelor degree in computer science or related fields"}]},
                            {"vacancyId": 6, "description": "Senior Angular Developer", "position": "Senior Developer",
                             "employment": "PART_TIME", "vacancyStatus": "OPEN", "salary": 4000, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [
                                 {"requirementId": 11, "description": "Experience with any public cloud provider"},
                                 {"requirementId": 12, "description": "Experience in and understanding of CI"}]},
                            {"vacancyId": 12, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [
                                 {"requirementId": 23, "description": "Fundamental understanding of testing process"},
                                 {"requirementId": 24, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 26, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 52, "description": "Good knowledge of Python"},
                                              {"requirementId": 51,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 16, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "requirements": [
                                 {"requirementId": 32, "description": "Fundamental understanding of testing process"},
                                 {"requirementId": 31, "description": "Good knowledge of Python"}]},
                            {"vacancyId": 19, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 37, "description": "Good knowledge of Python"},
                                              {"requirementId": 38,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 32, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 63, "description": "Good knowledge of Python"},
                                              {"requirementId": 64,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 31, "description": "Junior ATQC Engineer", "position": "Junior Engineer",
                             "employment": "FULL", "vacancyStatus": "OPEN", "salary": 450, "currency": "USD",
                             "hotVacancy": "true",
                             "requirements": [{"requirementId": 61, "description": "Good knowledge of Python"},
                                              {"requirementId": 62,
                                               "description": "Fundamental understanding of testing process"}]},
                            {"vacancyId": 5, "description": "Middle WebUI Developer", "position": "Middle Developer",
                             "employment": "HOURLY", "vacancyStatus": "OPEN", "salary": 3000, "currency": "EUR",
                             "hotVacancy": "false",
                             "requirements": [
                                 {"requirementId": 10, "description": "Good understanding of the networking"},
                                 {"requirementId": 9,
                                  "description": "Solid understanding of Linux operating system"}]},
                            {"vacancyId": 1, "description": "Junior Java Developer", "position": "Junior Developer",
                             "employment": "FULL", "vacancyStatus": "OCCUPIED", "salary": 1000, "currency": "USD",
                             "hotVacancy": "false",
                             "requirements": [{"requirementId": 1, "description": "Problem-solving skills"},
                                              {"requirementId": 2,
                                               "description": "Good knowledge of PostgreSQL, JUnit, bash, ant, Linux"}]}],
                        "user": {"userId": 2, "login": "cowner@gmail.com",
                                 "password": "$2a$10$DmeWO6UlY/m2QjJaxLGUzezqOotvJmpzbBmZGBr8o/HHeNUuCWcpK",
                                 "enabled": "true"},
                        "claims": []}, "title": "None", "description": "tgrhh"}

    response = app.get('claims/byCompany/1')
    print('==== 1 ===')
    pprint(response.text)

    pprint(app.session.cookies.get_dict())

    pprint(app.session.cookies.get_dict())
    response = app.post('claims/create', data)
    pprint(app.session.cookies.get_dict())
    assert response.status_code == 200, "Wrong status code"
    response = app.get('claims/byCompany/1')
    print('==== 2 ===')
    pprint(response.text)

    assert response.status_code == 200, "Wrong status code"


def test_others_Nazar(app):
    app.authentication('user@gmail.com', 'user')

    data = {"resumeId":200,"position":"Junior","skills":[{"skillId":3,"title":"Linux","description":"Good skill","printPdf":True},{"skillId":4,"title":"Angular","description":"Some experience","printPdf":True},{"skillId":5,"title":"Html","description":"Some experience","printPdf":True}],"jobs":[{"jobId":4,"position":"Junior","begin":"2006-10-08","end":"2009-10-04","companyName":"SoftServe","description":"Junior Java Developer","printPdf":True},{"jobId":5,"position":"Senior","begin":"2010-04-08","end":"2014-11-04","companyName":"InventorSoft","description":"Senior Java Developer","printPdf":True},{"jobId":3,"position":"Middle","begin":"2008-03-08","end":"2005-07-04","companyName":"ValSoft","description":"Middle Java developer","printPdf":True}],"education":{"educationId":2,"degree":"Master","school":"KPI","specialty":"Software Engineer","graduation":2009},"person":{"userId":3,"firstName":"Denys","lastName":"Ohorodnik","birthday":"1999-06-04","contact":{"contactId":1,"email":"den.ohorodnik@gmail.com","phoneNumber":"+380973999060"},"address":{"addressId":1,"country":"Ukraine","city":"Chernivtsi","street":"Holovna","building":"20","zipCode":58000},"user":{"userId":3,"login":"user@gmail.com","password":"$2a$10$t31PsVNWl8eaWr9/gPwKKeX.4Q2grl12wmiRrN9fEZDMlMGHwA92m","enabled":True}},"reviewed":False,"vacancies":[]}

    pprint(app.session.cookies.get_dict())
    request = app.put('pdf/updatePDF', data)
    print('==== 2 ===', request.status_code, request.text)
    pprint(request.json())
    assert request.status_code == 200, "Wrong status code"

    assert request.status_code == 200, "Wrong status code"
