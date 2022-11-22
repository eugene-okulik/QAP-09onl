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


@pytest.fixture(scope="function")
def create_a_meme(base_url, user_authorization):
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "we cant keep it - my dad 10 months ago",
        "url": "https://sun9-35.userapi.com/impg/aQnVdpGvRGcsisBvX3k_uJ2mz04qMZ-Wi8vFaw/9bPt8FYiHl8.jpg?size=1028x1110&quality=95&sign=66dceafcc6ef0b6aff613655a52beed5&type=album",
        "tags": ["fun", "dad", "cat"],
        "info": {"colors": ["gray", "orange", "blue"],
                 "objects": ["room", "cat", "dad"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    yield response['id']
    requests.request('DELETE', f'{base_url}/meme/{response["id"]}')

