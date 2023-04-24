#!/usr/bin/python3
"""
Given an Employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    Id = argv[1]
    user_t = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                          format(Id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(Id), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
