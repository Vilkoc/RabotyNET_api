import requests

user_data = ("user@gmail.com", "user")
data = {
    "resumeId": 2,
    "position": "Middle Developer",
    "skills": [
        {
            "skillId": 3,
            "title": "Linux",
            "description": "Good skill",
            "printPdf": "true"
        },
        {
            "skillId": 4,
            "title": "Angular",
            "description": "Some experience",
            "printPdf": "true"
        },
        {
            "skillId": 5,
            "title": "Html",
            "description": "Some experience",
            "printPdf": "true"
        }
    ],
    "jobs": [
        {
            "jobId": 4,
            "position": "Junior",
            "begin": "2006-10-08",
            "end": "2009-10-04",
            "companyName": "SoftServe",
            "description": "Junior Java Developer",
            "printPdf": "true"
        },
        {
            "jobId": 5,
            "position": "Senior",
            "begin": "2010-04-08",
            "end": "2014-11-04",
            "companyName": "InventorSoft",
            "description": "Senior Java Developer",
            "printPdf": "true"
        },
        {
            "jobId": 3,
            "position": "Middle",
            "begin": "2008-03-08",
            "end": "2005-07-04",
            "companyName": "ValSoft",
            "description": "Middle Java developer",
            "printPdf": "true"
        }
    ],
    "education": {
        "educationId": 2,
        "degree": "Master",
        "school": "KPI",
        "specialty": "Software Engineer",
        "graduation": 2009
    },
    "person": {
        "userId": 3,
        "firstName": "Denys",
        "lastName": "Ohorodnik",
        "birthday": "1999-06-04",
        "contact": {
            "contactId": 1,
            "email": "den.ohorodnik@gmail.com",
            "phoneNumber": "+380973999060"
        },
        "address": {
            "addressId": 1,
            "country": "Ukraine",
            "city": "Chernivtsi",
            "street": "Holovna",
            "building": "20",
            "zipCode": 58000
        },
        "user": {
            "userId": 3,
            "login": "user@gmail.com",
            "password": "$2a$10$t31PsVNWl8eaWr9/gPwKKeX.4Q2grl12wmiRrN9fEZDMlMGHwA92m",
            "enabled": "true"
        }
    },
    "reviewed": "false",
    "vacancies": [

    ]
}


def test_change_data():
    session = requests.Session()
    session.post(url="http://localhost:8080/RabotyNET/login",
                 auth=user_data)
    session.get("http://localhost:8080/RabotyNET")
    tmp = {"X-XSRF-TOKEN": session.cookies.get_dict()['XSRF-TOKEN'], 'content-type': 'application/json'}
    change = session.put('http://localhost:8080/RabotyNET/pdf/updatePDF', json=data, headers=tmp)

    print(change.status_code)