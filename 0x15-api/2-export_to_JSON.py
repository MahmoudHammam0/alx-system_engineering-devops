#!/usr/bin/python3
'Export to JSON module'
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    main_url = "https://jsonplaceholder.typicode.com"
    name_url = "{}/users?id={}".format(main_url, emp_id)
    tasks_url = "{}/todos?userId={}".format(main_url, emp_id)
    name_req = requests.get(name_url)
    tasks_req = requests.get(tasks_url)
    emp_name = name_req.json()[0].get("username")
    new_list = []
    new_dict = {}
    for task in tasks_req.json():
        new_dict['task'] = task['title']
        new_dict['completed'] = task['completed']
        new_dict['username'] = emp_name
        new_list.append(new_dict)
        new_dict = {}
    res = {}
    res[emp_id] = new_list
    with open('{}.json'.format(emp_id), 'w') as f:
        json.dump(res, f)
