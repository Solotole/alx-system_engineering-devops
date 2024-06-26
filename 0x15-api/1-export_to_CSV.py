#!/usr/bin/python3
""" script to send request and get response
    from an open source API and represent in csv format
"""


if __name__ == '__main__':
    import csv
    import requests
    import sys
    file_name = f"{sys.argv[1]}.csv"
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    user = r.json().get('username')
    userid = r.json().get('id')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    with open(file_name, 'w') as files:
        csv_writer = csv.writer(files, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in todos.json():
            if task.get('userId') == int(sys.argv[1]):
                csv_writer.writerow([userid, user,
                                    str(task.get('completed')),
                                    task.get('title')])
