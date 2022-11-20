import pytest
import requests
import json
from base_url import testing_token, BASE_URL


@pytest.fixture(scope="session")
def token():
    url = f"{BASE_URL}/authorize/{testing_token}"
    info_for_user = ""
    response = requests.request("GET", url, data=info_for_user)
    if response.text == "Token is alive. Username is Vitali_Zalutski":
        yield testing_token
    else:
        headers = {'Content-type': 'application/json'}
        info_for_user = {"name": "Vitali_Zalutski"}
        response = requests.request('POST',
                                    f'{BASE_URL}/authorize',
                                    headers=headers,
                                    json=info_for_user).json()
        yield response['token']


@pytest.fixture(scope='function')
def create_meme(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    info = {
        "text": "meme",
        "url": "https://pikabu.ru/story/khekh_9659495",
        "tags": ["fun", "cats"],
        "info": {"colors": ["white", "red", "black"]}
    }
    response = requests.request('POST', f"{BASE_URL}/meme", headers=headers, json=info).json()
    yield response['id']

#a
