import requests
import json


def test_create_meme(base_url, user_authorization):
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "Джун и собесы",
        "url": "https://hr-portal.ru/files/styles/large/public/mini/120332410_1489612924581086_7825869147172094934_n.jpg?itok=4KomK-7F",
        "tags": ["real life", "pizza"],
        "info": {"colors": ["white", "black", "red"],
                 "objects": ["pizza", "text", "picture"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['url'] == "https://hr-portal.ru/files/styles/large/public/mini/120332410_1489612924581086_7825869147172094934_n.jpg?itok=4KomK-7F"


def test_update_meme(base_url, user_authorization, test_create_meme):
    meme_id =test_create_meme
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
    data_json = {
        "id": meme_id,
        "text": "В ТЗ всё написано, делайте, что просят...",
        "url": "https://devby.io/storage/images/16/12/40/11/derived/bc79f08f4fd660a3388590070cb16704.jpg",
        "tags": ["numbers", "IT"],
        "info": {"colors": ["blue", "white", "black"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/{meme_id}',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == "В ТЗ всё написано, делайте, что просят..."


def test_delete_mem(base_url, user_authorization, test_create_meme):
    meme_id = test_create_meme
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
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
    assert response.status_code == 404, "Deleted meme is not exist"
