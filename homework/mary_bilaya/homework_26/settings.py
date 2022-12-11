import json
import requests

token = 's5Vn2QsIZbOzREo'


def test_check_token(base_url):
    response = requests.request('GET', f'{base_url}/authorize/{token}')
    assert response.status_code == 200, 'Token is not alive'


def test_token(base_url):
    headers = {'Content-Type': 'application/json'}
    data_json = {"name": "mary"}
    data = json.dumps(data_json)
    response = requests.request('POST', f'{base_url}/authorize', headers=headers, data=data).json()
    authorization_token = response['token']
    print(authorization_token)

