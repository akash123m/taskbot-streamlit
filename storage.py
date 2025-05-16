import json
from datetime import datetime

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task, time):
    tasks = load_tasks()
    tasks.append({"task": task, "time": time, "status": "pending", "created": str(datetime.now())})
    save_tasks(tasks)

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['status'] = "done"
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
    save_tasks(tasks)

def get_tasks():
    return load_tasks()
