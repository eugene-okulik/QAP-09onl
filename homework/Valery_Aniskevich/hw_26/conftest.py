import pytest
import requests
import json

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='session')
def post_authorize(base_url):
    with open('token.txt', 'r') as token_file:
        token = token_file.read()
        response_authorize = requests.request('GET', f'{base_url}/authorize/{token}').text
        if response_authorize == "Token is alive. Username is Valera":
            return
        else:
            headers = {
                'Content-Type': 'application/json',
            }
            data_json = {
                "name": "Valera"
            }
            data = json.dumps(data_json)
            response = requests.request('POST', f'{base_url}/authorize', headers=headers, data=data).json()
            token_file = open('token.txt', 'w')
            token_file.write(response['token'])


@pytest.fixture(scope='session')
def token():
    with open('token.txt', 'r') as token_file:
        return token_file.read()


@pytest.fixture(scope='function')
def create_a_post(base_url, token, post_authorize):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "Great quote",
        "url": "https://tengrinews.kz/userdata/4(246).jpg",
        "tags": ["fun", "quote", "Klitschko", "tomorrow"],
        "info": {"object": ["Klitschko", "boxer"]}
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
