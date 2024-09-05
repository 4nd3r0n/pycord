import requests
import random

def waifu() -> dict:
    send = {'img': '', 'name': '', 'description': '', 'tag': ''}
    tags = ['maid', 'waifu', 'oppai', 'selfies', 'uniform']
    tag = random.choice(tags)

    response = requests.get(url='https://api.waifu.im/search',
        params={'included_tags': [tag], 'height': '>=2000'},
        headers={'Accept-Version': 'v6'}
    )

    if response.status_code == 200:
        data = response.json()

        send['name'] = data['images'][0]['tags'][0]['name']
        send['description'] = data['images'][0]['tags'][0]['description']
        send['img'] = data['images'][0]['url']
        send['tag'] = tag
    else:
        print('Request failed with status code:', response.status_code)

    return send
