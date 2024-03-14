#!/usr/bin/python3
"""
- Script to Retrieve Employee TODO List Progress
- Utilizes either the urllib or requests module to interact with the REST API
- Accepts an integer as a parameter, representing the employee ID.
- Output Format: The script must display the employee's TODO list progress
in the following exact format:
- The first line should indicate the employee's name and their progress
with tasks, represented as (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
- EMPLOYEE_NAME: Name of the employee.
- NUMBER_OF_DONE_TASKS: Number of completed tasks.
- TOTAL_NUMBER_OF_TASKS: Total number of tasks, including both
completed and non-completed tasks.
- The subsequent lines should display the titles of completed tasks,
with one tabulation and one space before each task title.
- Extended to export data in the CSV format.
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""
import csv
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com/users"


def retrieve_employee_name(employee_id):
    """
    Retrieves the name of the employee.
    """
    url = f"{BASE_URL}/{employee_id}"
    response = requests.get(url)
    return response.json().get("name")


def retrieve_assigned_tasks(employee_id):
    """
    Retrieves all tasks assigned to the employee.
    """
    url = f"{BASE_URL}/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def retrieve_completed_tasks(employee_id):
    """
    Retrieves the list of completed tasks by the employee.
    """
    completed_tasks = []
    url = f"{BASE_URL}/{employee_id}/todos"
    response = requests.get(url)
    for task in response.json():
        if task.get("completed"):
            completed_tasks.append(task.get("title"))
    return completed_tasks


def print_employee_progress(employee_name, completed_tasks, assigned_tasks):
    """
    Prints the employee's task list progress and exports it to CSV.
    """
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          len(completed_tasks),
                                                          len(assigned_tasks)))
    for task in completed_tasks:
        print("\t{}".format(task))

    with open('{}.csv'.format(employee_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in assigned_tasks:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_name = retrieve_employee_name(employee_id)
    assigned_tasks = retrieve_assigned_tasks(employee_id)
    completed_tasks = retrieve_completed_tasks(employee_id)
    print_employee_progress(employee_name, completed_tasks, assigned_tasks)
