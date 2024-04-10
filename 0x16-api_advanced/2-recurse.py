#!/usr/bin/python3
'Top Ten module'
import requests


def recurse(subreddit, hot_list=[], i=0):
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
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, auth=auth, data=data, headers=headers,
            allow_redirects=False)
    if req.status_code != 200:
        return None
    res = req.json()['data']['children']
    if len(hot_list) < len(res):
        hot_list.append(res[i]['data']['title'])
        i += 1
        return recurse(subreddit, hot_list, i)
    else:
        return hot_list
