import pytest
from application import Application
from utilities.db import prepare_db
from utilities.db import restart_tomcat
from time import sleep


@pytest.fixture(scope='session', autouse=True)
def prep_db(worker_id):
    if worker_id == 'gw0' or worker_id == 'master':
        restart_tomcat()
        prepare_db()
    sleep(40)


@pytest.fixture(scope='function')
def app():
    """Creates instance of Application class"""
    app = Application()
    yield app
