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
        "name": "evgen"
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/authorize',
        headers=headers,
        data=data
    ).json()
    yield response['token']


@pytest.fixture(scope='function')
def create_a_meme(base_url, user_authorization):
    headers = {
        'Authorization': f'{user_authorization}',
        'Content-Type': 'application/json'
    }

    data_json = {
        "text": "как я разбираюсь в собаках",
        "url": "https://cs14.pikabu.ru/post_img/2022/11/10/8/1668087866112982105.jpg",
        "tags": ["fun", "dogs", 'fundogs'],
        "info": {"colors": ["orange", "white", "red"], "objects": ["picture", "text"]}
    }
    data = json.dumps(data_json)
    response = requests.request('POST', f"{base_url}/meme", headers=headers, data=data).json()
    yield response['id']
    headers = {'Authorization': user_authorization}
    requests.request("DELETE", f"{base_url}/meme/{response['id']}", headers=headers)
