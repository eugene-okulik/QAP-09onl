import docker
import requests
from requests.exceptions import ConnectionError
from time import sleep


client = docker.from_env()
container_id = client.containers.run(
    "eokulik/cool_web_app",
    detach=True,
    ports={
        '8080/tcp': 8080
    },
    remove=True,
    name="web_app"
)
# print(container_id.id)
# print(client.containers.list())
container = client.containers.get(container_id.id)
print(container.logs())
# sleep(5)
response = ''
while True:
    try:
        response = requests.request('GET', 'http://localhost:8080')
        break
    except ConnectionError:
        continue
print(container.logs())
print(response.text)
container.stop()