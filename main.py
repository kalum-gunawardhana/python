import json
import os

FILE = "students.json"

# Load data


def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save data


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Create


def create_student():
    students = load_data()
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    student = {"id": len(students) + 1, "name": name,
               "age": age, "course": course}
    students.append(student)
    save_data(students)
    print("Student added successfully!")

# Read


def read_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for s in students:
        print(
            f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")

# Update


def update_student():
    students = load_data()
    read_students()
    sid = int(input("\nEnter student ID to update: "))
    for s in students:
        if s["id"] == sid:
            s["name"] = input("New name: ") or s["name"]
            s["age"] = input("New age: ") or s["age"]
            s["course"] = input("New course: ") or s["course"]
            save_data(students)
            print("Student updated successfully!")
            return
    print("Student not found.")

# Delete


def delete_student():
    students = load_data()
    read_students()
    sid = int(input("\nEnter student ID to delete: "))
    students = [s for s in students if s["id"] != sid]
    save_data(students)
    print("Student deleted successfully!")

# Menu


def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_student()
        elif choice == '2':
            read_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
