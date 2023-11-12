#!/usr/bin/python3
"""
This is our model
"""
import requests


def recurse(subreddit, hot_list=[], c=0):
    """
    This is our function
    """
    if c == 0:
        url = "https://www.reddit.com/r/{}.json".format(subreddit)
        r = requests.get(url)
        if r.status_code == 404:
            return None
        r_json = r.json()
        ch_lists = r_json.get("data").get("children")
        if len(ch_lists) > c:
            ch_lists[c] = ch_lists[c].get("data").get("title")
            return recurse(subreddit, ch_lists, 1)
        return None
    else:
        if len(hot_list) > c:
            hot_list[c] = hot_list[c].get("data").get("title")
            return recurse(subreddit, hot_list, c = c + 1)
        else:
            return (hot_list)
