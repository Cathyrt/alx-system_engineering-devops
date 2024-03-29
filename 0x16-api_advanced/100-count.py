#!/usr/bin/python3
"""
Function parses the title of all hot articles
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after='', word_count={}):
    header = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
    }
    url = "https://www.reddit.com/r/{}/hot/.json?limit=100&after={}".format(
            subreddit, after)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        for child in data['data']['children']:
            title = child['data']['title'].lower()
            for word in word_list:
                if word in title:
                    word_count[word] = word_count.get(word, 0) + 1
        if data['data']['after']:
            return count_words(
                    subreddit, word_list, data['data']['after'], word_count)
        else:
            return sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    else:
        return None
