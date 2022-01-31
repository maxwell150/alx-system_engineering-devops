#!/usr/bin/python3
"""
uses a REST API, for a given employee ID, returns information about
his/her TODO list progress and exports it to a csv format
"""
import csv
import requests
import sys

def todo_list():
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todo = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([int(sys.argv[1]), employee.get('username'),
                            task.get('completed'),
                            task.get('title')])


if __name__ == '__main__':
    todo_list()
