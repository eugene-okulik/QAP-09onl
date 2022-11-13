import requests
import json


def test_create_new_meme(base_url, user_authorization):
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
    data_json = {
        "text": "we cant keep it - my dad 10 months ago",
        "url": "https://sun9-35.userapi.com/impg/aQnVdpGvRGcsisBvX3k_uJ2mz04qMZ-Wi8vFaw/9bPt8FYiHl8.jpg?size=1028x1110&quality=95&sign=66dceafcc6ef0b6aff613655a52beed5&type=album",
        "tags": ["fun", "dad", "cat"],
        "info": {"colors": ["gray", "orange", "blue"],
                 "objects": ["room", "cat", "dad"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['url'] == "https://sun9-35.userapi.com/impg/aQnVdpGvRGcsisBvX3k_uJ2mz04qMZ-Wi8vFaw/9bPt8FYiHl8.jpg?size=1028x1110&quality=95&sign=66dceafcc6ef0b6aff613655a52beed5&type=album"


def test_update_meme(base_url, user_authorization, create_a_meme):
    meme_id = create_a_meme
    headers = {
        "Authorization": f'{user_authorization}',
        'Content-Type': 'application/json'
    }
    data_json = {
        "id": meme_id,
        "text": "funny meme",
        "url": "https://sun9-3.userapi.com/impg/MhZfx8fqO9BOQLx2LQU3uTpeWPzFL8dHkKKgQA/8gGJdqbZ9Ow.jpg?size=827x1029&quality=96&sign=c61d4cf5bac48e8659cb6b586bdffbcb&type=album",
        "tags": ["old man", "technical support", "hamster", "mouse", "fun"],
        "info": {"colors": ["gray", "white", "blue"],
                 "objects": ["headphones", "men"]}
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/{meme_id}',
        headers=headers,
        data=data
    ).json()
    assert response['url'] == "https://sun9-3.userapi.com/impg/MhZfx8fqO9BOQLx2LQU3uTpeWPzFL8dHkKKgQA/8gGJdqbZ9Ow.jpg?size=827x1029&quality=96&sign=c61d4cf5bac48e8659cb6b586bdffbcb&type=album"


def test_delete_post(base_url, user_authorization, create_a_meme):
    meme_id = create_a_meme
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
    assert response.status_code == 404, 'Deleted meme is not deleted'


def test_get_all_meme(base_url, user_authorization):
    headers = {
        "Authorization": f'{user_authorization}'
    }
    response = requests.request(
        'GET',
        f'{base_url}/meme',
        headers=headers
    ).json()
    
    flag = False
    for memes in response['data']:
        if 'dad' in memes['tags']:
            flag = True

    assert flag, "meme with tag fun is not found"
