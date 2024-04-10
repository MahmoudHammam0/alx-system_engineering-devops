#!/usr/bin/python3
'2. Recurse it!'
import requests


def recurse(subreddit, hot_list=[], next=None):
    'returns a list of titles of all hot articles for a given subreddit'
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
    params = {'after': next}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, auth=auth, data=data, headers=headers,
                       allow_redirects=False, params=params)
    if req.status_code != 200:
        return None
    data = req.json()['data']
    articles = data['children']
    next = data['after']
    for article in articles:
        hot_list.append(article['data']['title'])
    if next:
        return recurse(subreddit, hot_list, next)
    else:
        return hot_list
