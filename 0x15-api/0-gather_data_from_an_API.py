#!/usr/bin/python3
"""
    Gather data from an API
"""
import json
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

# Get employee ID from command line arguments
employee_id = int(sys.argv[1])

response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': employee_id}
        )
response_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
# Parse JSON response
todos = response_todos.json()
user = response_user.json()

# Extracting employee name
employee_name = set()
for todo in todos:
    employee_name.add(todo['userId'])

# Calculate progress
total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo['completed'])


# Displaying information
print(f"Employee {user['name']} is done with tasks "
      f"({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo['completed']:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    # Check if an argument (employee ID) is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line arguments
    employee_id = int(sys.argv[1])
