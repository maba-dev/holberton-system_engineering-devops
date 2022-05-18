#!/usr/bin/python3
"""  Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    USERNAME = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    ).json()['username']
    USER_ID = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    ).json()['id']
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    )
    Dict = {USER_ID: []}
    for i in response.json():
        Dict[USER_ID].append({
            "task": i["title"],
            "completed": i["completed"],
            "username": USERNAME,
        })
    f = open('{}.json'.format(USER_ID), 'w')
    json.dump(Dict, f)
    f.close()
