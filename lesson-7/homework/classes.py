# Generalized Vector Class
import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of same dimension")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            return Vector(*[a * other for a in self.components])

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[round(a / mag, 3) for a in self.components])


# Employee Records Manager (OOP Version)
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w"):
                pass

    def add_employee(self):
        eid = input("Enter Employee ID: ")
        if self.search_employee(eid, silent=True):
            print("Employee ID already exists!")
            return
        name = input("Enter Name: ")
        pos = input("Enter Position: ")
        sal = input("Enter Salary: ")
        emp = Employee(eid, name, pos, sal)
        with open(self.FILE, "a") as f:
            f.write(str(emp) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE) as f:
            lines = f.readlines()
        print("Employee Records:")
        for line in lines:
            print(line.strip())

    def search_employee(self, eid, silent=False):
        with open(self.FILE) as f:
            for line in f:
                if line.startswith(eid + ","):
                    if not silent:
                        print("Employee Found:\n" + line.strip())
                    return line.strip()
        if not silent:
            print("Employee not found.")
        return None

    def update_employee(self):
        eid = input("Enter Employee ID to update: ")
        records = []
        found = False
        with open(self.FILE) as f:
            for line in f:
                if line.startswith(eid + ","):
                    name = input("New Name: ")
                    pos = input("New Position: ")
                    sal = input("New Salary: ")
                    records.append(f"{eid}, {name}, {pos}, {sal}\n")
                    found = True
                else:
                    records.append(line)
        if found:
            with open(self.FILE, "w") as f:
                f.writelines(records)
            print("Employee updated.")
        else:
            print("Employee not found.")

    def delete_employee(self):
        eid = input("Enter Employee ID to delete: ")
        with open(self.FILE) as f:
            lines = f.readlines()
        with open(self.FILE, "w") as f:
            deleted = False
            for line in lines:
                if not line.startswith(eid + ","):
                    f.write(line)
                else:
                    deleted = True
        if deleted:
            print("Employee deleted.")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
            choice = input("Enter your choice: ")
            match choice:
                case '1': self.add_employee()
                case '2': self.view_all_employees()
                case '3': self.search_employee(input("Enter Employee ID: "))
                case '4': self.update_employee()
                case '5': self.delete_employee()
                case '6': print("Goodbye!"); break
                case _: print("Invalid choice.")


# To-Do Application
import json
import csv
from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

class Storage(ABC):
    @abstractmethod
    def load(self): pass
    @abstractmethod
    def save(self, tasks): pass

class JSONStorage(Storage):
    FILE = "tasks.json"

    def load(self):
        try:
            with open(self.FILE) as f:
                data = json.load(f)
                return [Task(**d) for d in data]
        except FileNotFoundError:
            return []

    def save(self, tasks):
        with open(self.FILE, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)

class ToDoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self):
        tid = input("Task ID: ")
        title = input("Title: ")
        desc = input("Description: ")
        due = input("Due Date (YYYY-MM-DD): ")
        status = input("Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(tid, title, desc, due, status))
        print("Task added.")

    def view_tasks(self):
        for t in self.tasks:
            print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")

    def update_task(self):
        tid = input("Enter Task ID: ")
        for t in self.tasks:
            if t.task_id == tid:
                t.title = input("New Title: ")
                t.description = input("New Description: ")
                t.due_date = input("New Due Date: ")
                t.status = input("New Status: ")
                print("Task updated.")
                return
        print("Task not found.")

    def delete_task(self):
        tid = input("Enter Task ID: ")
        self.tasks = [t for t in self.tasks if t.task_id != tid]
        print("Task deleted.")

    def filter_tasks(self):
        status = input("Enter status to filter: ")
        for t in self.tasks:
            if t.status.lower() == status.lower():
                print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved.")

    def menu(self):
        while True:
            print("""
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
""")
            choice = input("Enter your choice: ")
            match choice:
                case '1': self.add_task()
                case '2': self.view_tasks()
                case '3': self.update_task()
                case '4': self.delete_task()
                case '5': self.filter_tasks()
                case '6': self.save_tasks()
                case '7': self.tasks = self.storage.load(); print("Tasks loaded.")
                case '8': break
                case _: print("Invalid choice.")
