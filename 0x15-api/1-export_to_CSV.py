#!/usr/bin/python3
"""
Export data from an API to CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    Id = argv[1]
    user_t = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                          format(Id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(Id), verify=False).json()
    with open("{}.csv".format(Id), 'w', newline='') as cfile:
        taskwriter = csv.writer(cfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(Id), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
