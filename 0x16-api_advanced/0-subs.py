#!/usr/bin/python3
"""
Query Reddit API for the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    Return 0 if an invalid subreddit is given.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom user agent
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers')
        if subscribers is not None:
            return subscribers
    return 0
