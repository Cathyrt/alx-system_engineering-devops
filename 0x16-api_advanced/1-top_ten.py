#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Retrieves the title of the top ten posts from a given subreddit."""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    res = requests.get(url, headers=header,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        print('None')
        return
    data = res.json()
    hot_posts = data['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
