import pytest
import json
import requests

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    yield BASE_URL


@pytest.fixture(scope='function')
def create_a_meme(base_url, check_token):
    headers = {'Content-Type': 'application/json', 'Authorization': check_token}
    data_json = {
        'text': "Do you prepare to zoom's meeting? :)",
        'url': "https://i.kym-cdn.com/photos/images/newsfeed/001/965/115/01b.jpg",
        'tags': ['zoom', 'meeting', 'computer', 'fun'],
        'info': {'object': ['dog', 'animal']}
    }
    data = json.dumps(data_json)
    response = requests.request('POST', f"{base_url}/meme", headers=headers, data=data).json()
    yield response['id']
    headers = {'Authorization': check_token}
    requests.request("DELETE", f"{base_url}/meme/{response['id']}", headers=headers)


def get_new_token(base_url):
    headers = {'Content-Type': 'application/json'}
    data_json = {'name': 'sveta'}
    data = json.dumps(data_json)
    response = requests.request('POST', f"{base_url}/authorize", headers=headers, data=data).json()
    print(response)
    print("response['token']=", response['token'])
    with open('authorization.txt', 'w') as file:  # w=overwrite the entire file
        file.write(response['token'])
    return response['token']


@pytest.fixture(scope='session')
def check_token(base_url):
    with open('authorization.txt', 'r') as file:
        token = file.read()
    response = requests.request('GET', f"{base_url}/authorize/{token}")
    # print('check-token=', token)
    if response.status_code == 200:  # "Token is found/alive"
        # print('check-then=', token)
        return token
    else:
        token = get_new_token(BASE_URL)
        # print('new-token=', token)
        return token
