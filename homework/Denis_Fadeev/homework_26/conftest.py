import pytest
import requests
import json

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='session')
def token_read():
    with open('token.txt', 'r') as file_t:
        return file_t.read()


@pytest.fixture(scope='session')
def enter_login(base_url):
    with open('token.txt', 'r') as file_t:
        token = file_t.read()
        response = requests.request('GET', f'{base_url}/authorize/{token}').text
        if response == 'Token is alive. Username is xsmugxjoex':
            return
        else:
            headers = {
                'Content-Type': 'application/json'
            }
            data_json = {
                "name": "xsmugxjoex"
            }
            data = json.dumps(data_json)
            response = requests.request(
                'POST',
                f'{base_url}/authorize',
                headers=headers,
                data=data
            ).json()
            file_t = open('token.txt', 'w')
            file_t.write(response['token'])


@pytest.fixture(scope='function')
def create_a_post(base_url, token_read, enter_login):
    headers = {
        'Authorization': token_read,
        'Content-Type': 'application/json'
    }
    data_json = {
        "info": {"object": ["china", "animal", "cat"]},
        "tags": ["fun", "animals", "cat"],
        "text": "Когда строил планы в начале 2019 года и ничего не предвещало беды...",
        "url": "https://snob.ru/indoc/attachments/snob2/22/06/22064dcb40c8fd69334a3ea45339f4c9f3bd1184bdf44b6b74bb4a236b6d5316.jpg"
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    yield response['id']
