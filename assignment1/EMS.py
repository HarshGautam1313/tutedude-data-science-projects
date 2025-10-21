# Step 1 - Initialize employee data
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Amit", "age": 30, "department": "IT", "salary": 65000},
    103: {"name": "Riya", "age": 25, "department": "Finance", "salary": 55000},
}


# Step 3 - Add Employee
def add_employee():
    print("\n--- Add New Employee ---")
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("❌ Employee ID already exists! Try another ID.")
            return
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary,
        }
        print(f"✅ Employee '{name}' added successfully!")

    except ValueError:
        print("⚠️ Invalid input! Please enter correct data types.")


# Step 4 - View All Employees
def view_employees():
    print("\n--- All Employees ---")
    if not employees:
        print("No employees available.")
        return

    print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<15}{'Salary':<10}")
    print("-" * 65)
    for emp_id, info in employees.items():
        print(
            f"{emp_id:<10}{info['name']:<20}{info['age']:<10}{info['department']:<15}{info['salary']:<10}"
        )


# Step 5 - Search Employee
def search_employee():
    print("\n--- Search Employee ---")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}")
        else:
            print("❌ Employee not found.")
    except ValueError:
        print("⚠️ Invalid Employee ID!")


# Step 2 & 6 - Menu System
def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("🙏 Thank you for using the Employee Management System!")
            break
        else:
            print("⚠️ Invalid choice! Please select between 1-4.")


# Run the program
if __name__ == "__main__":
    main_menu()
