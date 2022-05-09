#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import json
import requests


def recurse(subreddit, hot_list=[], params={}):
    """Find hot subreddit article titles using recursion"""
    payload = {}

    url = "https://www.reddit.com/r/"
    url = url + subreddit + "/hot/.json?limit=100"

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '149 at Holberton'
    }
    result = requests.get(url, headers=headers, params=params)
    title = []
    if not result.status_code == 200:
        return None
    result = result.json()
    children = result.get('data').get('children')
    numChildren = len(children)
    for i in range(numChildren):
        if children[i].get('data').get('title'):
            title.append(children[i].get('data').get('title'))
            hot_list.append(title)
        else:
            return
    after = result.get('data').get('after')
    if after is None:
        return hot_list
    else:
        payload = {"after": after}
        recurse(subreddit, hot_list, payload)
        return hot_list
