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
    r_json = r.json()
    ch_lists = r_json.get("data").get("children")
    for ch_list in ch_lists:
        print(ch_list.get("data").get("title"))
