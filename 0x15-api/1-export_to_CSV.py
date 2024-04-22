#!/usr/bin/python3
"""
Module documentation goes here.
"""

import sys
import json
import requests
import csv

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

        # Define CSV file name
        csv_filename = f"{employee_id}.csv"

        # Open CSV file in write mode
        with open(csv_filename, mode='w', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile, delimiter=',')

            # Write header
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write data for each task
            for todo in todos:
                csv_writer.writerow([todo["userId"], todo["username"], todo["completed"], todo["title"]])

        print(f"CSV file '{csv_filename}' has been created successfully.")

    else:
        print("Failed to fetch TODO list. Please try again later.")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Parse employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Fetch and export TODO list progress to CSV
    fetch_todo_list_progress(employee_id)
