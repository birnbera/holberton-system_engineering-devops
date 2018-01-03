#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import csv
import requests
import sys


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


def format_user_todos(user_id):
    """Format employee TODO list as a string"""
    todos = get_todos_by_userid(user_id)
    complete = list(filter(lambda t: t.get('completed') is True, todos))
    name = get_user_by_userid(user_id).get('name')
    output = "Employee {} is done with tasks({}/{}):\n\t".format(name,
                                                                 len(complete),
                                                                 len(todos))
    output += '\n\t'.join(map(lambda c: c.get('title'), complete))
    return output


def export_csv_user_todos(user_id):
    """Export employee TODO list to a csv file"""
    todos = get_todos_by_userid(user_id)
    username = get_user_by_userid(user_id).get('username')
    data = [dict(userId=user_id,
                 username=username,
                 completed=todo.get('completed'),
                 title=todo.get('title'))
            for todo in todos]
    with open("{}.csv".format(user_id), 'w', newline="") as f:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(f,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    user_id = sys.argv[1]
    export_csv_user_todos(user_id)
