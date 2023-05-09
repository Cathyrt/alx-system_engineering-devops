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
    limits = {'limit': '10'}

    res = requests.get(url, headers=header,
                       params=limits, allow_redirects=False)
    if res.status_code != 200:
        print('None')
    else:
        res_json = res.json()

        if res_json.get('data') and res_json.get('data').get('children'):
            hot_posts = res_json.get('data').get('children')
            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
