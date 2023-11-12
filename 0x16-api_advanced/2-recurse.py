#!/usr/bin/python3
"""
This is our model
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    This is our function
    """
    if subreddit is None:
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}
    r = requests.get(url, params={"after": after}, headers=user_agent)
    if r.status_code == 200:
        r_json = r.json()
        after = r_json.get("data").get("after")
        if not after:
            return hot_list
        ch_list = r_json.get("data").get("children")
        for ch_l in ch_list:
            hot_list.append(ch_l.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
