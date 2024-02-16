#!/usr/bin/python3
"""
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""


import requests

def number_of_subscribers(subreddit):
    """returns the num of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
        
    # Reddit API URL for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": ""0x16-api_advanced:project:\
v1.0.0 (by /u/nenyeikpa)}.json()

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and return the number of subscribers
            subreddit_data = response.json().get("data")
            subscribers = subreddit_data.get("subscribers")
            return subscribers
        else:
            # Return 0 for invalid subreddit or other errors
            return 0
    except Exception as e:
        # Handle exceptions (e.g., network errors) and return 0
        print(f"Error: {e}")
        return 0
