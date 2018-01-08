#!/usr/bin/python3
"""Function to GET the top 10 hot posts in the given `subreddit`"""
from requests import get


def top_ten(subreddit):
    """Use GET request to find the top 10 hot posts in `subreddit`"""
    r = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
            params={"raw_json": 1, "limit": 10, "g": "GLOBAL"},
            headers={"User-Agent": "Andrew from Holberton"},
            allow_redirects=False)

    try:
        r.raise_for_status()
    except:
        print("None")
    else:
        try:
            children = r.json().get('data').get('children')
            for child in children:
                print(child.get('data').get('title'))
        except:
            print("None")
