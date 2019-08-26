import pytest
from application import Application
from utilities.db import prepare_db


@pytest.fixture(scope='session', autouse=False)
def prep_db(worker_id):
    if worker_id == 'gw0' or worker_id == 'master':
        prepare_db()


@pytest.fixture(scope='function')
def app():
    app = Application()
    yield app
