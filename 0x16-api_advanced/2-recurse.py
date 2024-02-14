#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all
hot articles for a given subreddit or None
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/nenyeikpa_tech_jr)"
    }
    titles = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, titles=titles,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
