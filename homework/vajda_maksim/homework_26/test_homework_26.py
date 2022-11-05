import requests
import json


def test_create_meme(base_url, authorize, token):
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    data_json = {
        "text": "do you want caviar?",
        "url": "https://s00.yaplakal.com/pics/pics_original/9/5/0/7027059.jpg",
        "tags": ["ikra", "caviar"],
        "info": {"colors": ["red", "black", "KabachoK"], "object": ["banka", "muzhyk"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == "do you want caviar?"


def test_change_meme(base_url, authorize, token, create_a_mem):
    meme_id = create_a_mem
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    data_json = {
        "id": meme_id,
        "text": "do you want caviar?",
        "url": "https://s00.yaplakal.com/pics/pics_original/4/6/0/7027064.jpg",
        "tags": ["ikra", "caviar"],
        "info": {"colors": ["red", "black", "KabachoK"], "object": ["banka", "muzhyk"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/{meme_id}',
        headers=headers,
        data=data
    ).json()
    assert response['url'] == "https://s00.yaplakal.com/pics/pics_original/4/6/0/7027064.jpg"


def test_delete_meme(base_url, authorize, token, create_a_mem):
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    meme_id = create_a_mem
    requests.request(
        'DELETE',
        f'{base_url}/meme/{meme_id}',
        headers=headers
    )
    response = requests.request(
        'GET',
        f'{base_url}/meme/{meme_id}',
        headers=headers
    )
    assert response.status_code == 404, 'Deleted post is not deleted'


def test_get_all_memes(base_url, authorize, token):
    headers = {
        "Authorization": f"{token}"
    }
    response = requests.request(
        'GET',
        f'{base_url}/meme',
        headers=headers
    ).json()
    for key in response['data']:
        for k, v in key.items():
            if k == 'tags':
                for tag in v:
                    if tag == 'fun':
                        assert tag == 'fun'
