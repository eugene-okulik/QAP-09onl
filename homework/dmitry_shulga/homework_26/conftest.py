import pytest
import requests
import json


BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='session')
def get_token(base_url):
    with open("token.txt", "r") as file:
        old_token = file.read()
    response = requests.request('GET', f'{base_url}/authorize/{old_token}').text
    if response == "Token is alive. Username is Dmitry_Shulga":
        act_token = old_token
    else:
        headers = {
            'Content-Type': 'application/json'
        }
        data_json = {
            "name": "Dmitry_Shulga"
        }
        data = json.dumps(data_json)
        response = requests.request(
            'POST',
            f'{base_url}/authorize',
            headers=headers,
            data=data
        ).json()
        new_token = response['token']
        with open("token.txt", "w") as new_file:
            new_file.write(new_token)
        act_token = response['token']
    return act_token


@pytest.fixture(scope='function')
def create_a_post(base_url, get_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
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

