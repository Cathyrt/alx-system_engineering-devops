#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a
given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Retrieves a list of hot posts from a given subreddit."""
    url = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-agent': 'Mozilla/5.0'}
    limit = {'limit': 100}
    if isinstance(after, str):
        if after != 'STOP':
            limit['after'] = after
        else:
            return hot_list
    res = requests.get(url, headers=header,
                       params=limit)
    if res.status_code != 200:
        return None
    data = res.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = 'STOP'
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
