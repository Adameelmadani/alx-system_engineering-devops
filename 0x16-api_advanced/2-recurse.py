#!/usr/bin/python3
"""
This is our model
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    This is our function
    """
    url = "https://www.reddit.com/r/{}/json?after={}".format(subreddit, after)
    r = requests.get(url)
    if r.status_code == 404:
        return None
    r_json = r.json()
    ch_list = r_json.get("data").get("children")
    for i in range(0, len(ch_list)):
        ch_list[i] = ch_list[i].get("data").get("title")
    hot_list += ch_list
    if r_json.get("data").get("after", None):
        return recurse(subreddit, hot_list, r_json.get("data").get("after"))
    return hot_list
