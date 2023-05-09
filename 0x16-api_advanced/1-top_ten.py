#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Retrieves the title of the top ten posts from a given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {"User-agent": "Mozilla/5.0"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        for child in data['data']['children']:
            print(child['data']['title'])
