from application import Application

app = Application()

app.authentication('user@gmail.com', 'user')

app.put('people', {'userId': 3, 'firstName': 'Denys', 'lastName': 'Ohorodnik', 'birthday': '1999-06-04', 'contact': {'contactId': 1, 'email': 'den.ohorodnik@gmail.com', 'phoneNumber': '+380973999060'}, 'address': {'addressId': 1, 'country': 'Ukraine', 'city': 'Chernivtsi', 'street': 'Holovna', 'building': '20', 'zipCode': 58000}, 'user': {'userId': 3, 'login': 'user@gmail.com', 'password': '$2a$10$t31PsVNWl8eaWr9/gPwKKeX.4Q2grl12wmiRrN9fEZDMlMGHwA92m', 'enabled': True}})

app.debug_info()

