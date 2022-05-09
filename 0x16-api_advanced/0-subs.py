#!/usr/bin/python3
"""function to query subscribers given a subreddit as arg"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/"
    url = url + subreddit + "/about/.json"

    headers = {
        'User-Agent': 'just_max',
        'From': 'max@holbertonschool.com'
    }
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        result = result.json()
        return result['data']['subscribers']
    else:
        return 0
