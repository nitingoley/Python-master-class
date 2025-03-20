#  Mini Project: Student Management System
# Features:
# ✅ Add a student
# ✅ View all students
# ✅ Search for a student
# ✅ Update student marks
# ✅ Delete a student  


students= {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    students[roll_no] = {"name": name ,  "marks": marks}
    print(f"Student {name} added successfully\n")


# Function to display all students
def view_students():
    if not students:
        print("No Students found!\n")
        return 
    print("\n Student List:")
    for roll_no , details in students.items():
        print(f"Roll No: {roll_no} , Name: {details['name']}, Marks: {details['marks']}")
    print()

# Function to search for a student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    if roll_no in students:
        print(f"✅ Found: Roll No: {roll_no}, Name: {students[roll_no]['name']}, Marks: {students[roll_no]['marks']}\n")
    else:
        print("❌ Student not found!\n")



# Function to update marks

def update_marks():
    roll_no = input("Enter Roll to Update Marks: ")
    if roll_no in students:
        new_marks = float(input("Enter New Marks: "))
        students[roll_no]['marks'] = new_marks
        print("✅ Marks updated successfully!\n")
    else:
        print("❌ Student not found!\n")

# Function to delete a student

def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully\n")
    else:
        print("❌ Student not found!\n")


# Main menu loop

while True:
    print("\n🎓 Student Management System 🎓")
    print("1️⃣ Add Student")
    print("2️⃣ View Students")
    print("3️⃣ Search Student")
    print("4️⃣ Update Marks")
    print("5️⃣ Delete Student")
    print("6️⃣ Exit")
    
    choice = input('Enter your choice: ')

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Existing ... Thank you!")
        break 
    else:
        print("❌ Invalid Choice! Please enter a valid option.\n")