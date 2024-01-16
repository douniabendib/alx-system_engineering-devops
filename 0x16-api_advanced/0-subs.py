#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
import request


def number_of_subscribers(subreddit):
    """fct that return subreddit or 0 if invalid""" 
    url = f"https://www.reddit.com/r/{}/about.json"

    # Get user agent
    # Reference: https://stackoverflow.com/questions/10606133/
    # sending-user-agent-using-requests-library-in-python
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    
    resp = requests.get(url, headers=headers).json()
    subscribers = resp.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
