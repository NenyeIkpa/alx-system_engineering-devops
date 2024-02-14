#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """returns the num of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/nenyeikpa_tech_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
