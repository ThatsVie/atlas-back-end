# API

The API project interacts with a mock REST API available at [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/). It comprises four Python scripts designed to manage tasks for employees, offering various features including exporting tasks for specific users and all employees to JSON files. Structured to streamline task management and facilitate data export for further analysis or integration with other systems, the project simplifies the process of fetching, organizing, and exporting data in different formats using Python.


## Tasks

### 0-gather_data_from_an_API.py:

The Python script **0-gather_data_from_an_API.py** utilizes a REST API to fetch and display information about the progress of a given employee's TODO list. It accepts an employee ID as a parameter, retrieves the tasks associated with that employee from the API, and outputs the employee's name, the number of completed tasks out of the total tasks, and the titles of completed tasks with appropriate formatting.

### 1-export_to_CSV.py:

The Python script **1-export_to_CSV.py** extends the functionality from **0-gather_data_from_an_API.py** by exporting the retrieved data in CSV format. It records all tasks owned by the specified employee in a CSV file named after the user ID, with each row containing the user ID, username, task completion status, and task title, separated by commas.

### 2-export_to_JSON.py:

The Python script **2-export_to_JSON.py** builds upon **0-gather_data_from_an_API.py** by exporting the retrieved data in JSON format. It records all tasks owned by the specified employee in a JSON file named after the user ID, with each task represented as an object containing task title, completion status, and username, all nested under the user ID.

### 3-dictionary_of_list_of_dictionaries.py:

The Python script **3-dictionary_of_list_of_dictionaries.py** extends the functionality of  **0-gather_data_from_an_API.py** by exporting data in JSON format for all tasks from all employees. It organizes the tasks under each user ID, with each task represented as an object containing the task title, completion status, and username. The resulting JSON file is named todo_all_employees.json.


## Requirements

- Python 3.x
- requests library

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ThatsVie/atlas-back-end.git
    ```

2. Navigate to the project directory:

    ```bash
    cd api
    ```

3. Install the required dependencies:

    ```bash
    pip install requests
    ```
