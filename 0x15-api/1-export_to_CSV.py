#!/usr/bin/python3
'Export to CSV module'
import csv
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
    with open('{}.csv'.format(emp_id), 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks_req.json():
            write.writerow([emp_id, emp_name, task['completed'],
                           task['title']])
