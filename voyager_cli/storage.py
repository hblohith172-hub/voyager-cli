import json
import os

class Task:
    """Simple Task object for easy attribute access."""
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

class TaskStorage:
    def __init__(self, filename="tasks.json"):
        # Store tasks in the same workspace directory
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(self.filename):
            self._save_raw([])

    def add_task(self, title):
        tasks = self._get_raw()
        new_id = max([t['id'] for t in tasks], default=0) + 1
        tasks.append({'id': new_id, 'title': title, 'done': False})
        self._save_raw(tasks)
        return new_id

    def get_all_tasks(self):
        """Returns a list of Task objects."""
        data = self._get_raw()
        return [Task(**t) for t in data]

    def mark_done(self, task_id):
        tasks = self._get_raw()
        found = False
        for t in tasks:
            if t['id'] == task_id:
                t['done'] = True
                found = True
        if not found:
            raise ValueError(f"Task {task_id} not found.")
        self._save_raw(tasks)

    def _get_raw(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def _save_raw(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
"""Storage module for voyager-cli."""


