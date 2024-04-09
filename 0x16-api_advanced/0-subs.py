#!/usr/bin/python3
"number of subscribers for a given subreddit"
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    user_agent = {'User-agent': 'Google Chrome'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    results = response.json()
    try:
        return results.get('data').get('subscribers')

    except Exception as e:
        return 0
