#!/usr/bin/python3
"""  Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    USERNAME = requests.get(
        'https://jsonplaceholder.typicode.com/users'
        )
    USER_ID = requests.get(
        'https://jsonplaceholder.typicode.com/users/'
    ).json()
    Dict = {}
    for i in USER_ID:
        userId = i["id"]
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                userId
            )
        )

        Dict[str(i["id"])] = []
        for j in response.json():
            Dict[str(i["id"])].append({
                "username": i["username"],
                "task": j["title"],
                "completed": j["completed"]
            })

    f = open('todo_all_employees.json', 'w')
    json.dump(Dict, f)
    f.close()
