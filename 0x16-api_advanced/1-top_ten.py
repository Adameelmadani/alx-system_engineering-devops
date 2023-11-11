#!/usr/bin/python3
"""
This is our model
"""
import requests


def top_ten(subreddit):
    """
    This is our function
    """
    url = "https://www.reddit.com/r/{}.json?limit=10".format(subreddit)
    r = requests.get(url)
    if r.status_code == 404:
        print("None")
        return
    """r_json = r.json()
    ch_list = r_json.get("data").get("children")
    for i in range(1, 11):
        print(ch_list[i].get("data").get("title"))"""
    print("OK")
