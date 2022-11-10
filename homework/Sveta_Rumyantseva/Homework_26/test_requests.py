import json
import requests


def test_existing_meme(base_url, check_token):
    headers = {'Authorization': check_token}
    response = requests.request('GET', f"{base_url}/meme", headers=headers).json()
    for my_dict in response['data']:
        for key in my_dict.keys():
            if key == 'tags':
                for val in my_dict['tags']:
                    if val == 'fun':
                        assert val == 'fun'


def test_get_one_meme(base_url, check_token):
    headers = {'Authorization': check_token}
    response = requests.request('GET', f"{base_url}/meme/3", headers=headers).json()
    assert response['id'] == 3


def test_get_all_meme(base_url, check_token):
    headers = {'Authorization': check_token}
    response = requests.request('GET', f"{base_url}/meme", headers=headers)
    assert response.status_code == 200


def test_create_meme(base_url, check_token):
    headers = {'Content-Type': 'application/json', 'Authorization': f"{check_token}"}
    data_json = {
        'text': "Do you prepare to zoom's meeting? :)",
        'url': 'https://i.kym-cdn.com/photos/images/newsfeed/001/965/115/01b.jpg',
        'tags': ['zoom', 'meeting', 'computer', 'fun'],
        'info': {'object': ['dog', 'animal']}
    }
    data = json.dumps(data_json)
    response = requests.request("POST", f"{base_url}/meme", headers=headers, data=data).json()
    assert response['text'] == "Do you prepare to zoom's meeting? :)"


def test_update_meme(base_url, create_a_meme, check_token):
    meme_id = create_a_meme
    # print('\nCreated meme with id=', meme_id)
    headers = {'Content-Type': 'application/json', 'Authorization': check_token}
    data_json = {
        'id': meme_id,
        'text': "Funny zoom's meeting :)",
        'url': "https://i.kym-cdn.com/photos/images/newsfeed/001/965/115/01b.jpg",
        'tags': ['zoom', 'meeting', 'computer', 'fun'],
        'info': {'object': ['dog', 'animal']}
    }
    data = json.dumps(data_json)
    response = requests.request("PUT", f"{base_url}/meme/{meme_id}", headers=headers, data=data).json()
    # print('\nresponse after PUT=', response)

    assert response['text'] == "Funny zoom's meeting :)"
    assert response['url'] == "https://i.kym-cdn.com/photos/images/newsfeed/001/965/115/01b.jpg"
    assert response['tags'] == ['zoom', 'meeting', 'computer', 'fun']
    assert response['info'] == {'object': ['dog', 'animal']}


def test_delete_post(base_url, create_a_meme, check_token):
    meme_id = create_a_meme
    # print(f"\n Created meme_id={meme_id}")
    headers = {'Authorization': check_token}
    requests.request("DELETE", f"{base_url}/meme/{meme_id}", headers=headers)
    response = requests.request("GET", f"{base_url}/meme/{meme_id}", headers=headers)
    assert response.status_code == 404, 'The meme is not deleted'
