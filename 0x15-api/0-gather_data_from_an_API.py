#!/usr/bin/python3
""" script to send request and get response
    from an open source API
"""
if __name__ == '__main__':
    import requests
    import sys
    completed = 0
    total = 0
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    user = r.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for task in todos.json():
        if task.get('userId') == int(sys.argv[1]):
            total += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks ({}/{}):'
          .format(user, completed, total))
    for task in todos.json():
        if task.get('completed') and task.get('userId') == int(sys.argv[1]):
            print('\n'.join(["\t " + task.get('title')]))
