#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function returns 0
    """
    CLIENT_ID = 'zL8evAsF03DzVk_TArVH3g'
    SECRET_KEY = 'FT7BTQs-WLEtZEOlH_2mE2QEQ8CV2g'

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {
        'grant_type': 'password',
        'username': 'Responsible-Big4336',
        'password': 'password123'
    }

    headers = {'User-Agent': 'MyAPI1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']

    headers['Authorization'] = "bearer {}".format(TOKEN)

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, auth=auth, data=data, headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return 0
    d = response.json()
    if 'data' not in d:
        return 0
    if 'subscribers' not in d.get('data'):
        return 0

    return d['data']['subscribers']
