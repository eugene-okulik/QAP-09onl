import requests
from settings import BASE_URL

def test_create_meme_check_text_is_correct(get_token):
    headers = {
        'Authorization': get_token,
        'Content-Type': 'application/json'
    }
    payload = {
        "text": "roads",
        "url": "https://www.memify.ru/meme/39626/",
        "tags": ["fun", "russia", 'road'],
        "info": {"colors": ["grey", "blue"]}
    }
    response = requests.request('POST', f'{BASE_URL}/meme', headers=headers, json=payload).json()
    assert response['text'] == "roads"


def test_create_meme_check_status_code_200(get_token):
    headers = {
        'Authorization': get_token,
        'Content-Type': 'application/json'
    }
    payload = {
        "text": "work",
        "url": "https://www.memify.ru/meme/90982/vrach-mama-rabota-sobaka/",
        "tags": ["fun", "dogs", 'fundogs'],
        "info": {"colors": ["orange", "white", "red"]}
    }
    response = requests.request('POST', f'{BASE_URL}/meme', headers=headers, json=payload)
    assert response.status_code == 200


def test_update_meme_check_status_code_200(create_meme, get_token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    payload = {
        'id': meme_id,
        'text': "Text after update",
        'url': "https://www.memify.ru/meme/91720/",
        'tags': ['fun', 'cat'],
        'info': {'animal': ['cat']}
    }
    response = requests.request("PUT", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=payload)
    assert response.status_code == 200


def test_update_meme_check_tag_value(create_meme, get_token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    payload = {
        'id': meme_id,
        'text': "Text after update",
        'url': "https://www.memify.ru/meme/6203/rabochee-sobranie-kogda-trudishsja-na-udalenke/",
        'tags': ['fun'],
        'info': {'object': ['two cats', 'eat']}
    }
    response = requests.request("PUT", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=payload).json()
    assert response["tags"] == ['fun']


def test_delete_meme_check_status_code_200(create_meme, get_token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    payload = ""
    response = requests.request("DELETE", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=payload)
    assert response.status_code == 200


def test_delete_meme_check_status_code_404(create_meme, get_token):
    meme_id = create_meme
    headers = {
        'Content-Type': 'application/json',
        'Authorization': get_token
    }
    payload = ""
    requests.request("DELETE", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=payload)
    headers = {"Authorization": get_token}
    response = requests.request("GET", f"{BASE_URL}/meme/{meme_id}", headers=headers, json=payload)
    assert response.status_code == 404


def test_get_all_post(get_token):
    all_tags = []
    headers = {
        "Authorization": get_token
    }
    response = requests.request('GET', f'{BASE_URL}/meme', headers=headers).json()['data']
    for element in response:
        for k, v in element.items():
            if k == 'tags':
                for name in v:
                    all_tags+= v
    all_tags_set = set(all_tags)
    assert 'fun' in all_tags_set