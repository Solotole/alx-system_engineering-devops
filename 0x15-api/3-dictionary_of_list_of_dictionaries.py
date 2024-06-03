#!/usr/bin/python3
""" script to send request and get response
    from an open source API of all users and converting
    into json format
"""
if __name__ == '__main__':
    import json
    import requests

    main_dict = {}
    mini_dict = {}
    lists = []
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for user in r.json():
        user_name = user.get('username')
        user_id = user.get('id')
        for task in todos.json():
            if user_id == task.get('userId'):
                tasks = task.get('title')
                status = task.get('completed')
                mini_dict['username'] = user_name
                mini_dict['task'] = tasks
                mini_dict['completed'] = status
                lists.append(mini_dict)
                mini_dict = {}
            else:
                continue
        main_dict[user_id] = lists
        lists = []

    with open('todo_all_employees.json', 'w') as files:
        json_object = json.dumps(main_dict)
        files.write(json_object)
