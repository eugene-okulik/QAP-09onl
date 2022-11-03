import json
import pytest
import requests

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope="session")
def base_url():
    yield BASE_URL


@pytest.fixture(scope="session")
def user_authorization(base_url):
    headers = {
        'Content-type': 'application/json',
    }
    data_json = {
        "name": "pavel"
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/authorize',
        headers=headers,
        data=data
    ).json()
    yield response['token']

