import pytest
from application import Application
from utilities.db import prepare_db


# @pytest.fixture(scope='session', autouse=True)
# def prep_db(worker_id):
#     """Updates DB befire running tests"""
#     if worker_id == 'gw0' or worker_id == 'master':
#         prepare_db()


@pytest.fixture(scope='function')
def app():
    """Creates instance of Application class"""
    app = Application()
    yield app
