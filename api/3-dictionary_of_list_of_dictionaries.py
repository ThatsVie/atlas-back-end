#!/usr/bin/python3
"""
This script retrieves tasks from all employees and
exports the data in JSON format.

"""
import json
import requests
import sys


def retrieve_employee_name(employee_id):
    """
    Retrieves the name of the employee.
    """
    url = "{}/{}".format(base_url, employee_id)
    response = requests.get(url)
    return response.json().get("username")


def retrieve_assigned_tasks(employee_id):
    """
    Retrieves the total number of tasks assigned to the employee.
    """
    url = "{}/{}/todos".format(base_url, employee_id)
    response = requests.get(url)
    return (response.json())


def export_to_json():
    """
    Export tasks for all employees to a JSON file in the desired format.
    """
    tasks_data = {}

    for employee_id in range(1, 11):  
        tasks = retrieve_assigned_tasks(employee_id)
        employee_name = retrieve_employee_name(employee_id)

        employee_data = []
        for task in tasks:
            task_data = {
                "username": employee_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            employee_data.append(task_data)

        tasks_data[str(employee_id)] = employee_data

    tasks_json = json.dumps(tasks_data)

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        jsonfile.write(tasks_json)


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    export_to_json()
