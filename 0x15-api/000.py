#!/usr/bin/python3
"""
    Gather data from an API
"""
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            userId = int(sys.argv[1])
            response_user = requests.get(
                    '{}/users/{}'.format(API, userId)
                    ).json()
            response_todos = requests.get(
                    '{}/todos'.format(API)
                    ).json()
            name = response_user.get('name')
            todos = list(
                    filter(lambda x: x.get('userId') == userId, response_todos)
                    )
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
