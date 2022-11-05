import pytest
import requests
import json


BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='function')
def create_a_post(base_url):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bk4wHEq1E3cIgPp'
    }
    data_json = {
        "text": "Cat",
        "url": "https://www.memify.ru/meme/56668/koshka/",
        "tags": ["fun", "animals"],
        "info": {"object": ["cat", "animals"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    yield response['id']
