#!/usr/bin/python3
"""function to query subscribers given a subreddit as arg"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    redditApi = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'just-max'}
    res = requests.get(redditApi, headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json()['data']['subscribers']
    return results
