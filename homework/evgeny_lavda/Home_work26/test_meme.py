import requests
import json


def test_get_all_post(base_url, user_authorization):
    headers = {
        "Authorization": f'{user_authorization}'
    }
    response = requests.request(
        'GET',
        f'{base_url}/meme',
        headers=headers
    ).json()
    meme_tag_list = []
    for meme in range(len(response['data'])):
        tags = (response['data'][meme])
        # print(type(tags['tags']))
        for i in tags['tags']:
            # print(type(i))
            meme_tag_list.append(i)
    assert 'fun' in meme_tag_list, 'tag fun is not found'


def test_create_meme(base_url, user_authorization):
    headers = {
        'Authorization': f'{user_authorization}',
        'Content-Type': 'application/json'
    }

    data_json = {
        "text": "как я разбираюсь в собаках",
        "url": "https://cs14.pikabu.ru/post_img/2022/11/10/8/1668087866112982105.jpg",
        "tags": ["fun", "dogs", 'fundogs'],
        "info": {"colors": ["orange", "white", "red"], "objects": ["picture", "text"]}
    }

    data = json.dumps(data_json)

    response = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=headers,
        data=data).json()

    assert response['text'] == "как я разбираюсь в собаках"


def test_update_meme(base_url, create_a_meme, user_authorization):
    meme_id = create_a_meme

    headers = {
        'Content-Type': 'application/json',
        'Authorization': user_authorization
    }

    data_json = {
        'id': meme_id,
        'text': "This is the base",
        'url': "https://memepedia.ru/wp-content/uploads/2017/04/%D0%A3%D0%BF%D1%8F%D1%87%D0%BA%D0%B0%D0%BC%D0%B5%D0%BD.png",
        'tags': ['fun', 'oldmeme', 'onotole', 'retro'],
        'info': {'object': ['yp4ka', 'meme']}
    }
    data = json.dumps(data_json)
    response = requests.request("PUT", f"{base_url}/meme/{meme_id}", headers=headers, data=data).json()
    assert response["tags"] == ['fun', 'oldmeme', 'onotole', 'retro']


def test_delete_post(base_url, create_a_meme, user_authorization):
    meme_id = create_a_meme
    headers = {'Authorization': user_authorization}

    requests.request(
        "DELETE",
        f"{base_url}/meme/{meme_id}",
        headers=headers)

    response = requests.request(
        "GET",
        f"{base_url}/meme/{meme_id}",
        headers=headers
    )
    assert response.status_code == 404, 'The meme was not removed'
