#!/usr/bin/python3
"""
listing top ten titles
"""
import requests


def top_ten(subreddit):
    """ function to list titles """
    url = 'https://www.reddit.com/r/{}/hot.json'
    complete_url = url.format(subreddit)
    headers = {'User-Agent': 'python'}
    response = requests.get(complete_url, headers=headers,
                            params={'limit': 10}, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        for post in data['data']['children']:
            print('{}'.format(post['data']['title']))
