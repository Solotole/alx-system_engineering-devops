#!/usr/bin/python3
""" script to send request and get response
    from an open source API
"""
if __name__ == '__main__':
    import json
    import requests
    import sys
    file_name = f"{sys.argv[1]}.json"
    complete_dict = {}
    mini_dict = {}
    lists = []
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    user = r.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    for task in todos.json():
        if task.get('userId') == int(sys.argv[1]):
            mini_dict['task'] = task.get('title')
            mini_dict['completed'] = task.get('completed')
            mini_dict['username'] = user
            lists.append(mini_dict)
            mini_dict = {}
    complete_dict[sys.argv[1]] = lists

    with open(file_name, 'w') as f:
        json_object = json.dumps(complete_dict)
        f.write(json_object)
