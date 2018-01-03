#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import sys
import requests


user_endpoint = "https://jsonplaceholder.typicode.com/users/"


def get_todos_by_userid(user_id):
    """Get TODO list for a user identified by `user_id`"""
    todos = requests.get(user_endpoint + user_id + '/todos')
    if todos.status_code == 200:
        return todos.json()
    else:
        exit(1)


def get_name_by_userid(user_id):
    """Get the full name of auser identified by `user_id`"""
    user = requests.get(user_endpoint + user_id)
    if user.status_code == 200:
        return user.json()
    else:
        exit(1)


def format_user_todos(user_id):
    """Format employee TODO list as a string"""
    todos = get_todos_by_userid(user_id)
    complete = list(filter(lambda t: t.get('completed') is True, todos))
    name = get_name_by_userid(user_id).get('name')
    output = "Employee {} is done with tasks({}/{}):\n\t".format(name,
                                                                 len(complete),
                                                                 len(todos))
    output += '\n\t'.join(map(lambda c: c.get('title', ''), complete))
    return output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    user_id = sys.argv[1]
    print(format_user_todos(user_id))
