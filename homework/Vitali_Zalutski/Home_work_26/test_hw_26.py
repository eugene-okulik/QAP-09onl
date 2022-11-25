import requests
from base_url import BASE_URL


def test_create_meme(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    info = {
        "text": "gerald",
        "url": "https://www.memify.ru/meme/92056/",
        "tags": ["fun", "russia", "gerald", "film"],
        "info": {"colors": ["grey", "blue"]}
    }
    response = requests.request('POST', f'{BASE_URL}/meme', headers=headers, json=info).json()
    assert response['text'] == "gerald"


def test_update_status_200(create_meme, token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    info = {
        'id': meme_id,
        'text': "after update",
        'url': "https://pikabu.ru/story/vzyal_vazhnoe_9655506",
        'tags': ['fun', 'cat'],
        'info': {'animal': ['cat']}
    }
    response = requests.request("PUT", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=info)
    assert response.status_code == 200


def test_delete_status_200(create_meme, token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    info = ""
    response = requests.request("DELETE", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=info)
    assert response.status_code == 200


def test_delete_status_404(create_meme, token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    info = ""
    requests.request("DELETE", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=info)
    headers = {"Authorization": token}
    response = requests.request("GET", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=info)
    assert response.status_code == 404


def test_get_all(token):
    headers = {
        "Authorization": token
    }
    response = requests.request('GET', f'{BASE_URL}/meme', headers=headers).json()
    tags_list = []
    for memes in range(len(response['data'])):
        tags = (response['data'][memes])
        for i in tags['tags']:
            tags_list.append(i)
    assert 'fun' in tags_list


