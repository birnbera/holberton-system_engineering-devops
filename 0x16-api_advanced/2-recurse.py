#!/usr/bin/python3
"""Function to recursively GET all the hot posts of a give subreddit"""
from requests import get


def recurse(subreddit, hot_posts=[], after=None):
    """Recursively GET all the hot posts of `subreddit`"""
    r = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
            params={"raw_json": 1, "g": "GLOBAL", "after": after},
            headers={"User-Agent": "Andrew from Holberton"},
            allow_redirects=False)
    try:
        r.raise_for_status()
    except:
        return None
    else:
        try:
            children = r.json().get('data').get('children')
            hot_posts.extend(map(lambda c: c.get('data').get('title'),
                                 children))
            after = r.json().get('data').get('after')
            if after is None:
                return hot_posts
            else:
                return recurse(subreddit, hot_posts, after=after)
        except:
            return None
