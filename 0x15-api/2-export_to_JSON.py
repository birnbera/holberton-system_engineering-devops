#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import json
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


def export_json_user_todos(user_id):
    """Export employee TODO list to a json file"""
    todos = get_todos_by_userid(user_id)
    username = get_user_by_userid(user_id).get('username')
    data = {user_id: [dict(task=todo.get('title'),
                           completed=todo.get('completed'),
                           username=username)
                      for todo in todos]}
    with open("{}.json".format(user_id), 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    """Get user_id as command line parameter and return the completed
    tasks for the user associated with that id as json file"""
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    user_id = sys.argv[1]
    export_json_user_todos(user_id)
