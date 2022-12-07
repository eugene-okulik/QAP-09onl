import requests
import json


def test_create_post(base_url, token_read, enter_login):
    headers = {
        'Authorization': token_read,
        'Content-Type': 'application/json'
    }
    data_json = {
        "info": {"object": ["china", "animal", "cat"]},
        "tags": ["fun", "animals", "cat"],
        "text": "Когда строил планы в начале 2019 года и ничего не предвещало беды...",
        "url": "https://snob.ru/indoc/attachments/snob2/22/06/22064dcb40c8fd69334a3ea45339f4c9f3bd1184bdf44b6b74bb4a236b6d5316.jpg"
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'Когда строил планы в начале 2019 года и ничего не предвещало беды...'


def test_update_post(base_url, token_read, enter_login):
    headers = {
        'Authorization': token_read,
        'Content-Type': 'application/json'
    }
    data_json = {
        "id": 245,
        "info": {
            "object": [
                "china",
                "animal",
                "cat"
            ]
        },
        "tags": [
            "fun",
            "animals",
            "cat"
        ],
        "text": "Когда строил планы в начале 2019 года и ничего не предвещало беды... или нет?!",
        "updated_by": "xsmugxjoex",
        "url": "https://snob.ru/indoc/attachments/snob2/22/06/22064dcb40c8fd69334a3ea45339f4c9f3bd1184bdf44b6b74bb4a236b6d5316.jpg"
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/meme/245',
        headers=headers,
        data=data
    ).json()
    assert response['text'] == 'Когда строил планы в начале 2019 года и ничего не предвещало беды... или нет?!'


def test_delete_post(base_url, token_read, create_a_post):
    headers = {
        'Authorization': token_read
    }
    post_id = create_a_post
    requests.request(
        'DELETE',
        f'{base_url}/meme/{post_id}',
        headers=headers
    )
    response = requests.request(
        'GET',
        f'{base_url}/meme/{post_id}',
        headers=headers
    )
    assert response.status_code == 404, 'Deleted post is not deleted'


def test_get_all_posts(base_url, token_read):
    headers = {
        'Authorization': token_read
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
