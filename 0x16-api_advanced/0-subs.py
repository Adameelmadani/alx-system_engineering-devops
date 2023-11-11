#!/usr/bin/python3
"""
This is our model
"""
import requests


def number_of_subscribers(subreddit):
    """
    This is our function
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url)
    if r.status_code == 404:
        return 0
    r_json = r.json()
    return r_json.get("data").get("subscribers")
