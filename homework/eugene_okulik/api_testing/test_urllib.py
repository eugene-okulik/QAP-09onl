import json
from urllib import request, error


def test_get_all_posts(base_url):
    req = request.Request(f'{base_url}/posts')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    # print(response)
    assert len(response) == 100


def test_get_one_post(base_url):
    req = request.Request(f'{base_url}/posts/15')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert response['id'] == 15


def test_create_post(base_url):
    req = request.Request(f'{base_url}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    data_json = {
        "title": "ashdkfjashdlkfjahlkdshafd",
        "body": "ksdhfkjshdlkfhsdfkjhs",
        "userId": 1,
        "id": 101
    }
    req.data = json.dumps(data_json).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert response['title'] == 'ashdkfjashdlkfjahlkdshafd'


def test_delete_post(base_url):
    req = request.Request(f'{base_url}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    data_json = {
        "title": "ashdkfjashdlkfjahlkdshafd",
        "body": "ksdhfkjshdlkfhsdfkjhs",
        "userId": 1
    }
    req.data = json.dumps(data_json).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    post_id = response['id']
    req = request.Request(f'{base_url}/posts/{post_id}')
    req.method = 'DELETE'
    request.urlopen(req)
    req = request.Request(f'{base_url}/posts/15')
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        assert err.code == 404
    else:
        assert False, 'Deleted post is not deleted'

