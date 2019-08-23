import requests

session = requests.Session()
user_data = ("user@gmail.com", "user")
data = {
    "education": {"educationId": "2", "degree": "Master", "school": "KPI",
                  "specialty": "Software Engineer", "graduation": 2009, },
    "jobs": {"2": {"begin": "2010-04-08", "companyName": "InventorSoft", "description": "Senior Java Developer",
                   "end": "2014-11-04", "jobId": 5, "position": "Senior", "printPdf": "true"},
             "1": {"begin": "2008-03-08", "companyName": "ValSoft", "description": "Middle Java developer",
                   "end": "2005-07-04", "jobId": 3, "position": "Middle", "printPdf": "true"},
             "0": {"begin": "2006-10-08", "companyName": "SoftServe", "description": "Junior Java Developer",
                   "end": "2009-10-04", "jobId": 4, "position": "Junior", "printPdf": "true"}},
    "person": {"address": {"addressId": 1, "building": "20", "city": "Chernivtsi", "country": "Ukraine",
                           "street": "Holovna", "zipCode": 58000},
               "birthday": "1999-06-04",
               "contact": {"contactId": 1, "email": "den.ohorodnik@gmail.com", "phoneNumber": "+380973999060"},
               "firstName": "Denys", "lastName": "Ohorodnik", "user": {"userId": 3, "login": "user@gmail.com",
                                                                       "password": "$2a$10$t31PsVNWl8eaWr9/gPwKKeX.4Q2grl12wmiRrN9fEZDMlMGHwA92m",
                                                                       "enabled": "true"}},
    "position": "Junior", "resumeId": 2, "reviewed": "false",
    "skills": {"0": {"description": "Good skill", "printPdf": "true", "skillId": 3, "title": "Linux"},
               "1": {"description": "Some experience", "printPdf": "true", "skillId": 4, "title": "Angular"},
               "2": {"description": "Some experience", "printPdf": "true", "skillId": 5, "title": "Html"}}}


def test_change_data():
    session.post('http://localhost:8080/RabotyNET/login', auth=user_data)
    session.get('http://localhost:8080/RabotyNET/pdf')
    session.get(url="http://localhost:8080/RabotyNET/users/3")
    tmp = {"X-XSRF-TOKEN": session.cookies.get_dict()['XSRF-TOKEN']}
    change = session.put('http://localhost:8080/RabotyNET/pdf/updatePDF', headers=tmp,
                         json=data)

    print(change.text)
