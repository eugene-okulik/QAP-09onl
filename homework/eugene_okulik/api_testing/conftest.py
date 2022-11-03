import pytest
import requests
import json


BASE_URL = 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='function')
def create_a_post(base_url):
    headers = {
        'Content-Type': 'application/json',
    }
    data_json = {
        "title": "ashdkfjashdlkfjahlkdshafd",
        "body": "ksdhfkjshdlkfhsdfkjhs",
        "userId": 1
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/posts',
        headers=headers,
        data=data
    ).json()
    yield response['id']
