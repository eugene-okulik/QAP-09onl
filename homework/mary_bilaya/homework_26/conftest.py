import json
import requests
import pytest
import settings

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='function')
def create_a_new_meme(base_url):
    headers = {'Content-Type': 'application/json',
               'Authorization': settings.token}
    data_json = {
        "info": {"object": ["puppy", "animal", "dog"]},
        "tags": ["fun", "animals", "cute"],
        "text": "Are you sure about that???",
        "url": "https://memes.com/m/3-4x8r8pWk9"
    }
    data = json.dumps(data_json)
    response = requests.request('POST', f'{base_url}/meme', headers=headers, data=data).json()
    yield response['id']






