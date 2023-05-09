#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the total number of subscribers for a given subreddit."""
    url = 'http://reddit.com/r/{}/about.json'
    header = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url.format(subreddit), headers=header)
    if res.status_code != 200:
        return 0
    return res.json().get('data', {}).get('subscribers', 0)
