#!/usr/bin/python3
"""
This is our module
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_name = requests.get(user_url).json().get('name')

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_json = requests.get(todo_url).json()

    tasks = []
    n_d = 0
    n = 0
    for do in todo_json:
        if do.get('userId') == int(user_id):
            if do.get('completed') is True:
                tasks.append(do.get('title'))
                n_d += 1
            n += 1

    f_str = "Employee {} is done with tasks({}/{}):".format(user_name, n_d, n)
    print(f_str)
    for task in tasks:
        print("\t {}".format(task))
