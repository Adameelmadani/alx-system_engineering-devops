#!/usr/bin/python3
"""
This is our module
"""
import sys
import requests


user_id = int(sys.argv[1])
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
user_r = requests.get(user_url)
user_json = user_r.json()

todo_url = "https://jsonplaceholder.typicode.com/todos"
todo_r = requests.get(todo_url)
todo_json = todo_r.json()

user_name = user_json.get('name')

tasks = []
n_done = 0
n = 0
for do in todo_json:
    if do.get('userId') == user_id:
        if do.get('completed') is True:
            tasks.append(do.get('title'))
            n_done += 1
        n += 1

f_str = "Employee {} is done with tasks({}/{}):".format(user_name, n_done, n)
print(f_str)
for task in tasks:
    print("\t {}".format(task))
