import pytest
import requests
import json

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope="session")
def user_authorization(base_url):
    headers = {
        'Content-type': 'application/json',
    }
    data_json = {
        "name": "Tanya"
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
def create_meme(base_url, user_authorization):
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "Джун и собесы",
        "url": "https://hr-portal.ru/files/styles/large/public/mini/120332410_1489612924581086_7825869147172094934_n.jpg?itok=4KomK-7F",
        "tags": ["real life", "pizza"],
        "info": {"colors": ["white", "black", "red"],
                 "objects": ["pizza", "text", "picture"]}
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
