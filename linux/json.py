import json
import time
import requests
server_url = 'http://your-server-url.com'

while True:
    with open('payload.json', 'r') as file:
        data = json.load(file)
    response = requests.post(server_url, json=data)
    print('Status code:', response.status_code)
    print('Response:', response.text)
    time.sleep(10)
