#!/usr/bin/python3
"""a function that queries the API and prints the titles of the first 10 hot"""


import requests


def top_ten(subreddit):
    """ define a function"""
    subs = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers={'User-Agent': 'cherif'}
    )
    if subs.status_code == 404:
        print("None")
    subs = subs.json()
    data = subs.get('data').get('children')
    for i in data[:10]:
        print(i['data']['title'])
