#!/usr/bin/python3


import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    subs = requests.get('https://www.reddit.com/r/{}/hot.json'
                        .format(subreddit),
                        params={'count': count, 'after': after},
                        headers={'User-Agent': 'cherif'},
                        allow_redirects=False
                        )
    if subs.status_code == 404:
        return None

    subs = subs.json()
    hot = hot_list + [
        i.get('data').get('title') for i in subs.get('data').get('children')
        ]

    if not subs.get('data').get('after'):
        return hot

    return recurse(subreddit, hot, subs.get('data').get('count'),
                   subs.get('data').get('after'))
