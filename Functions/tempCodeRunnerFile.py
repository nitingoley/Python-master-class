    print()

# Function to search for a student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    if roll_no in students:
        print(f"✅ Found: {students[roll_no]}\n")
    else:
        print("❌ Student not found!\n")
