#!/usr/bin/python3
"""Reddit API"""


import requests


def recurse(subreddit, hot_list=[], after=''):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:app:v0.0.0 (by /u/Any_Manager_3702)"
    }
    params = {
        'after': after
    }
    subs = requests.get(
        url, headers=headers, params=params, allow_redirects=False
        )

    if subs.status_code == 404:
        return(None)
    elif after is None:
        return
    response = subs.json().get('data').get('children')

    for childrens in response:
        hot_list.append(childrens.get('data').get('title'))
    after = subs.json().get('data').get('after')
    recurse(subreddit, hot_list=hot_list, after=after)
    return hot_list
