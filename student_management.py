import csv
import os

filename = "students_management.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Name", "Marks"])


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def display_students():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student():
    roll = input("Enter roll number to search: ")

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                print("Student found:", row)
                return

    print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")

    with open(filename, "r") as file:
        rows = list(csv.reader(file))

    new_rows = [rows[0]]

    found = False

    for row in rows[1:]:
        if row[0] == roll:
            found = True
        else:
            new_rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")