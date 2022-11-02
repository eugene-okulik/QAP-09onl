import pytest
import requests
import json


BASE_URL = "http://167.172.172.115:52355"


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='session')
def authorize(base_url):
    with open("token.txt", 'r') as t:
        token = t.read()
    response = requests.request('GET', f'{base_url}/authorize/{token}').text
    if response == 'Token is alive. Username is vajda':
        return
    else:
        headers = {
            "Content-Type": "application/json"
        }
        data_json = {
            "name": "vajda"
        }
        data = json.dumps(data_json)
        response = requests.request(
            'POST',
            f'{base_url}/authorize',
            headers=headers,
            data=data
        ).json()
        with open("token.txt", "w") as file:
            file.write(response["token"])


@pytest.fixture(scope='session')
def token():
    with open("token.txt", 'r') as t:
        token = t.read()
        return token
