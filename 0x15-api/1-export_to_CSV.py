#!/usr/bin/python3
"""
This is our module
"""
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

    file_name = "{}.csv".format(user_id)
    lines = []
    for do in todo_json:
        if do.get('userId') == user_id:
            line = "\"{}\",\"{}\",\"{}\",\"{}\"".format(user_id, user_name,
                    do.get('completed'), do.get('title'))
            lines.append(line)

    with open(file_name, "w") as file:
        for i in range(0, len(lines)):
            file.write(lines[i])
            if i != len(lines) - 1:
                file.write("\n")
