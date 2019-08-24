from base64 import b64decode as decode

TOKEN = "3e83667c-c59c-4fda-aa7a-a47346a3cd6a"

EMAIL_FORGOT_PASSWORD = "rabotynet.test.fp@gmail.com"
FROM_FORGOT_PASSWORD = decode(b'cm9tYV9leHBlcnQ=').decode()

REGISGER_DATA = {
    "login": 'rabotynet.test@gmail.com',
    "matchingPassword": 'Qdrwbj!23',
    "password": 'Qdrwbj!23'
}

LOGIN = [
        ('admin@gmail.com', 'admin', 'Сompanies'),
        ('user@gmail.com', 'user', 'Create company'),
        ('cowner@gmail.com', 'cowner', 'My companies')
    ]
