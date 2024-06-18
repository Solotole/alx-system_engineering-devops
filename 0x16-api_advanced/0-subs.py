#!/usr/bin/python3
"""
module that counts number of reddit subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ counting number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'
    complete_url = url.format(subreddit)
    headers = {'User-Agent': 'Custom'}
    response = requests.get(complete_url,
                            headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    elif response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
