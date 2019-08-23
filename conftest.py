# import pytest
# from application import Application
# from utilities.db import prepare_db, restart_tomcat
#
#
#
# @pytest.fixture(scope='session', autouse=True)
# def prep_db(worker_id):
#     if worker_id == 'gw0' or worker_id == 'master':
#         # restart_tomcat()
#         prepare_db()
#     # sleep(40)
#
#
# @pytest.fixture(scope='function')
# def app():
#     app = Application()
#     yield app
#
