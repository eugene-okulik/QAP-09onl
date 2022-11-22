import pytest
import requests
from settings import test_token, BASE_URL


@pytest.fixture(scope="session")
def get_token():
    url = f"{BASE_URL}/authorize/{test_token}"
    payload = ""
    response = requests.request("GET", url, data=payload)
    if response.text == "Token is alive. Username is a.dudin":
        yield test_token
    else:
        headers = {'Content-type': 'application/json'}
        payload = {"name": "a.dudin"}
        response = requests.request('POST',
                                    f'{BASE_URL}/authorize',
                                    headers=headers,
                                    json=payload).json()
        yield response['token']


@pytest.fixture(scope='function')
def create_meme(get_token):
    headers = {
        'Authorization': get_token,
        'Content-Type': 'application/json'
    }
    payload = {
        "text": "text_meme",
        "url": "https://www.memify.ru/meme/91720/",
        "tags": ["fun", "cats"],
        "info": {"colors": ["orange", "red", "black"]}
    }
    response = requests.request('POST', f"{BASE_URL}/meme", headers=headers, json=payload).json()
    yield response['id']
