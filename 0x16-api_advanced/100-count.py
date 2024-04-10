#!/usr/bin/python3
'Count it!'
import requests


def count_words(subreddit, word_list, next=None, word_count=None):
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
    if word_count is None:
        word_count = {}
    data = req.json()['data']
    articles = data['children']
    next = data['after']
    for article in articles:
        title = article['data']['title'].lower()
        words = set(title.split())
        for word in word_list:
            word = word.lower()
            if word in words:
                count = word_count.get(word, 0)
                word_count[word] = count + 1
    if next:
        return count_words(subreddit, word_list, next, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
