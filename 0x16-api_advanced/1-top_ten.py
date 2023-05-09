#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Retrieves the title of the top ten posts from a given subreddit."""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=header, allow_redirects=False)
    inf = res.json().get('data', {}).get('children', {})
    if res.status_code != 200:
        return print('None')
    for x in inf[0:10]:
        print(x.get('data', {}).get('title'))
