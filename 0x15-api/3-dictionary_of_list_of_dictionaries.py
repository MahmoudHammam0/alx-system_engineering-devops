#!/usr/bin/python3
'Dictionary of list of dictionaries module'
import json
import requests


if __name__ == "__main__":
    res = {}
    main_url = "https://jsonplaceholder.typicode.com"
    for emp_id in range(1, 11):
        new_list = []
        name_url = "{}/users?id={}".format(main_url, emp_id)
        tasks_url = "{}/todos?userId={}".format(main_url, emp_id)
        name_req = requests.get(name_url)
        tasks_req = requests.get(tasks_url)
        emp_name = name_req.json()[0].get("username")
        new_dict = {}
        for task in tasks_req.json():
            new_dict['username'] = emp_name
            new_dict['task'] = task['title']
            new_dict['completed'] = task['completed']
            new_list.append(new_dict)
            new_dict = {}
        res[emp_id] = new_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(res, f)
