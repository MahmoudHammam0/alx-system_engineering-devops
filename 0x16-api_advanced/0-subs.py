#!/usr/bin/python3
"number of subscribers for a given subreddit"
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    clientId = 'J2BkSoEGIIGkNRe4aVwAnw'
    secretKey = 'sKObr2oIPuhq88fqo2U1_TDeOu42eA'
    auth = requests.auth.HTTPBasicAuth(clientId, secretKey)
    data = {
        'grant_type': 'password',
        'username': 'Mahmoudhammam',
        'password': '0170398745Mh'
    }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    token = res.json()['access_token']
    headers['Authorization'] = 'bearer {}'.format(token)
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, auth=auth, data=data, headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    if 'data' not in data:
        return 0
    if 'subscribers' not in data.get('data'):
        return 0
    return data['data']['subscribers']
