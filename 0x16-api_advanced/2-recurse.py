#!/usr/bin/python3
"""
recursive pagination
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ fuction to return listings in recursion """
    url = 'https://www.reddit.com/r/{}/hot.json'
    complete_url = url.format(subreddit)
    headers = {'User-Agent': 'Custom'}
    response = requests.get(complete_url, headers=headers,
                            params={'after': after}, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for datas in data['data']['children']:
            hot_list.append(datas['data']['title'])
        after = response.json().get('data').get('after')

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
