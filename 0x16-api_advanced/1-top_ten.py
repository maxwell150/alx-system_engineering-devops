#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
https://www.reddit.com/r/programming/hot/.json&limit=10
"""
import json
import requests


def top_ten(subreddit):
    """Return Top10 subreddit"""
    url = "https://www.reddit.com/r/"
    url = url + subreddit + "/hot/.json?limit=10"

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '149@holbertonschool.com'
    }
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        result = result.json()
        children = result.get('data').get('children')
        for i in range(10):
            title = children[i].get('data').get('title')
            print("{}".format(title))
    else:
        print("None")
