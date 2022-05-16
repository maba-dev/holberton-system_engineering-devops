#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID"""
import requests
from sys import argv


if __name__ == "__main__":
    api_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1]))
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()['name']

    response = requests.get(api_url)

    number_of_completed_tasks = 0
    total_number_of_asks = 0
    title_tab = []
    for i in response.json():
        total_number_of_asks += 1
        if i['completed']:
            number_of_completed_tasks += 1
            title_tab.append(i['title'])
    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
        name, number_of_completed_tasks, total_number_of_asks))
    for j in title_tab:
        print("\t {}".format(j))
