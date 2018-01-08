#!/usr/bin/python3
"""Function to GET number of subscribers for a given subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """Use GET request to find number of subscribers to `subreddit`"""
    r = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
            params={"raw_json": 1},
            headers={"User-Agent": "Andrew from Holberton"},
            allow_redirects=False)

    try:
        r.raise_for_status()
    except:
        return 0
    else:
        num_subscribers = r.json().get('data').get('subscribers')
        if num_subscribers is None:
            return 0
        return num_subscribers
