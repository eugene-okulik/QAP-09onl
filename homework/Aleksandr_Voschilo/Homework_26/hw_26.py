import requests
import json


def test_create_mem(base_url, login, token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "what are they cooking",
        "url": "https://memes.com/m/double-tap-to-edit-0mRw6-m0VR3",
        "tags": ["cooking", "cats", "chiken"],
        "info": {"colors": ["orange", "white", "red"], "objects":["picture", "text"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data).json()
    assert response['text'] == "what are they cooking"


def test_change_mem(base_url, token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data_json = {
        "id": 2,
        "text": "what are they cooking",
        "url": "https://memes.com/m/double-tap-to-edit-0mRw6-m0VR3",
        "tags": ["cooking", "cats", "chiken", "fun"],
        "info": {"colors": ["orange", "white", "red"], "objects": ["picture", "text"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/2',
        headers=headers,
        data=data
    ).json()
    assert response["tags"] == ["cooking", "cats", "chiken", "fun"]


def test_get_all_memes(base_url, token):
    headers = {
        'Authorization': token
    }
    response = requests.request('GET', f'{base_url}/meme', headers=headers).json()
    count_of_fun = 0
    for i in range(len(response['data'])):
        for j in response['data'][i]['tags']:
            if j == "fun":
                count_of_fun += 1
    assert count_of_fun >= 1, "Not enough 'fun'!"


def test_delete_mem(base_url, token):
    headers = {
        'Authorization': token
    }
    requests.request('DELETE', f'{base_url}/meme/2', headers=headers)
    response = requests.request('GET', f'{base_url}/meme/2', headers=headers)
    assert response.status_code == 404, 'Deleted post is not deleted'



