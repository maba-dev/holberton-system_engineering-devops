#!/usr/bin/python3
""" a function that queries the Reddit and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    subs = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-Agent': 'cherif'}
    )
    if subs.status_code == 404:
        return 0
    subs = subs.json()
    return (subs.get('data').get('subscribers'))
