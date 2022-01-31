#!/usr/bin/python3
"""
uses a REST API, for a given employee ID, returns information about
his/her TODO list progress and export to dictionary of list of dictionaries
"""
import json
import requests

def todo_list():
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + 'users').json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            employee.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username")
            } for task in requests.get(url + "todos",
                                    params={"userId": employee.get("id")}).json()]
            for employee in employees}, jsonfile)

if __name__ == '__main__':
    todo_list()
