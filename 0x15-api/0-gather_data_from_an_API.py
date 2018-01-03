#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import requests
import sys


user_endpoint = "https://jsonplaceholder.typicode.com/users/"


def get_todos_by_userid(user_id):
    """Get TODO list for a user identified by `user_id`"""
    todos = requests.get(user_endpoint + user_id + '/todos')
    try:
        todos.raise_for_status()
        return todos.json()
    except:
        exit(1)


def get_user_by_userid(user_id):
    """Get user identified by `user_id`"""
    user = requests.get(user_endpoint + user_id)
    try:
        user.raise_for_status()
        return user.json()
    except:
        exit(1)


def format_user_todos(user_id):
    """Format employee TODO list as a string"""
    todos = get_todos_by_userid(user_id)
    completed = list(filter(lambda t: t.get('completed') is True, todos))
    name = get_user_by_userid(user_id).get('name')
    output = "Employee {} is done with tasks({}/{}):".format(name,
                                                             len(completed),
                                                             len(todos))
    titles = '\n\t '.join(map(lambda c: c.get('title', ''), completed))
    if not titles:
        return output
    return output + '\n\t ' + titles


if __name__ == "__main__":
    """Get user_id as command line parameter and print out the completed
    tasks for the user associated with that id"""
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    user_id = sys.argv[1]
    print(format_user_todos(user_id))
