#!/usr/bin/python3
"""
uses a REST API, for a given employee ID, returns information about
his/her TODO list progress and export to json format
"""
import json
import requests
import sys

def todo_list():
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todo = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w") as file:
        json.dump({sys.argv[1]: [{"tasks": task.get('title'),
                                  "completed": task.get('completed'),
                                  "username": employee.get('username')}
                                  for task in todo]}, file)

if __name__ == '__main__':
    todo_list()
