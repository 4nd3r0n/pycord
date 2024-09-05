from os import name
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
        names: list = []
        descs: list = []

        send['img'] = data['images'][0]['url']
        for i in range(len(data['images'][0]['tags'])):
            descs.append(data['images'][0]['tags'][i]['description'])
            names.append(data['images'][0]['tags'][i]['name'])
        send['description'] = ', '.join(descs)
        send['name'] = ', '.join(names)
        send['tag'] = tag
    else:
        print('Request failed with status code:', response.status_code)

    return send
