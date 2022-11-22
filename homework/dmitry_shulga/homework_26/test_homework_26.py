import requests
import json


def test_get_all_posts(base_url, get_token):
    headers = {
                 'Content-Type': 'application/json',
                 'Authorization': get_token
             }
    response = requests.request('GET', f'{base_url}/meme', headers=headers).json()
    for key in response['data']:
        for k, v in key.items():
            if k == 'tags':
                for tag in v:
                    if tag == 'fun':
                        assert tag == 'fun'


def test_one_post(base_url, get_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    response = requests.request('GET', f'{base_url}/meme/1', headers=headers).json()
    assert response['id'] == 1


def test_create_post(base_url, get_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    data_json = {
        "text": "Dog",
        "url": "https://www.memify.ru/meme/57275/sobaka/",
        "tags": ["fun", "animals"],
        "info": {"object": ["dog", "animals"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['url'] == 'https://www.memify.ru/meme/57275/sobaka/'
    create_id = response['id']
    requests.request('DELETE', f'{base_url}/meme/{create_id}', headers=headers)


def test_update_post(base_url, create_a_post, get_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    put_id = create_a_post
    data_json = {
        "id":  put_id,
        "text": "Funny Cat",
        "url": "https://www.memify.ru/meme/56668/koshka/",
        "tags": ["fun", "animals"],
        "info": {"object": ["cat", "animals"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/{put_id}',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'Funny Cat'
    requests.request('DELETE', f'{base_url}/meme/{put_id}', headers=headers)


def test_delete_post(base_url, create_a_post, get_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    post_id = create_a_post
    requests.request('DELETE', f'{base_url}/meme/{post_id}', headers=headers)
    response = requests.request('GET', f'{base_url}/meme/{post_id}', headers=headers)
    assert response.status_code == 404, 'Deleted post is not deleted'

