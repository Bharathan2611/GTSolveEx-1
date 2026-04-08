"""
Write a well structured clean code for task manager application.
Mock Data:
https://jsonplaceholder.typicode.com/todos

step 1: Create a class to manage tasks
Step 2:fetch data from API
step 3: Check response status code is 200
step 4:  filter completed and pending tasks
step 5: Add New Task
step 6: Updated Task 
Step 7: Delete Task
Step 9: Covert data to DataFrame
Step 10: Save Tasks to CSV
"""

import pandas as pd 

import requests

#Step 1: Create a class to manage tasks
class TaskManager:
    def __init__(self, url):
        self.url = url
        self.tasks = []

    #Step 2:fetch data from API
    def fetch_tasks(self):
        response = requests.get(self.url)

        #Step 3: Check response status code is 200
        if response.status_code == 200:
            self.tasks = response.json()
        else:
            raise ValueError("Failed to fetch data from API")

    #Step 4:  filter completed and pending tasks
    def filter_tasks(self):
        completed_tasks = []
        pending_tasks = []
        for task in self.tasks:
            if task.get("completed"):
                completed_tasks.append(task)
            else:
                pending_tasks.append(task)
        return completed_tasks, pending_tasks
    
    #Step 5: Add New Task
    def add_task(self, title, completed=False):
        new_task = {
            "userId": 1,
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": completed
        }
        self.tasks.append(new_task)
    #Step 6: Updated Task
    def update_task(self, task_id, title=None, completed=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if title is not None:
                    task["title"] = title
                if completed is not None:
                    task["completed"] = completed
                return
        raise ValueError("Task not found")
    
    #Step 7: Delete Task
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
    #Step 9: Covert data to DataFrame
    def to_dataframe(self):
        return pd.DataFrame(self.tasks)
    #Step 10: Save Tasks to CSV
    def save_to_csv(self, filename):
        df = self.to_dataframe()
        df.to_csv(filename, index=False)

url= "https://jsonplaceholder.typicode.com/todos"
task_manager = TaskManager(url)
try:
    task_manager.fetch_tasks()
    completed, pending = task_manager.filter_tasks()
    print("Total Tasks:", len(task_manager.tasks))
    print("Completed Tasks:", len(completed))
    print("Pending Tasks:", len(pending))
except ValueError as e:
    print(e)

added_task = "Task from GT Solve Exercise"
task_manager.add_task(added_task)
print("Added Task:", added_task)

updated_task_id = 2
updated_title = "Vijayalakshmi Updated Task"
task_manager.update_task(updated_task_id, title=updated_title)
print(f"Updated Task with ID {updated_task_id}: {updated_title}")

deleted_task_id = 1
task_manager.delete_task(deleted_task_id)
print(f"Deleted Task with ID: {deleted_task_id}")

to_dataframe = task_manager.to_dataframe()
print(to_dataframe.head())

print("Length of Tasks:", len(task_manager.tasks))


task_manager.save_to_csv("Task Data.csv")