import requests
import json


def test_create_post(base_url, post_authorize, token):
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
    assert response['text'] == "Great quote"


def test_update_post(base_url, post_authorize, token, create_a_post):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data_json = {
        "id": create_a_post,
        "text": "Great quote from Vladimir Klitschko",
        "url": "https://tengrinews.kz/userdata/4(246).jpg",
        "tags": ["fun", "quote", "Klitschko", "tomorrow"],
        "info": {"object": ["Klitschko", "boxer"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/{create_a_post}',
        headers=headers,
        data=data
    ).json()
    assert response["text"] == "Great quote from Vladimir Klitschko"


def test_delete_post(base_url, post_authorize, token, create_a_post):
    headers = {
        'Authorization': token,
    }
    requests.request(
        'DELETE',
        f'{base_url}/meme/{create_a_post}',
        headers=headers
    )
    response = requests.request(
        'GET',
        f'{base_url}/meme/{create_a_post}',
        headers=headers
    )
    assert response.status_code == 404, 'Deleted post is not deleted'


def test_get_all_posts(base_url, post_authorize, token):
    headers = {
        'Authorization': token,
    }
    response = requests.request('GET', f'{base_url}/meme', headers=headers).json()
    data = response['data']
    print(data)
    sum_fun = 0
    for i in data:
        for key, value in i.items():
            if key == 'tags':
                for tags in value:
                    if tags == 'fun':
                        sum_fun += 1
    assert sum_fun >= 1, "fun does not exist"


