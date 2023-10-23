#!/usr/bin/python3
"""
This is our module
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_r = requests.get(user_url)
    user_json = user_r.json()

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_r = requests.get(todo_url)
    todo_json = todo_r.json()

    user_name = user_json.get('username')

    file_name = "{}.json".format(user_id)
    t_list = []
    for do in todo_json:
        if do.get('userId') == user_id:
            t_dict = {}
            t_dict['task'] = do.get('title')
            t_dict['completed'] = do.get('completed')
            t_dict['username'] = user_name
            t_list.append(t_dict)
    json_dict = {user_id: t_list}

    with open(file_name, "w") as file:
        json.dump(json_dict, file)
