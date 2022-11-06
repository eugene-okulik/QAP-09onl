import requests
import json
import settings


def test_create_a_meme(base_url):
    headers = {'Content-Type': 'application/json',
               'Authorization': settings.token}
    data_json = {
        "info": {"object": ["puppy", "animal", "dog"]},
        "tags": ["fun", "animals", "cute"],
        "text": "Are you sure about that???",
        "url": "https://memes.com/m/3-4x8r8pWk9"
    }
    data = json.dumps(data_json)
    response = requests.request('POST', f'{base_url}/meme', headers=headers, data=data).json()
    print(response['id'])
    assert response['text'] == 'Are you sure about that???'


def test_update_meme(base_url, create_a_new_meme):
    meme_id = create_a_new_meme
    headers = {'Content-Type': 'application/json',
               'Authorization': settings.token}
    data_json = {
        "id": meme_id,
        "info": {"object": ["puppy", "animal", "dog"]},
        "tags": ["fun", "animals", "cute"],
        "text": "NOPE...I HAVE NOT SEEN YOUR LIPSTICK",
        "url": "https://memes.com/m/3-4x8r8pWk9"
    }
    data = json.dumps(data_json)
    response = requests.request('PUT', f'{base_url}/meme/{meme_id}', headers=headers, data=data).json()
    assert response['text'] == 'NOPE...I HAVE NOT SEEN YOUR LIPSTICK'
    assert response['tags'] == ['fun', 'animals', 'cute']
    assert response['info'] == {'object': ['puppy', 'animal', 'dog']}


def test_delete_a_meme(base_url, create_a_new_meme):
    headers = {'Authorization': settings.token}
    meme_id = create_a_new_meme
    requests.request('DELETE', f'{base_url}/meme/{meme_id}', headers=headers)
    response = requests.request('GET', f'{base_url}/meme/{meme_id}', headers=headers)
    assert response.status_code == 404, 'ATTENTION! Deleted meme exists'


def test_get_all_memes(base_url):
    headers = {'Authorization': settings.token}
    response = requests.request('GET', f'{base_url}/meme', headers=headers).json()
    for key in response['data']:
        for k, v in key.items():
            if k == 'tags':
                for el in k:
                    if el == 'fun':
                        assert el == 'fun'




