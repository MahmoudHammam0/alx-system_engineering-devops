#!/usr/bin/python3
'Gather data from an API module'
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    main_url = "https://jsonplaceholder.typicode.com"
    name_url = "{}/users?id={}".format(main_url, emp_id)
    tasks_url = "{}/todos?userId={}".format(main_url, emp_id)
    name_req = requests.get(name_url)
    tasks_req = requests.get(tasks_url)
    emp_name = name_req.json()[0].get("name")
    no_tasks = len(tasks_req.json())
    no_done = 0
    for task in tasks_req.json():
        if task['completed'] is True:
            no_done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, no_done, no_tasks))
    for task in tasks_req.json():
        if task['completed'] is True:
            print("     {}".format(task['title']))
