"""This module contains URL's for project requests"""

BASE_URL = 'http://localhost:8080/RabotyNET/'

# Login
LOGIN_URL = BASE_URL + 'login'
LOGOUT_URL = BASE_URL + 'logout'

# Registrtation
USER_REGISTER_URL = BASE_URL + 'users/auth'
USER_CONFIRM_EMAIL_URL = BASE_URL + 'users/auth/confirm'

# Companies
COMPANY_EXISTS_URL = BASE_URL + 'companies/exists/InventorSoft'
DELETING_OF_COMPANY = BASE_URL + 'companies/delete/2'
UPDATE_COMPANY_URL = BASE_URL + 'companies/update'
ALL_COMPANIES_URL = BASE_URL + 'companies/all'
COMPANY_GET_CLAIM_URL = BASE_URL + 'claims/byCompany/1'
CREATE_CLAIM_URL = BASE_URL + 'claims/create'

# User profile
USER_URL = BASE_URL + 'people'
USER_PROFILE_URL = USER_URL + '/3'
GET_USER_ADMIN_INFO = BASE_URL + 'users/1'

# User resume
RESUME_URL = BASE_URL + 'pdf/updatePDF'
SEND_RESUME_URL = BASE_URL + 'vacancies/sendResume/34'
GENERATE_RESUME = BASE_URL + 'pdf/createPdf/2&false'
RESUME_DATA = BASE_URL + 'pdf'

# Vacancies
VACANCIES_URL = BASE_URL + 'vacancies'

# Search
SEARCH_VACANCY_URL = BASE_URL + 'searchVacancy'
