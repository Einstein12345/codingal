import json

FILE_NAME = "applications.json"

def load_applications():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_applications(applications):
    with open(FILE_NAME, "w") as file:
        json.dump(applications, file, indent=4)

def add_application(applications):
    print("\n--- New Application ---")
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade applying for: ")
    parent = input("Enter parent/guardian name: ")

    application = {
        "name": name,
        "age": age,
        "grade": grade,
        "parent": parent
    }

    applications.append(application)
    save_applications(applications)
    print("Application submitted successfully!\n")

def view_applications(applications):
    print("\n--- All Applications ---")
    if not applications:
        print("No applications found.")
        return

    for i, app in enumerate(applications, 1):
        print(f"\nApplication {i}")
        print(f"Name: {app['name']}")
        print(f"Age: {app['age']}")
        print(f"Grade: {app['grade']}")
        print(f"Parent: {app['parent']}")

def search_application(applications):
    name = input("Enter name to search: ").lower()
    found = False

    for app in applications:
        if app["name"].lower() == name:
            print("\n--- Application Found ---")
            print(app)
            found = True

    if not found:
        print("No application found.")

def main():
    applications = load_applications()

    while True:
        print("\n--- School Application System ---")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Application")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            search_application(applications)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__== "main":
    main()      