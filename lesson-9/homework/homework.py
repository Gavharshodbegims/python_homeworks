# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

# Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)

# Test
if __name__ == "__main__":
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")
    lib.add_member("Alice")

    try:
        lib.borrow("Alice", "1984")
        lib.borrow("Alice", "The Hobbit")
        lib.return_book("Alice", "1984")
        lib.borrow("Alice", "Unknown Book")
    except Exception as e:
        print("Error:", e)

#2

import csv
from collections import defaultdict

# Read grades from CSV
grades = []
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append({"name": row["Name"], "subject": row["Subject"], "grade": int(row["Grade"])})

# Calculate averages
subject_totals = defaultdict(list)
for entry in grades:
    subject_totals[entry["subject"]].append(entry["grade"])

averages = [{"Subject": sub, "Average Grade": round(sum(grades) / len(grades), 2)}
            for sub, grades in subject_totals.items()]

# Write averages to CSV
with open("average_grades.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    writer.writerows(averages)

#3

import json
import csv

# Load tasks from JSON
with open("tasks.json", "r") as f:
    tasks = json.load(f)

# Display tasks
for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# Calculate stats
total_tasks = len(tasks)
completed_tasks = sum(1 for t in tasks if t["completed"])
pending_tasks = total_tasks - completed_tasks
avg_priority = round(sum(t["priority"] for t in tasks) / total_tasks, 2)

print("\n--- Task Stats ---")
print(f"Total tasks: {total_tasks}")
print(f"Completed tasks: {completed_tasks}")
print(f"Pending tasks: {pending_tasks}")
print(f"Average priority: {avg_priority}")

# Save updated tasks (if any modifications made)
with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)

# Convert to CSV
with open("tasks.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Task", "Completed", "Priority"])
    writer.writeheader()
    for task in tasks:
        writer.writerow({
            "ID": task["id"],
            "Task": task["task"],
            "Completed": task["completed"],
            "Priority": task["priority"]
        })
