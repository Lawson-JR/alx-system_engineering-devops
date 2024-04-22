#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        if employee_response.status_code != 200 or todos_response.status_code != 200:
            print("Failed to fetch data. Please try again later.")
            return

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        employee_name = employee_data['name']

        completed_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos_data)

        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
