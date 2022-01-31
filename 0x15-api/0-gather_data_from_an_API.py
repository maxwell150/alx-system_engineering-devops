#!/usr/bin/python3
"""
uses a REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
import sys

def todo_list():
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todo = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    complete_tasks = []
    for task in todo:
        if task.get('completed') is True:
            complete_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'), len(complete_tasks),len(todo)))
    [print("\t {}".format(complete)) for complete in complete_tasks]

if __name__ == '__main__':
    todo_list()
