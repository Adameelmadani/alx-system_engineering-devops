#!/usr/bin/python3
"""
This is our module
"""
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_r = requests.get(users_url)
    users_json = users_r.json()

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_r = requests.get(todo_url)
    todo_json = todo_r.json()

    file_name = "todo_all_employees.json"
    json_dict = {}
    for user_json in users_json:
        t_list = []
        user_name = user_json.get('username')
        user_id = user_json.get('id')
        for do in todo_json:
            if do.get('userId') == user_id:
                t_dict = {}
                t_dict['username'] = user_name
                t_dict['task'] = do.get('title')
                t_dict['completed'] = do.get('completed')
                t_list.append(t_dict)
        json_dict[user_id] = t_list

    with open(file_name, "w") as file:
        json.dump(json_dict, file)
