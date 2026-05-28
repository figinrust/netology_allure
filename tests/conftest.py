import pytest
import requests

@pytest.fixture
def valid_qwery_params():
    return {'foo': 'bar', 'test': '123'}
