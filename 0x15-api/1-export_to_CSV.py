#!/usr/bin/python3
import csv
import requests
from sys import argv


if __name__ == "__main__":
    USERNAME = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()['username']
    USER_ID =  requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()['id']

    response = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1]))


    f = open('{}.csv'.format(USER_ID), 'w')
    employee_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for i in response.json():
        employee_writer.writerow([USER_ID, USERNAME, i["completed"], i["title"]])
    f.close()