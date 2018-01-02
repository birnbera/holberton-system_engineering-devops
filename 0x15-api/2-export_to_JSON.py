#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import sys
import json
import requests


todo_endpoint = "https://jsonplaceholder.typicode.com/todos"
user_endpoint = "https://jsonplaceholder.typicode.com/users"


def get_todos_by_userid(user_id):
    """Get TODO list for a user identified by `user_id`"""
    payload = {'userId': user_id}
    todos = requests.get(todo_endpoint, params=payload)
    try:
        return todos.json()
    except:
        exit(1)


def get_user_by_userid(user_id):
    """Get the username of auser identified by `user_id`"""
    payload = {'id': user_id}
    user = requests.get(user_endpoint, params=payload)
    try:
        return user.json()[0]
    except:
        exit(1)


def export_json_user_todos(user_id):
    """Export employee TODO list to a csv file"""
    todos = get_todos_by_userid(user_id)
    username = get_user_by_userid(user_id).get('username')
    data = {user_id: [dict(task=todo.get('title'),
                           completed=todo.get('completed'),
                           username=username)
                      for todo in todos]}
    with open("{}.json".format(user_id), 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    user_id = sys.argv[1]
    export_json_user_todos(user_id)
