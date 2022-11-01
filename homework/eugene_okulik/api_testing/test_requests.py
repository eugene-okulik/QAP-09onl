import requests
import json


def test_get_all_posts(base_url):
    response = requests.request('GET', f'{base_url}/posts').json()
    # print(response)
    assert len(response) == 100


def test_one_post(base_url):
    response = requests.request('GET', f'{base_url}/posts/15').json()
    assert response['id'] == 15


def test_create_post(base_url):
    headers = {
        'Content-Type': 'application/json',
    }
    data_json = {
        "title": "ashdkfjashdlkfjahlkdshafd",
        "body": "ksdhfkjshdlkfhsdfkjhs",
        "userId": 1,
        "id": 101
    }
    data = json.dumps(data_json)
    response = requests.request(
        'POST',
        f'{base_url}/posts',
        headers=headers,
        data=data
    ).json()
    assert response['title'] == 'ashdkfjashdlkfjahlkdshafd'


def test_update_post(base_url):
    headers = {
        'Content-Type': 'application/json',
    }
    data_json = {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum - updated",
        "body": "quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error"
    }
    data = json.dumps(data_json)
    response = requests.request(
        'PUT',
        f'{base_url}/posts/10',
        headers=headers,
        data=data
    ).json()
    assert response['title'] == 'optio molestias id quia eum - updated'


def test_delete_post(base_url, create_a_post):
    post_id = create_a_post
    requests.request('DELETE', f'{base_url}/posts/{post_id}')
    response = requests.request('GET', f'{base_url}/posts/{post_id}')
    assert response.status_code == 404, 'Deleted post is not deleted'
