# Zero Check Decorator

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# Example usage:
# print(div(6, 2))
# print(div(6, 0))

# Employee Records Manager

def employee_menu():
    filename = "employees.txt"

    def add_employee():
        with open(filename, 'a') as f:
            emp_id = input("Employee ID: ")
            name = input("Name: ")
            position = input("Position: ")
            salary = input("Salary: ")
            f.write(f"{emp_id}, {name}, {position}, {salary}\n")

    def view_employees():
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("No records found.")

    def search_employee():
        eid = input("Enter Employee ID to search: ")
        found = False
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith(eid + ","):
                    print("Record found:", line.strip())
                    found = True
        if not found:
            print("Employee not found.")

    def update_employee():
        eid = input("Enter Employee ID to update: ")
        lines = []
        found = False
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            for line in lines:
                if line.startswith(eid + ","):
                    name = input("New name: ")
                    position = input("New position: ")
                    salary = input("New salary: ")
                    f.write(f"{eid}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    f.write(line)
        if not found:
            print("Employee not found.")

    def delete_employee():
        eid = input("Enter Employee ID to delete: ")
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            for line in lines:
                if not line.startswith(eid + ","):
                    f.write(line)
        print("Deleted if existed.")

    while True:
        print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
        choice = input("Choose an option: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            break
        else:
            print("Invalid option.")

# Word Frequency Counter
import os
import string
from collections import Counter

def word_frequency():
    if not os.path.exists("sample.txt"):
        print("sample.txt not found. Please type a paragraph to create it:")
        with open("sample.txt", 'w') as f:
            f.write(input("Enter text: "))

    with open("sample.txt", 'r') as f:
        text = f.read()

    # Clean and process
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    counter = Counter(words)
    total = sum(counter.values())

    try:
        top_n = int(input("How many top common words to display? "))
    except ValueError:
        top_n = 5

    top_words = counter.most_common(top_n)

    print(f"Total words: {total}")
    print("Top words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", 'w') as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total}\n")
        f.write("Top Words:\n")
        for word, count in top_words:
            f.write(f"{word} - {count}\n")

# Uncomment to run
# print(div(6, 0))
# employee_menu()
# word_frequency()
