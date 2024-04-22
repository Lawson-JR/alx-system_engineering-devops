#!/usr/bin/python3
"""
Module documentation goes here.
"""

import sys
import json
import requests

def fetch_todo_list_progress(employee_id):
    """
    Function documentation goes here.
    """
    # Define the base URL of the API endpoint
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URL with the employee ID
    url = f"{base_url}/todos?userId={employee_id}"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        todos = response.json()

        # Calculate progress
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo["completed"])

        # Get employee name
        employee_name = todos[0]["username"]  # Assuming username is available in the response

        # Display output
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for todo in todos:
            if todo["completed"]:
                print(f"\t{todo['title']}")

    else:
        print("Failed to fetch TODO list. Please try again later.")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Parse employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Fetch and display TODO list progress
    fetch_todo_list_progress(employee_id)
