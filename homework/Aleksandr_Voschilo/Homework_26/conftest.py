import pytest
import requests
import json


BASE_URL = 'http://167.172.172.115:52355/'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='session')
def token():
    with open('token.txt', 'r') as token_file:
        return token_file.read()


@pytest.fixture(scope='session')
def login(base_url):
    with open('token.txt', 'r') as token_file:
        token = token_file.read()
        response = requests.request('GET', f'{base_url}/authorize/{token}').text
        if response == 'Token is alive. Username is writeln2012':
            return
        else:
            headers = {
                'Content-Type': 'application/json'
            }
            data_json = {
                'name': 'writeln2012'
            }
            data = json.dumps(data_json)
            response_login = requests.request(
                'POST',
                f'{base_url}/authorize',
                headers=headers,
                data=data
            ).json()
            token_file = open('token.txt', 'w')
            token_file.write(response_login['token'])


@pytest.fixture(scope='function')
def create_a_post(base_url, token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "what are they cooking",
        "url": "https://memes.com/m/double-tap-to-edit-0mRw6-m0VR3",
        "tags": ["cooking", "cats", "chicken"],
        "info": {"colors": ["orange", "white", "red"], "objects": ["picture", "text"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data).json()
    yield response['id']
    requests.request('DELETE', f'{base_url}/posts/{response["id"]}')
