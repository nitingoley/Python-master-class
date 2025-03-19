# Mini Project: Student Report Card 📚
# This project will help you practice dictionaries by creating a simple report card system where you can:
# ✅ Store student details (name, subjects, and marks)
# ✅ Calculate total and percentage
# ✅ Find the highest and lowest scoring subject 



student = {"name": input("Enter Student Name: ")}

student["subjects"] = {}

num_subjects = int(input("Enter number of subjects: "))


for _ in range(num_subjects):
    subject = input("Enter subject name: ")
    marks = int(input(f"Enter marks for {subject}: "))
    student["subjects"][subject] = marks 

print("\n Student Name:", student["name"])
print("\n Subjects & Marks:") 
for subject , marks in student["subjects"].items():
        print(f"  {subject}: {marks}")


marks_list = list(student["subjects"].values())
total_marks= sum(marks_list)
percentage = total_marks / len(marks_list)

print("\n Total Marks:" , total_marks)
print("Percentage", round(percentage, 2), "%")

highest_subject = max(student["subjects"], key=student["subjects"].get)
lowest_subject = min(student["subjects"], key=student["subjects"].get) 

print("\n Highest Score: " , highest_subject , "-" , subject["subjects"][highest_subject])
print("Lowest Score:" , lowest_subject , "-" , student["subjects"][lowest_subject])


